import unittest
from wsit.main.pyx.xml.rpc.holders.ulong_holder_editor import ULongHolderEditor
from wsit.main.pyx.xml.rpc.holders.ulong_holder import ULongHolder
from wsit.test.pyx.xml.rpc.holders.ulong_holder_test import TestULongHolder


class TestULongHolderEditor(unittest.TestCase):

    def test_init(self):
        ulong_holder_editor = ULongHolderEditor()
        self.assertTrue(ulong_holder_editor.get_value().get() == 0) 

    def test_private_field(self):
        ulong_holder_editor = ULongHolderEditor()
        with self.assertRaises(AttributeError):
            ulong_holder_editor.value = 123

    def test_set_value(self):
        ulong_holder_editor = ULongHolderEditor()
        for tested_value in TestULongHolder.valid_values:
            ulong_holder = ULongHolder(tested_value)
            ulong_holder_editor.set_value(ulong_holder)
            self.assertTrue(ulong_holder.get() == ulong_holder_editor.get_value().get()) 

    def test_set_value_exception(self):
        ulong_holder_editor = ULongHolderEditor()
        # Only ULongHolder type allowed
        for tested_value in TestULongHolder.exception_values + TestULongHolder.valid_values:
            with self.assertRaises(TypeError):
                ulong_holder_editor.set_value(tested_value)

    def test_set_as_text(self):
        ulong_holder_editor = ULongHolderEditor()
        for tested_value in TestULongHolder.valid_values:
            ulong_holder_editor.set_as_text(tested_value.__str__())
            self.assertTrue(ulong_holder_editor.get_as_text().__eq__(tested_value.__str__())) 

    def test_set_as_text_exception(self):
        ulong_holder_editor = ULongHolderEditor()
        for tested_value in TestULongHolder.exception_text_values:
            with self.assertRaises(Exception):
                ulong_holder_editor.set_as_text(tested_value)
