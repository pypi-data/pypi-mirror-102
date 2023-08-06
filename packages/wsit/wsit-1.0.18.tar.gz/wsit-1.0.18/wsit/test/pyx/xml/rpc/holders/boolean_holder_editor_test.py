import unittest
from wsit.main.pyx.xml.rpc.holders.boolean_holder_editor import BooleanHolderEditor
from wsit.main.pyx.xml.rpc.holders.boolean_holder import BooleanHolder
from wsit.test.pyx.xml.rpc.holders.boolean_holder_test import TestBooleanHolder

class TestBooleanHolderEditor(unittest.TestCase):

    def test_init(self):
        boolean_holder_editor = BooleanHolderEditor()
        boolean_holder = BooleanHolder()
        self.assertTrue(boolean_holder.get() == boolean_holder_editor.get_value().get()) 

    def test_private_field(self):
        boolean_holder_editor = BooleanHolderEditor()
        with self.assertRaises(AttributeError):
            boolean_holder_editor.value = 123

    def test_set_value(self):
        boolean_holder_editor = BooleanHolderEditor()
        for tested_value in TestBooleanHolder.valid_values:
            boolean_holder = BooleanHolder(tested_value)
            boolean_holder_editor.set_value(boolean_holder)
            self.assertTrue(boolean_holder.get() == boolean_holder_editor.get_value().get()) 

    def test_set_value_exception(self):
        boolean_holder_editor = BooleanHolderEditor()
        for tested_value in TestBooleanHolder.exception_values:
            with self.assertRaises(Exception):
                boolean_holder_editor.set_value(tested_value)

    def test_set_as_text(self):
        boolean_holder_editor = BooleanHolderEditor()
        for tested_value in TestBooleanHolder.valid_text_values:
            boolean_holder_editor.set_as_text(tested_value)
            self.assertTrue(tested_value.lower().__eq__(boolean_holder_editor.get_as_text().lower())) 

    def test_set_as_text_exception(self):
        boolean_holder_editor = BooleanHolderEditor()
        for tested_value in TestBooleanHolder.exception_text_values:
            with self.assertRaises(Exception):
                boolean_holder_editor.set_as_text(tested_value)

if __name__ == '__main__':
    unittest.main()
