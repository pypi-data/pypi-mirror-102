import unittest

from wsit.main.com.vsi.wsi.wsi_acms_context import WsiAcmsContext
from wsit.main.com.vsi.wsi.wsi_acms_context_editor import WsiAcmsContextEditor
from wsit.test.com.vsi.wsi.wsi_acms_context_test import TestWsiAcmsContext

class TestWsiAcmsContextEditor(unittest.TestCase):

    def test_init(self):
        wsi_acms_context_editor = WsiAcmsContextEditor()
        self.assertTrue(wsi_acms_context_editor.get_value().get_sel_string() is None) 
        self.assertTrue(wsi_acms_context_editor.get_value().get_ext_status() is None) 
        self.assertTrue(wsi_acms_context_editor.get_value().get_app_name() is None) 

    def test_private_field(self):
        wsi_acms_context_editor = WsiAcmsContextEditor()
        with self.assertRaises(AttributeError):
            wsi_acms_context_editor.value = 123

    def test_set_value(self):
        wsi_acms_context_editor = WsiAcmsContextEditor()
        for tested_value in TestWsiAcmsContext.valid_values:
            wsi_acms_context = WsiAcmsContext.init_by_sel_str(tested_value)
            wsi_acms_context_editor.set_value(wsi_acms_context)
            self.assertTrue(wsi_acms_context_editor.get_value().get_sel_string().__eq__(tested_value)) 

    def test_set_value_exception(self):
        wsi_acms_context_editor = WsiAcmsContextEditor()
        # Only WsiAcmsContext type is allowed
        for tested_value in TestWsiAcmsContext.exception_values + TestWsiAcmsContext.valid_values:
            with self.assertRaises(Exception):
                wsi_acms_context_editor.set_value(tested_value)

    def test_set_as_text(self):
        wsi_acms_context_editor = WsiAcmsContextEditor()
        wsi_acms_context_editor.set_as_text(WsiAcmsContextEditor.null)
        self.assertTrue(wsi_acms_context_editor.get_value().get_sel_string() is None) 
        self.assertTrue(wsi_acms_context_editor.get_value().get_ext_status() is None) 
        self.assertTrue(wsi_acms_context_editor.get_value().get_app_name() is None) 

    def test_set_as_text_exception(self):
        wsi_acms_context_editor = WsiAcmsContextEditor()
        for tested_value in TestWsiAcmsContext.exception_text_values:
            with self.assertRaises(Exception):
                wsi_acms_context_editor.set_value(tested_value)

if __name__ == '__main__':
    unittest.main()
