import unittest
from wsit.main.pyx.xml.rpc.holders.short_holder_editor import ShortHolderEditor
from wsit.main.pyx.xml.rpc.holders.short_holder import ShortHolder
from wsit.test.pyx.xml.rpc.holders.short_holder_test import TestShortHolder


class TestShortHolderEditor(unittest.TestCase):

    def test_init(self):
        short_holder_editor = ShortHolderEditor()
        self.assertTrue(short_holder_editor.get_value().get() == 0) 

    def test_private_field(self):
        short_holder_editor = ShortHolderEditor()
        with self.assertRaises(AttributeError):
            short_holder_editor.value = 123

    def test_set_value(self):
        short_holder_editor = ShortHolderEditor()
        for tested_value in TestShortHolder.valid_values:
            short_holder = ShortHolder(tested_value)
            short_holder_editor.set_value(short_holder)
            self.assertTrue(short_holder.get() == short_holder_editor.get_value().get()) 

    def test_set_value_exception(self):
        short_holder_editor = ShortHolderEditor()
        for tested_value in TestShortHolder.exception_values:
            with self.assertRaises(Exception):
                short_holder_editor.set_value(tested_value)

    def test_set_as_text(self):
        short_holder_editor = ShortHolderEditor()
        for tested_value in TestShortHolder.valid_values:
            short_holder_editor.set_as_text(str(tested_value))
            self.assertTrue(short_holder_editor.get_as_text().__eq__(tested_value.__str__())) 

    def test_set_as_text_exception(self):
        short_holder_editor = ShortHolderEditor()
        for tested_value in TestShortHolder.exception_text_values:
            with self.assertRaises(Exception):
                short_holder_editor.set_as_text(tested_value)
