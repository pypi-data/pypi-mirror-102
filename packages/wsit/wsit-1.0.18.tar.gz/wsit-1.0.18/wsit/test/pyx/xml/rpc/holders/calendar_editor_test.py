import unittest
from wsit.main.pyx.xml.rpc.holders.calendar_editor import CalendarEditor
from wsit.test.pyx.xml.rpc.holders.calendar_holder_test import TestCalendarHolder

class TestCalendarEditor(unittest.TestCase):
    def test_init(self):
        calendar_editor = CalendarEditor()
        self.assertTrue(calendar_editor.get_value() is not None) 

    def test_private_field(self):
        calendar_editor = CalendarEditor()
        with self.assertRaises(AttributeError):
            calendar_editor.value = 123

    def test_set_value(self):
        calendar_editor = CalendarEditor()
        for tested_value in TestCalendarHolder.valid_values:
            calendar_editor.set_value(tested_value)
            self.assertTrue(tested_value == calendar_editor.get_value()) 

    def test_set_value_exception(self):
        calendar_editor = CalendarEditor()
        for tested_value in TestCalendarHolder.exception_values + TestCalendarHolder.exception_text_values:
            with self.assertRaises(Exception):
                calendar_editor.set_value(tested_value)

    def test_set_as_text(self):
        calendar_editor = CalendarEditor()
        for tested_value in TestCalendarHolder.valid_text_values:
            calendar_editor.set_as_text(tested_value)
            self.assertTrue(tested_value.__eq__(calendar_editor.get_as_text())) 

    def test_set_as_text_exception(self):
        calendar_editor = CalendarEditor()
        for tested_value in TestCalendarHolder.exception_values + TestCalendarHolder.exception_text_values:
            with self.assertRaises(Exception):
                calendar_editor.set_as_text(tested_value)

if __name__ == '__main__':
    unittest.main()
