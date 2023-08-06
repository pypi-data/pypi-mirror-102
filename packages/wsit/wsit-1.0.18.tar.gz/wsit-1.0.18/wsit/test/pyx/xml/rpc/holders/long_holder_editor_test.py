import unittest
from wsit.main.pyx.xml.rpc.holders.long_holder_editor import LongHolderEditor
from wsit.main.pyx.xml.rpc.holders.long_holder import LongHolder
from wsit.test.pyx.xml.rpc.holders.long_holder_test import TestLongHolder


class TestLongHolderEditor(unittest.TestCase):

    def test_init(self):
        long_holder_editor = LongHolderEditor()
        self.assertTrue(long_holder_editor.get_value().get() == 0) 

    def test_private_field(self):
        long_holder_editor = LongHolderEditor()
        with self.assertRaises(AttributeError):
            long_holder_editor.value = 123

    def test_set_value(self):
        long_holder_editor = LongHolderEditor()
        for tested_value in TestLongHolder.valid_values:
            long_holder = LongHolder(tested_value)
            long_holder_editor.set_value(long_holder)
            self.assertTrue(long_holder.get() == long_holder_editor.get_value().get()) 

    def test_set_value_exception(self):
        long_holder_editor = LongHolderEditor()
        # Only LongHolder type allowed
        for tested_value in TestLongHolder.exception_values + TestLongHolder.valid_values:
            with self.assertRaises(TypeError):
                long_holder_editor.set_value(tested_value)

    def test_set_as_text(self):
        long_holder_editor = LongHolderEditor()
        for tested_value in TestLongHolder.valid_values:
            long_holder_editor.set_as_text(tested_value.__str__())
            self.assertTrue(long_holder_editor.get_as_text().__eq__(tested_value.__str__())) 

    def test_set_as_text_exception(self):
        long_holder_editor = LongHolderEditor()
        for tested_value in TestLongHolder.exception_text_values:
            with self.assertRaises(Exception):
                long_holder_editor.set_as_text(tested_value)
