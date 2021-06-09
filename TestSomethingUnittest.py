import unittest

from main import find_client_by_doc, find_shelf_by_doc, give_all_docs_list, add_new_doc, del_doc,\
    documents, directories


class TestAccountingUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    def setUp(self):
        self.DATA_DOCS_INPUT = ['2207 876123', '11-2', '10006', '']
        self.DATA_DOCS_INPUT_SET2 = ['1234 567890', 'passport', 'Иван Крузенштерн', '3']
        self.DATA_DOCS_INPUT_SET3 = [{'type': 'passport', 'number': '2207 876123', 'name': 'Василий Гупкин'},
                                     {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
                                     {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}]
        self.DATA_DOCS_INPUT_SET4 = {'1': ['2207 876123'], '2': ['11-2'], '3': ['10006']}

        self.DATA_EXPECT_OUTPUT_SET1 = ['Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов', '']
        self.DATA_EXPECT_OUTPUT_SET2 = ['passport', '2207 876123', 'Василий Гупкин', 'invoice', '11-2',
                                        'Геннадий Покемонов', 'insurance', '10006', 'Аристарх Павлов']
        self.DATA_EXPECT_OUTPUT_SET3 = [{'type': 'passport', 'number': '2207 876123', 'name': 'Василий Гупкин'},
                                        {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
                                        {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
                                        {'type': 'passport', 'number': '1234 567890', 'name': 'Иван Крузенштерн'}]
        self.DATA_EXPECT_OUTPUT_SET4 = ['passport', '2207 876123', 'Василий Гупкин', 'invoice', '11-2',
                                        'Геннадий Покемонов']
        self.DATA_EXPECT_OUTPUT_SET5 = [{'type': 'passport', 'number': '2207 876123', 'name': 'Василий Гупкин'},
                                        {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'}]
        self.DATA_EXPECT_OUTPUT_SET6 = {'1': ['2207 876123'], '2': ['11-2'], '3': []}
        print("method setUp")

    def test_find_client_by_doc_true(self):
        self.assertEqual(find_client_by_doc(self.DATA_DOCS_INPUT_SET3, self.DATA_DOCS_INPUT[0]),
                         self.DATA_EXPECT_OUTPUT_SET1[0])
        self.assertEqual(find_client_by_doc(self.DATA_DOCS_INPUT_SET3, self.DATA_DOCS_INPUT[1]),
                         self.DATA_EXPECT_OUTPUT_SET1[1])
        self.assertEqual(find_client_by_doc(self.DATA_DOCS_INPUT_SET3, self.DATA_DOCS_INPUT[2]),
                         self.DATA_EXPECT_OUTPUT_SET1[2])

    def test_find_client_by_doc_false(self):
        self.assertEqual(find_client_by_doc(self.DATA_DOCS_INPUT_SET3, self.DATA_DOCS_INPUT[3]),
                         self.DATA_EXPECT_OUTPUT_SET1[3])

    def test_find_shelf_by_doc_true(self):
        self.assertEqual(find_shelf_by_doc(self.DATA_DOCS_INPUT_SET4, self.DATA_DOCS_INPUT[0]), '1')
        self.assertEqual(find_shelf_by_doc(self.DATA_DOCS_INPUT_SET4, self.DATA_DOCS_INPUT[1]), '2')
        self.assertEqual(find_shelf_by_doc(self.DATA_DOCS_INPUT_SET4, self.DATA_DOCS_INPUT[2]), '3')

    def test_find_shelf_by_doc_false(self):
        self.assertEqual(find_shelf_by_doc(self.DATA_DOCS_INPUT_SET4, self.DATA_DOCS_INPUT[3]),
                         self.DATA_EXPECT_OUTPUT_SET1[3])

    def test_give_all_docs_list_true(self):
        self.assertEqual(give_all_docs_list(self.DATA_DOCS_INPUT_SET3), self.DATA_EXPECT_OUTPUT_SET2)

    def test_add_new_doc_true(self):
        args = self.DATA_DOCS_INPUT_SET2
        self.assertEqual(add_new_doc(self.DATA_DOCS_INPUT_SET3, self.DATA_DOCS_INPUT_SET4, *args),
                         self.DATA_EXPECT_OUTPUT_SET3)

    def test_add_new_doc_false(self):
        args = self.DATA_DOCS_INPUT_SET2
        self.assertNotEqual(add_new_doc(self.DATA_DOCS_INPUT_SET3, self.DATA_DOCS_INPUT_SET4, *args),
                            self.DATA_EXPECT_OUTPUT_SET2)

    def test_del_doc_true(self):
        self.assertEqual(del_doc(documents, directories, self.DATA_DOCS_INPUT[2]),
                         (self.DATA_EXPECT_OUTPUT_SET5, self.DATA_EXPECT_OUTPUT_SET6))

    def test_del_doc_false(self):
        self.assertNotEqual(del_doc(documents, directories, self.DATA_DOCS_INPUT[2]),
                            (self.DATA_DOCS_INPUT_SET3, self.DATA_DOCS_INPUT_SET4))

    def tearDown(self):
        self.DATA_DOCS_INPUT.clear()
        self.DATA_DOCS_INPUT_SET2.clear()
        self.DATA_DOCS_INPUT_SET3.clear()
        self.DATA_DOCS_INPUT_SET4.clear()
        self.DATA_EXPECT_OUTPUT_SET1.clear()
        self.DATA_EXPECT_OUTPUT_SET2.clear()
        self.DATA_EXPECT_OUTPUT_SET3.clear()
        self.DATA_EXPECT_OUTPUT_SET4.clear()
        self.DATA_EXPECT_OUTPUT_SET5.clear()
        self.DATA_EXPECT_OUTPUT_SET6.clear()
        print("method tearDown")

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


if __name__ == '__main__':
    unittest.main()
