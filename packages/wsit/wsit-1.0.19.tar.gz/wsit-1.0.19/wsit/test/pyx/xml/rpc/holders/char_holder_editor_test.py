import unittest

from wsit.main.pyx.xml.rpc.holders.char_holder import CharHolder
from wsit.main.pyx.xml.rpc.holders.char_holder_editor import CharHolderEditor
from wsit.test.pyx.xml.rpc.holders.char_holder_test import TestCharHolder

class TestCharHolderEditor(unittest.TestCase):
    def test_init(self):
        char_holder_editor = CharHolderEditor()
        self.assertTrue(char_holder_editor.get_value().get() == '\0') 

    def test_private_field(self):
        char_holder_editor = CharHolderEditor()
        with self.assertRaises(AttributeError):
            char_holder_editor.value = 123

    def test_set_value(self):
        char_holder_editor = CharHolderEditor()
        for tested_value in TestCharHolder.valid_values:
            char_holder = CharHolder(tested_value)
            char_holder_editor.set_value(char_holder)
            self.assertTrue(tested_value == char_holder_editor.get_value().get()) 

    def test_set_value_exception(self):
        char_holder_editor = CharHolderEditor()
        for tested_value in TestCharHolder.exception_values:
            with self.assertRaises(Exception):
                char_holder_editor.set_value(tested_value)

    def test_set_as_text(self):
        char_holder_editor = CharHolderEditor()
        for tested_value in TestCharHolder.valid_text_values + TestCharHolder.valid_values:
            char_holder_editor.set_as_text(tested_value)
            self.assertTrue(tested_value[0] == char_holder_editor.get_as_text()) 

    def test_set_as_text_exception(self):
        char_holder_editor = CharHolderEditor()
        for tested_value in TestCharHolder.exception_text_values:
            with self.assertRaises(Exception):
                char_holder_editor.set_as_text(tested_value)

if __name__ == '__main__':
    unittest.main()
