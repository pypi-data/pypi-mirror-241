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

import beautifuljason.graphics as graphics
import beautifuljason.data as data
import beautifuljason.utils as utils
import numpy as np
from typing import Iterable
import os
import shutil
import h5py
from PIL import Image as PILImage

class Document:
    """
    Represents a JASON document, providing methods to manipulate and extract data from it.

    :param file_name: The file name of the JASON document.
    :type file_name: str
    :param is_temporary: Whether the document is temporary. If True, the document will be deleted when the Document object is destroyed.
    :type is_temporary: bool
    :param mode: The mode in which the file should be opened. Defaults to 'a' (append mode).
    :type mode: str
    """

    def __init__(self, file_name: str, is_temporary=False, mode='a'):
        self.page_margin = 10
        self.is_temporary = is_temporary
        self.file_name = file_name
        self.load(mode)

    def load(self, mode='a'):
        """
        Loads the JASON document file.

        :param mode: The mode in which the file should be opened. Defaults to 'a' (append mode).
        :type mode: str
        """
        is_new_file = not os.path.isfile(self.file_name)
        self.h5_file = h5py.File(self.file_name, mode)

        if mode != 'r':
            # Create the document structure if it doesn't exist
            doc_group = self.h5_file.require_group('JasonDocument') 
            doc_group.require_group('NMR')
            doc_group.require_group('General')
            doc_group.require_group('Molecules')
            if is_new_file:
                self.h5_file.attrs['Version.Major'] = np.uint8(2)
                self.h5_file.attrs['Version.Minor'] = np.uint32(1994)
                doc_group.attrs['DPI'] = np.double(120.0)
                doc_group.attrs['HPages'] = np.int32(2)
                doc_group.attrs['VPages'] = np.int32(2)
                doc_group.attrs['Orientation'] = np.int32(1)
                doc_group.attrs['Units'] = np.int32(1)
                doc_group.attrs['Margins'] = np.array([0.0, 0.0, 0.0, 0.0], np.double)
                doc_group.attrs['PageSize'] = np.array([595, 842], np.int32)

    @property
    def items(self) -> list[graphics.GraphicsItem]:
        """
        :return: A list of all graphics items in the document.
        :rtype: :obj:`list` of :obj:`graphics.GraphicsItem`
        """
        return [graphics.GraphicsItemFactory.create(elem) for elem in utils.group_to_list(self.h5_file, '/JasonDocument/Items')]

    @property
    def nmr_data(self) -> Iterable[data.NMRSpectrum]:
        """
        :return: A list of all NMR data objects in the document.
        :rtype: :obj:`Iterable` of :obj:`NMRSpectrum`
        """
        return data.NMRSpectrum.List(self.h5_file['/JasonDocument/NMR'])

    @property
    def text_data(self) -> Iterable[data.Text]:
        """
        :return: A list of all text data objects in the document.
        :rtype: :obj:`Iterable` of :obj:`data.Text`
        """
        return data.Text.List(self.h5_file['/JasonDocument/General']) if '/JasonDocument/General' in self.h5_file else []

    @property
    def image_data(self) -> Iterable[data.Image]:
        """
        :return: A list of all image data objects in the document.
        :rtype: :obj:`Iterable` of :obj:`data.Image`
        """
        return data.Image.List(self.h5_file['/JasonDocument/General']) if '/JasonDocument/General' in self.h5_file else []

    @property
    def nmr_items(self) -> list[graphics.NMRSpectrumGraphicsItem]:
        """
        :return: A list of all NMR spectrum graphics items in the document.
        :rtype: :obj:`list` of :obj:`graphics.NMRSpectrumGraphicsItem`
        """
        return list(filter(lambda item: item.type == graphics.GraphicsItem.Type.NMRSpectrum, self.items))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.remove()

    def __del__(self):
        self.remove()

    def close(self):
        """
        Closes the document file.
        """
        if os.path.isfile(self.file_name):
            self.h5_file.close()

    def remove(self):
        """
        Closes and removes the document file if it's marked as temporary.
        """
        self.close()
        if self.is_temporary and os.path.isfile(self.file_name):
            os.remove(self.file_name)

    def copy(self, file_name: str | bytes):
        """
        Copies the JASON document to a new file.

        .. note:: 
            Starting from h5py v3.4, it's essential to close the h5py.File object before using the 'copy' method. 
            This constraint diminishes the utility of the 'copy' method. Intentionally, the `self.close()` line 
            is omitted in this method, delegating the responsibility of calling 'close' to the programmer.

        :param file_name: The destination file name.
        :type file_name: str | bytes
        """
        shutil.copyfile(self.file_name, file_name)

    def _create_item_elem(self, item_type):
        items_group = self.h5_file.require_group('/JasonDocument/Items')
        items_group.attrs['.container_type'] = 9
        items_len = len(self.items)
        item_elem = items_group.create_group(str(items_len))
        item_elem.attrs['Geometry'] = (0.0, 0.0, 0.0, 0.0)
        item_elem.attrs['Pos'] = (0.0, 0.0)
        item_elem.attrs['TransformOrigPoint'] = (0.0, 0.0)
        item_elem.attrs['Rotation'] = 0.0
        item_elem.attrs['ZValue'] = 0.0
        item_elem.attrs['ID'] = utils.create_uuid()
        item_elem.attrs['Type'] = int(item_type)

        return item_elem

    def create_nmrpeaks_table(self, spec_item: graphics.NMRSpectrumGraphicsItem, spec_data: data.NMRSpectrum) -> graphics.NMRPeakTableGraphicsItem:
        """
        Creates a new NMR peaks table in the document.

        :param spec_item: The spectrum graphics item to which the table is linked.
        :type spec_item: :obj:`NMRSpectrumGraphicsItem`
        :param spec_data: The NMR spectrum data for the table.
        :type spec_data: :obj:`data.NMRSpectrum`

        :return: The created NMR peaks table graphics item.
        :rtype: :obj:`graphics.NMRPeakTableGraphicsItem`
        """
        item_elem = self._create_item_elem(graphics.GraphicsItem.Type.NMRPeakTable)
        item: graphics.NMRPeakTableGraphicsItem = self.items[-1]
        item.set_defaults()

        item.linked_ids += [spec_item.id]
        spec_item.linked_ids += [item.id]

        peaks_table = item_elem.create_group('PeaksTable')
        peaks_table.attrs['SpectrumID'] = spec_data.id

        return item

    def create_nmrmultiplets_table(self, spec_item: graphics.NMRSpectrumGraphicsItem, spec_data: data.NMRSpectrum) -> graphics.NMRMultipletTableGraphicsItem:
        """
        Creates a new NMR multiplets table in the document.

        :param spec_item: The spectrum graphics item to which the table is linked.
        :type spec_item: :obj:`NMRSpectrumGraphicsItem`
        :param spec_data: The NMR spectrum data for the table.
        :type spec_data: :obj:`data.NMRSpectrum`

        :return: The created NMR multiplets table graphics item.
        :rtype: :obj:`graphics.NMRMultipletTableGraphicsItem`
        """
        item_elem = self._create_item_elem(graphics.GraphicsItem.Type.NMRMultipletTable)
        item: graphics.NMRMultipletTableGraphicsItem = self.items[-1]
        item.set_defaults()

        item.linked_ids += [spec_item.id]
        spec_item.linked_ids += [item.id]

        multiplets_table = item_elem.create_group('MultipletsTable')
        multiplets_table.attrs['SpectrumID'] = spec_data.id

        return item

    def create_nmrmultiplet_report(self, spec_item: graphics.NMRSpectrumGraphicsItem, spec_data: data.NMRSpectrum) -> graphics.NMRMultipletReportGraphicsItem:
        """
        Creates a new NMR multiplet report in the document.

        :param spec_item: The spectrum graphics item to which the report is linked.
        :type spec_item: :obj:`graphics.NMRSpectrumGraphicsItem`
        :param spec_data: The NMR spectrum data for the report.
        :type spec_data: :obj:`data.NMRSpectrum`

        :return: The created NMR multiplet report graphics item.
        :rtype: :obj:`graphics.NMRMultipletReportGraphicsItem`
        """
        item_elem = self._create_item_elem(graphics.GraphicsItem.Type.NMRMultipletReport)
        item: graphics.NMRMultipletReportGraphicsItem = self.items[-1]

        item.linked_ids += [spec_item.id]
        spec_item.linked_ids += [item.id]

        multiplets_report = item_elem.create_group('MultipletsReport')
        multiplets_report.attrs['SpectrumID'] = spec_data.id

        return item

    def create_nmrparams_table(self, spec_item: graphics.NMRSpectrumGraphicsItem, spec_data: data.NMRSpectrum) -> graphics.NMRParamTableGraphicsItem:
        """
        Creates a new NMR parameters table in the document.

        :param spec_item: The spectrum graphics item to which the table is linked.
        :type spec_item: :obj:`graphics.NMRSpectrumGraphicsItem`
        :param spec_data: The NMR spectrum data for the table.
        :type spec_data: :obj:`data.NMRSpectrum`

        :return: The created NMR parameters table graphics item.
        :rtype: :obj:`graphics.NMRParamTableGraphicsItem`
        """
        item_elem = self._create_item_elem(graphics.GraphicsItem.Type.NMRParamTable)
        item: graphics.NMRParamTableGraphicsItem = self.items[-1]
        item.set_defaults()

        item.linked_ids += [spec_item.id]
        spec_item.linked_ids += [item.id]
        
        params_table = item_elem.create_group('ParamsTable')
        params_table.create_group('list').attrs['.container_type'] = 9
        params_table.attrs['id'] = spec_data.id

        return item

    def create_text_item(self, html_str: str='') -> graphics.TextGraphicsItem:
        """
        Creates a new text item in the document.

        :param html_str: The HTML text to be added.
        :type html_str: :obj:`str`

        :return: The created text graphics item.
        :rtype: :obj:`graphics.TextGraphicsItem`
        """
        item_elem = self._create_item_elem(graphics.GraphicsItem.Type.Text)

        data_id = utils.create_uuid()
        item_elem.create_group('TextItem').attrs['TextID'] = data_id
        data_group = self.h5_file.require_group('/JasonDocument/General/TextDocuments')
        data_group.attrs['.container_type'] = 9
        data_elem = data_group.create_group(str(len(utils.group_to_list(data_group, ''))))
        data_elem.attrs['ID'] = data_id

        item: graphics.TextGraphicsItem = self.items[-1]
        item.text.html = html_str

        return item

    def create_image_item(self, data_id: str) -> graphics.ImageGraphicsItem:
        """
        Creates a new image item in the document.

        :param data_id: The ID of the image data object.
        :type data_id: :obj:`str`

        :return: The created image graphics item.
        :rtype: :obj:`graphics.ImageGraphicsItem`
        """
        item_elem = self._create_item_elem(graphics.GraphicsItem.Type.Image)

        image_draw = item_elem.create_group('ImageDraw')
        image_draw.attrs['ImageID'] = data_id
        image_draw.attrs['MaskColor'] = (0, 0, 0, 255, 0)

        return self.items[-1]

    def create_image_data(self, image_file: str) -> data.Image:
        """
        Creates a new image in the document.

        :param image_file: The path to the image file.
        :type image_file: :obj:`str`

        :return: The created image data object.
        :rtype: :obj:`Image`
        """

        data_id = utils.create_uuid()
        item_elem = self.create_image_item(data_id)

        data_group = self.h5_file.require_group('/JasonDocument/General/Pixmaps')
        data_group.attrs['.container_type'] = 9
        data_elem = data_group.create_group(str(len(utils.group_to_list(data_group, ''))))
        data_elem.attrs['ID'] = data_id

        with PILImage.open(image_file) as image:
            rgba_image = image.convert('RGBA')
            data = np.asarray(rgba_image)
            image_ds = data_elem.create_dataset('Pixmap', data=data)
            image_ds.attrs['CLASS'] = np.bytes_(b'IMAGE')
            image_ds.attrs['IMAGE_MINMAXRANGE'] = np.array([0, 255], np.uint8)
            image_ds.attrs['IMAGE_SUBCLASS'] = np.bytes_(b'IMAGE_TRUECOLOR')
            image_ds.attrs['IMAGE_VERSION'] = np.bytes_(b'1.2')
            image_ds.attrs['INTERLACE_MODE'] = np.bytes_(b'INTERLACE_PIXEL')

        return item_elem