##
##-----------------------------------------------------------------------------
##
## Copyright (c) 2023 JEOL Ltd.
## 1-2 Musashino 3-Chome
## Akishima Tokyo 196-8558 Japan
##
## This software is provided under the MIT License. For full license information,
## see the LICENSE file in the project root or visit https://opensource.org/licenses/MIT
##
##++---------------------------------------------------------------------------
##
## ModuleName : BeautifulJASON
## ModuleType : Python API for JASON desktop application and JJH5 documents
## Purpose : Automate processing, analysis, and report generation with JASON
## Author : Nikolay Larin
## Language : Python
##
####---------------------------------------------------------------------------
##

import beautifuljason.document as document
import configparser
import platform
import subprocess
import os.path
import tempfile
import pathlib
import json
import platform
from functools import cached_property
from copy import copy
from collections.abc import Sequence

class JASONException(Exception):
    """Exception raised for errors specific to the JASON application."""
    pass

class Config:
    """
    Represents the configuration settings for the JASON application.
    """

    if platform.system() == "Windows":
        DEFAULT_CONFIG_CONTENTS = r"""[JASON]
path_1 = C:\Program Files\JEOL\Jason\Jason.exe
path_2 = C:\Program Files\JEOL\Jason-dev\Jason-dev.exe"""
    elif platform.system() == "Darwin":  # Darwin indicates macOS
        DEFAULT_CONFIG_CONTENTS = """[JASON]
path_1 = /Applications/Jason.app/Contents/MacOS/Jason
path_2 = /Applications/Jason-dev.app/Contents/MacOS/Jason-dev"""
    else:
        # Default to a generic configuration or raise an exception
        DEFAULT_CONFIG_CONTENTS = """[JASON]
path_1 =
path_2 ="""

    def __init__(self):
        self.app_path = None
        self.error = ''

        # Define a work directory
        self.work_path = os.path.join(str(pathlib.Path.home()), '.beautifuljason')
        if not os.path.isdir(self.work_path):
            os.mkdir(self.work_path, 0o755)

        # Define a temporary directory. It can be overridden in the config.ini. See _load_config().
        self.temp_path = tempfile.gettempdir()

        self._load_config()

    @property
    def config_path(self) -> str:
        """
        :return: The path to the config.ini file.
        :rtype: str
        """
        return os.path.join(self.work_path, 'config.ini')

    def _load_config(self):
        """Load the JASON application path from the config.ini."""

        self.app_path = None
        self.error = ''

        config_parser = configparser.ConfigParser()
        config_parser.read(self.config_path)
        
        # Read the temp_path from the config if it exists
        if config_parser.has_option('JASON', 'temp_path'):
            self.temp_path = config_parser.get('JASON', 'temp_path')

        # Check if the config is empty and populate it from the default if necessary
        if not config_parser.sections():
            with open(self.config_path, 'w') as configfile:
                configfile.write(self.DEFAULT_CONFIG_CONTENTS)
                
            config_parser.read(self.config_path)  # Reload the config after populating

        # If a preferred path key is specified, use that first
        preferred_key = config_parser.get('JASON', 'preferred_path_key', fallback=None)
        if preferred_key and config_parser.has_option('JASON', preferred_key):
            preferred_path = config_parser.get('JASON', preferred_key)
            if os.path.exists(preferred_path):
                self.app_path = preferred_path
            else:
                self.error = f"Preferred path '{preferred_path}' specified in config.ini not found."
                return
            
        if self.app_path is None:
            # If the preferred path is not found or not specified, fall back to the default paths
            path_keys = [f"path_{i}" for i in range(1, 11)]  # Check paths from path_1 to path_10
            for key in path_keys:
                if config_parser.has_option('JASON', key):
                    path = config_parser.get('JASON', key)
                    if os.path.exists(path):
                        self.app_path = path
                        break

        if self.app_path is None:
            self.error = "No valid JASON application path found in config.ini."

    def add_path(self, new_path: str) -> int:
        """Add a new JASON instance path to the config.

        :param new_path: The new path to add for the JASON instance.
        :type new_path: str

        :return: The index of the new path.
        :rtype: int

        :raises JASONException: If the path already exists in the config.
        """
        config_parser = configparser.ConfigParser()
        config_parser.read(self.config_path)
        
        # Check if the path already exists
        if new_path in config_parser['JASON'].values():
            raise JASONException(f"The path '{new_path}' is already in the config.")
        
        highest_index = 0

        # Iterate over all items in the 'JASON' section and find the highest path index
        for key in config_parser['JASON']:
            if key.startswith('path_'):
                index = int(key.split('_')[1])
                highest_index = max(highest_index, index)

        # Create a new slot for the new path
        new_key = f"path_{highest_index + 1}"
        config_parser.set('JASON', new_key, new_path)
        
        with open(self.config_path, 'w') as configfile:
            config_parser.write(configfile)
            
        return highest_index + 1

    def set_preferred_path_index(self, path_index: int):
        """Set a new preferred JASON instance path index.

        :param path_index: The new path to set as preferred for the JASON instance.
        :type path_index: int
        """
        config_parser = configparser.ConfigParser()
        config_parser.read(self.config_path)
        path_key = f"path_{path_index}"
        if not config_parser.has_option('JASON', path_key):
            raise JASONException(f"No path found at index {path_index}.")
        config_parser.set('JASON', 'preferred_path_key', path_key)
        with open(self.config_path, 'w') as configfile:
            config_parser.write(configfile)
        self._load_config()  # Reload the configuration after setting the preferred path

    # Return the preferred path index or None if the preferred path is not set
    @property
    def preferred_path_index(self) -> int | None:
        """
        :return: The index of the preferred JASON instance path.
        :rtype: int | None
        """
        config_parser = configparser.ConfigParser()
        config_parser.read(self.config_path)
        preferred_key = config_parser.get('JASON', 'preferred_path_key', fallback=None)
        if preferred_key:
            return int(preferred_key.split('_')[1])
        else:
            return None

    def delete_path_by_index(self, index):
        """Delete a JASON instance path by its index.

        :param index: The index of the path to delete.
        :type index: int
        """

        if index == 1 or index == 2:
            raise JASONException("The default paths at index 1 and 2 cannot be deleted.")

        config_parser = configparser.ConfigParser()
        config_parser.read(self.config_path)

        # Find the key for the path at the specified index
        path_key = f"path_{index}"
        if not config_parser.has_option('JASON', path_key):
            raise JASONException(f"No path found at index {index}.")

        # Remove the path from the config
        config_parser.remove_option('JASON', path_key)
        with open(self.config_path, 'w') as configfile:
            config_parser.write(configfile)

        # If the path was the preferred path, remove the preferred path key
        if index == self.preferred_path_index:
            config_parser.remove_option('JASON', 'preferred_path_key')

        self._load_config()

    def reset(self):
        """Reset the configuration to the default settings."""
        with open(self.config_path, 'w') as configfile:
            configfile.write(self.DEFAULT_CONFIG_CONTENTS)
        
        self._load_config()  # Reload the configuration after resetting

    @property
    def all_paths(self) -> list[tuple[int, str]]:
        """
        :return: A list of all JASON application paths from the config.
        :rtype: :obj:`list[tuple[int, str]]`
        """
        config_parser = configparser.ConfigParser()
        config_parser.read(config.config_path)

        paths = []
        for key in config_parser['JASON']:
            if key.startswith('path_'):
                index = int(key.split('_')[1])
                path = config_parser['JASON'][key]
                paths.append((index, path))
        return paths

# Instantiate the Config class
config = Config()

class JASON:
    """
    Represents the main interface for interacting with the JASON application.

    :param app_path: The path to the JASON application. If not provided, it will be fetched from the configuration.
    :type app_path: str | None

    :raises JASONException: If the JASON app path is not specified or does not exist.
    """

    def __init__(self, app_path: str | None = None):
        if app_path is None:
            app_path = config.app_path
            if not app_path:
                raise JASONException('JASON path not specified in config and not provided during initialization.')

        if not os.path.isfile(app_path):
            raise JASONException(f'JASON path does not exist: {app_path}')

        self.app_dir = os.path.dirname(app_path)
        self.app_name = os.path.join('.', os.path.basename(app_path))

        if len(self.version) != 3:
            raise JASONException(f'Unexpected version: {self.version}')

        minVersion = (0, 1, 1924)
        if self.version < minVersion:
            raise JASONException(f'Old JASON version: {".".join(map(str, self.version))}. The minimal supported version is {".".join(map(str, minVersion))}')

    def _run(self, args):
        old_wd = os.getcwd()    
        os.chdir(self.app_dir)
        try:
            runres = subprocess.run([self.app_name, '--headless'] + args, capture_output=True)
        finally:
            os.chdir(old_wd)
        if runres.returncode != 0:
            raise JASONException("JASON finished with an error code {}".format(runres.returncode))
        return runres

    @cached_property
    def version(self) -> tuple[int, int, int] | None:
        """
        :return: The JASON version as a tuple of integers. Empty tuple if the version cannot be determined.
        :rtype: :obj:`tuple` of :obj:`int` | :obj:`tuple`
        """
        runres = self._run(['-v'])
        if runres.returncode == 0:
            return tuple(int(i) for i in runres.stdout.split(b' ')[-1].split(b'.'))
        else:
            return None

    def create_document(self, file_names: list[str] | str, actions: list[dict] = [], rules: str = "off") -> 'document.Document':
        """
        Creates a JASON document based on provided files and actions.

        :param file_names: List of file names or a single file name to be processed.
        :type file_names: :obj:`list[str]` | :obj:`str`
        :param actions: Actions to apply to the files. Defaults to an empty list.
        :type actions: :obj:`list[dict]`, optional
        :param rules: "on", "off", or library name for processing rules. Defaults to "off".
        :type rules: str, optional

        :return: The created JASON document.
        :rtype: :obj:`document.Document`
        """
        if isinstance(file_names, str):
            file_names = [file_names]
        saved_file_name = tempfile.mktemp(suffix='.jjh5', dir=config.temp_path)
        actions_file_name = self._create_actions_file(actions)
        if actions_file_name:
            new_file_names = []
            for fname in file_names:
                new_file_names.append(fname)
                new_file_names.append(actions_file_name)
            file_names = new_file_names
        self._run(file_names + ['-s', saved_file_name] + ['--rules', rules])
        if actions_file_name:
            os.remove(actions_file_name)
        return document.Document(saved_file_name, is_temporary=True)

    def launch(self, args):
        """
        Launches the JASON application with the provided arguments. 

        :param args: The arguments to pass to the JASON application.
        :type args: :obj:`list[str]`
        """
        if platform.system() == 'Windows':
            start = 'start "JASON"'
        else:
            start = 'open'
        os.system(start + ' ' + '"{}"'.format(os.path.join(self.app_dir, self.app_name)) + ' ' + ' '.join(['"{}"'.format(arg) if ' ' in arg else arg for arg in args]))

    def apply_actions(self, doc: document.Document, actions: list[dict]):
        """
        Applies the specified actions to a JASON document.

        :param doc: The JASON document to which the actions should be applied.
        :type doc: :obj:`Document`
        :param actions: The actions to apply.
        :type actions: :obj:`list[dict]`
        """
        actions_file_name = self._create_actions_file(actions)        
        doc.close()
        self._run([doc.file_name, actions_file_name, '-s', doc.file_name])
        doc.load()
        if actions_file_name:
            os.remove(actions_file_name)

    def _create_actions_file(self, actions):
        """
        Creates a temporary actions file based on the provided actions.
        """
        actions_file_name = ''
        if actions:
            actions_file_name = tempfile.mktemp(suffix='.jja', dir=config.temp_path)
            with open(actions_file_name, 'w') as f:
                f.write(json.dumps(actions))
        return actions_file_name

    def save(self, doc: document.Document, file_names: list[str] | str, actions: list[dict]=[]):
        """
        Saves the JASON document to the specified file names after applying the given actions. The file format is determined by the file extension.

        :param doc: The JASON document to save.
        :type doc: :obj:`Document`

        :param file_names: List of file names or a single file name to save the document to.
        :type file_names: :obj:`list[str]` | :obj:`str`

        :param actions: Actions to apply to the document before saving. Defaults to an empty list.
        :type actions: :obj:`list[dict]`, optional
        """
        if isinstance(file_names, str):
            file_names = [file_names]

        actions_file_name = self._create_actions_file(actions)

        save_args = []
        for file_name in file_names:
            save_args += ['-s', file_name]
        if isinstance(doc, document.Document):
            doc.close()
            args = [doc.file_name]
            if actions_file_name:
                args.append(actions_file_name)
            self._run(args + save_args)
            doc.load()
        else:
            if isinstance(doc, str):
                open_file_names = [doc]
            elif isinstance(doc, Sequence):
                open_file_names = list(doc)
            self._run(open_file_names + save_args)

        if actions_file_name:
            os.remove(actions_file_name)
