import unittest
from wsit.main.pyx.xml.rpc.holders.ubyte_holder_editor import UByteHolderEditor
from wsit.main.pyx.xml.rpc.holders.ubyte_holder import UByteHolder
from wsit.test.pyx.xml.rpc.holders.ubyte_holder_test import TestUByteHolder


class TestUByteHolderEditor(unittest.TestCase):

    def test_init(self):
        ubyte_holder_editor = UByteHolderEditor()
        self.assertTrue(ubyte_holder_editor.get_value().get() == 0) 

    def test_private_field(self):
        ubyte_holder_editor = UByteHolderEditor()
        with self.assertRaises(AttributeError):
            ubyte_holder_editor.value = 123

    def test_set_value(self):
        ubyte_holder_editor = UByteHolderEditor()
        for tested_value in TestUByteHolder.valid_values:
            ubyte_holder = UByteHolder(tested_value)
            ubyte_holder_editor.set_value(ubyte_holder)
            self.assertTrue(ubyte_holder.get() == ubyte_holder_editor.get_value().get()) 

    def test_set_value_exception(self):
        ubyte_holder_editor = UByteHolderEditor()
        for tested_value in TestUByteHolder.exception_values:
            with self.assertRaises(Exception):
                ubyte_holder_editor.set_value(tested_value)

    def test_set_as_text(self):
        ubyte_holder_editor = UByteHolderEditor()
        for tested_value in TestUByteHolder.valid_values:
            ubyte_holder_editor.set_as_text(str(tested_value))
            self.assertTrue(ubyte_holder_editor.get_as_text().__eq__(tested_value.__str__())) 

    def test_set_as_text_exception(self):
        ubyte_holder_editor = UByteHolderEditor()
        for tested_value in TestUByteHolder.exception_text_values:
            with self.assertRaises(Exception):
                ubyte_holder_editor.set_as_text(tested_value)
