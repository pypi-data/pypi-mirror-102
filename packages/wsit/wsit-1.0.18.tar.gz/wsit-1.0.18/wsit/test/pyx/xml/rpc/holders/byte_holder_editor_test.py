import unittest
from wsit.main.pyx.xml.rpc.holders.byte_holder_editor import ByteHolderEditor
from wsit.main.pyx.xml.rpc.holders.byte_holder import ByteHolder
from wsit.test.pyx.xml.rpc.holders.byte_holder_test import TestByteHolder

class TestByteHolderEditor(unittest.TestCase):

    def test_init(self):
        byte_holder_editor = ByteHolderEditor()
        self.assertTrue(byte_holder_editor.get_value().get() == 0) 

    def test_private_field(self):
        byte_holder_editor = ByteHolderEditor()
        with self.assertRaises(AttributeError):
            byte_holder_editor.value = 123

    def test_set_value(self):
        byte_holder_editor = ByteHolderEditor()
        for tested_value in TestByteHolder.valid_values:
            byte_holder = ByteHolder(tested_value)
            byte_holder_editor.set_value(byte_holder)
            self.assertTrue(byte_holder.get() == byte_holder_editor.get_value().get()) 

    def test_set_value_exception(self):
        byte_holder_editor = ByteHolderEditor()
        for tested_value in TestByteHolder.exception_values:
            with self.assertRaises(Exception):
                byte_holder_editor.set_value(tested_value)

    def test_set_as_text(self):
        byte_holder_editor = ByteHolderEditor()
        for tested_value in TestByteHolder.valid_values:
            byte_holder_editor.set_as_text(str(tested_value))
            self.assertTrue(byte_holder_editor.get_as_text().__eq__(tested_value.__str__())) 

    def test_set_as_text_exception(self):
        byte_holder_editor = ByteHolderEditor()
        for tested_value in TestByteHolder.exception_text_values:
            with self.assertRaises(Exception):
                byte_holder_editor.set_as_text(tested_value)

if __name__ == '__main__':
    unittest.main()
