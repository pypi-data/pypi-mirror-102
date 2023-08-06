import unittest

from wsit.main.com.vsi.wsi.big_decimal import BigDecimal
from wsit.main.pyx.xml.rpc.holders.big_decimal_holder import BigDecimalHolder
from wsit.main.pyx.xml.rpc.holders.big_decimal_holder_editor import BigDecimalHolderEditor
from wsit.test.pyx.xml.rpc.holders.big_decimal_holder_test import TestBigDecimalHolder

class TestDecimalHolderEditor(unittest.TestCase):
    def test_init(self):
        big_decimal_holder_editor = BigDecimalHolderEditor()
        dec_value = BigDecimal.init_from_str("0.0")
        big_decimal_holder = big_decimal_holder_editor.get_value()
        self.assertTrue(dec_value.__eq__(big_decimal_holder.get())) 

    def test_private_field(self):
        big_decimal_holder_editor = BigDecimalHolderEditor()
        with self.assertRaises(AttributeError):
            big_decimal_holder_editor.value = 123

    def test_set_value(self):
        big_decimal_holder_editor = BigDecimalHolderEditor()
        for tested_value in TestBigDecimalHolder.valid_values:
            dec_value = BigDecimal.init_from_str(tested_value)
            big_decimal_holder_editor.set_value(BigDecimalHolder(dec_value))
            big_decimal_holder = big_decimal_holder_editor.get_value()
            self.assertTrue(dec_value.__eq__(big_decimal_holder.get())) 

    def test_set_value_exception(self):
        big_decimal_holder = BigDecimalHolder()
        for tested_value in TestBigDecimalHolder.exception_values:
            with self.assertRaises(Exception):
                big_decimal_holder.set_value(tested_value)

    def test_set_as_text(self):
        big_decimal_holder_editor = BigDecimalHolderEditor()
        for tested_value in TestBigDecimalHolder.valid_values:
            big_decimal_holder_editor.set_as_text(str(tested_value))
            self.assertTrue(tested_value.__eq__(big_decimal_holder_editor.get_as_text())) 

    def test_set_as_text_exception(self):
        big_decimal_holder_editor = BigDecimalHolderEditor()
        for tested_value in TestBigDecimalHolder.exception_text_values:
            with self.assertRaises(Exception):
                big_decimal_holder_editor.set_as_text(tested_value)

if __name__ == '__main__':
    unittest.main()
