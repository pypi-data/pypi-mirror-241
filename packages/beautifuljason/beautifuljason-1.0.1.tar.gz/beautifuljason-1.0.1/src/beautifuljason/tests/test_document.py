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

import unittest
import os
import beautifuljason as bjason
from beautifuljason.tests.config import datafile_path, datafile_copy_path, newfile_path

class DocumentTestCase(unittest.TestCase):
    """Document class test cases"""

    @classmethod
    def setUpClass(cls):
        cls.jason = bjason.JASON()

    def test___init__(self):
        """Testing Document.__init__()"""

        # Existing documents
        with bjason.Document(datafile_copy_path('empty.jjh5')) as doc:
            self.assertTrue('JasonDocument' in doc.h5_file)
            self.assertEqual(len(doc.items), 0)
            doc.h5_file.create_group('TestGroup')
            self.assertTrue('TestGroup' in doc.h5_file)
        with self.jason.create_document(doc.file_name) as temp_doc:
            self.assertEqual(len(temp_doc.items), 0)

        with bjason.Document(datafile_copy_path('Ethylindanone_Proton-13-1.jjh5')) as doc:
            self.assertEqual(len(doc.items), 1)
            self.assertEqual(len(doc.nmr_items), 1)
        with self.jason.create_document(doc.file_name) as temp_doc:
            self.assertEqual(len(temp_doc.items), 1)

        # Existing document in read-only mode
        with bjason.Document(datafile_copy_path('empty.jjh5'), mode='r') as doc:
            self.assertTrue('JasonDocument' in doc.h5_file)
            self.assertEqual(len(doc.items), 0)
            with self.assertRaises(ValueError):
                doc.h5_file.create_group('TestGroup')
            self.assertFalse('TestGroup' in doc.h5_file)
        with self.jason.create_document(doc.file_name) as temp_doc:
            self.assertEqual(len(temp_doc.items), 0)

        # New document
        with bjason.Document(newfile_path('new_doc.jjh5')) as doc:
            self.assertTrue('JasonDocument' in doc.h5_file)
            self.assertEqual(len(doc.items), 0)
            doc.h5_file.create_group('TestGroup')
            self.assertTrue('TestGroup' in doc.h5_file)
        with self.jason.create_document(doc.file_name) as temp_doc:
            self.assertEqual(len(temp_doc.items), 0)

        # New temporary document
        with bjason.Document(newfile_path('new_temp_doc.jjh5'), is_temporary=True) as doc:
            self.assertTrue('JasonDocument' in doc.h5_file)
            self.assertEqual(len(doc.items), 0)
            doc.h5_file.create_group('TestGroup')
            self.assertTrue('TestGroup' in doc.h5_file)
            self.assertTrue(os.path.isfile(doc.file_name))
            doc_copy_name = newfile_path('copy_doc.jjh5')
            doc.close()
            doc.copy(doc_copy_name)
        self.assertTrue(len(doc.file_name) > 0)
        self.assertFalse(os.path.isfile(doc.file_name))
        with self.jason.create_document(doc_copy_name) as temp_doc:
            self.assertEqual(len(temp_doc.items), 0)

    def test_close(self):
        """Testing Document.close()"""

        # New document
        doc = bjason.Document(newfile_path('new_doc.jjh5'))
        self.assertTrue('JasonDocument' in doc.h5_file)
        doc.close()
        self.assertFalse('JasonDocument' in doc.h5_file)

        # New temporary document
        doc = bjason.Document(newfile_path('new_doc.jjh5'), is_temporary=True)
        self.assertTrue('JasonDocument' in doc.h5_file)
        doc.close()
        self.assertFalse('JasonDocument' in doc.h5_file)

    def test_remove(self):
        """Testing Document.remove()"""

        # New document
        doc = bjason.Document(newfile_path('new_doc.jjh5'))
        self.assertTrue(os.path.isfile(doc.file_name))
        doc.remove()
        self.assertTrue(os.path.isfile(doc.file_name))

        # New temporary document
        doc = bjason.Document(newfile_path('new_doc.jjh5'), is_temporary=True)
        self.assertTrue(os.path.isfile(doc.file_name))
        doc.remove()
        self.assertFalse(os.path.isfile(doc.file_name))

    def test_copy(self):
        """Testing Document.copy()"""

        orig_path = datafile_copy_path('empty.jjh5')
        with bjason.Document(orig_path) as doc:
            doc.h5_file.create_group('TestGroup')
            copy_path = newfile_path('copy.jjh5')
            doc.close()
            doc.copy(copy_path)
        with open(orig_path, 'rb') as orig_f, open(copy_path, 'rb') as copy_f:
            orig_b = orig_f.read()
            copy_b = copy_f.read()
            self.assertGreater(orig_b.find(b'TestGroup'), -1)
            self.assertEqual(orig_b, copy_b)

    def test_create_nmrpeaks_table(self):
        """Testing Document.create_nmrpeaks_table()"""

        with bjason.Document(datafile_copy_path('Ethylindanone_Proton-13-1.jjh5')) as doc:
            self.assertEqual(len(doc.items), 1)
            spec_item = doc.items[0]
            new_item1 = doc.create_nmrpeaks_table(spec_item, spec_item.spec_data(0))
            self.assertIsInstance(new_item1, bjason.NMRPeakTableGraphicsItem)
            self.assertEqual(len(doc.items), 2)
            self.assertEqual(len(new_item1.columns), 0)
            new_item2 = doc.create_nmrpeaks_table(spec_item, spec_item.spec_data(0))
            self.assertIsInstance(new_item2, bjason.NMRPeakTableGraphicsItem)
            self.assertEqual(len(doc.items), 3)
            self.assertEqual(len(new_item1.columns), 0)
        with self.jason.create_document(doc.file_name) as temp_doc:
            self.assertEqual(len(temp_doc.items), 3)

    def test_create_nmrmultiplets_table(self):
        """Testing Document.create_nmrintegrals_table()"""

        with bjason.Document(datafile_copy_path('Ethylindanone_Proton-13-1.jjh5')) as doc:
            self.assertEqual(len(doc.items), 1)
            spec_item = doc.items[0]
            new_item1 = doc.create_nmrmultiplets_table(spec_item, spec_item.spec_data(0))
            self.assertIsInstance(new_item1, bjason.NMRMultipletTableGraphicsItem)
            self.assertEqual(len(doc.items), 2)
            new_item2 = doc.create_nmrmultiplets_table(spec_item, spec_item.spec_data(0))
            self.assertIsInstance(new_item2, bjason.NMRMultipletTableGraphicsItem)
            self.assertEqual(len(doc.items), 3)
        with self.jason.create_document(doc.file_name) as temp_doc:
            self.assertEqual(len(temp_doc.items), 3)

    def test_create_nmrparams_table(self):
        """Testing Document.create_nmrparams_table()"""

        with bjason.Document(datafile_copy_path('Ethylindanone_Proton-13-1.jjh5')) as doc:
            self.assertEqual(len(doc.items), 1)
            spec_item = doc.items[0]
            new_item1 = doc.create_nmrparams_table(spec_item, spec_item.spec_data(0))
            self.assertIsInstance(new_item1, bjason.NMRParamTableGraphicsItem)
            self.assertEqual(len(doc.items), 2)
            new_item2 = doc.create_nmrparams_table(spec_item, spec_item.spec_data(0))
            self.assertIsInstance(new_item2, bjason.NMRParamTableGraphicsItem)
            self.assertEqual(len(doc.items), 3)
        with self.jason.create_document(doc.file_name) as temp_doc:
            self.assertEqual(len(temp_doc.items), 3)

    def test_create_nmrmultiplet_report(self):
        """Testing Document.create_nmrmultiplet_report()"""

        with bjason.Document(datafile_copy_path('Ethylindanone_Proton-13-1.jjh5')) as doc:
            self.assertEqual(len(doc.items), 1)
            spec_item = doc.items[0]
            new_item1 = doc.create_nmrmultiplet_report(spec_item, spec_item.spec_data(0))
            self.assertIsInstance(new_item1, bjason.NMRMultipletReportGraphicsItem)
            self.assertEqual(len(doc.items), 2)
            new_item2 = doc.create_nmrmultiplet_report(spec_item, spec_item.spec_data(0))
            self.assertIsInstance(new_item2, bjason.NMRMultipletReportGraphicsItem)
            self.assertEqual(len(doc.items), 3)
        with self.jason.create_document(doc.file_name) as temp_doc:
            self.assertEqual(len(temp_doc.items), 3)
            
    def test_create_text_item(self):
        """Testing Document.create_text()"""

        with bjason.Document(newfile_path('create_text.jjh5')) as doc:
            self.assertEqual(len(doc.items), 0)
            new_item1 = doc.create_text_item()
            self.assertEqual(doc.h5_file['/JasonDocument/Items'].attrs['.container_type'], 9)
            self.assertIsInstance(new_item1, bjason.TextGraphicsItem)
            self.assertEqual(len(doc.items), 1)
            new_item2 = doc.create_text_item('test text')
            self.assertEqual(new_item2.text.html, 'test text')
            self.assertIsInstance(new_item2, bjason.TextGraphicsItem)
            self.assertEqual(len(doc.items), 2)
        with self.jason.create_document(doc.file_name) as temp_doc:
            self.assertEqual(len(temp_doc.items), 2)

    def test_create_image_data(self):
        """Testing Document.create_image_data()"""

        with bjason.Document(newfile_path('create_image.jjh5')) as doc:
            self.assertEqual(len(doc.items), 0)
            try:
                new_item1 = doc.create_image_data(datafile_path('jason_logo.png'))
            except AssertionError:
                new_item1 = None
            else:
                self.assertIsInstance(new_item1, bjason.ImageGraphicsItem)
                self.assertEqual(new_item1.image.depth, 32)
                self.assertEqual(len(doc.items), 1)
                new_item2 = doc.create_image_data(datafile_path('jason_logo.png'))
                self.assertIsInstance(new_item2, bjason.ImageGraphicsItem)
                self.assertEqual(len(doc.items), 2)
        if new_item1:
            with self.jason.create_document(doc.file_name) as temp_doc:
                self.assertEqual(len(temp_doc.items), 2)
                self.assertEqual(len(temp_doc.image_data), 2)

    def test_create_image_item(self):
        """Testing Document.create_image_item()"""

        with bjason.Document(newfile_path('create_image_item.jjh5')) as doc:
            self.assertEqual(len(doc.items), 0)
            try:
                new_item1 = doc.create_image_data(datafile_path('jason_logo.png'))
            except AssertionError:
                new_item1 = None
            else:
                self.assertIsInstance(new_item1, bjason.ImageGraphicsItem)
                self.assertEqual(len(doc.items), 1)
                new_item2 = doc.create_image_item(new_item1.image_id)
                self.assertIsInstance(new_item2, bjason.ImageGraphicsItem)
                self.assertEqual(len(doc.items), 2)
                new_item3 = doc.create_image_item(new_item1.image_id)
                self.assertIsInstance(new_item3, bjason.ImageGraphicsItem)
                self.assertEqual(len(doc.items), 3)
        if new_item1:
            with self.jason.create_document(doc.file_name) as temp_doc:
                self.assertEqual(len(temp_doc.items), 3)
                self.assertEqual(len(temp_doc.image_data), 1)

if __name__ == '__main__':
    unittest.main()
