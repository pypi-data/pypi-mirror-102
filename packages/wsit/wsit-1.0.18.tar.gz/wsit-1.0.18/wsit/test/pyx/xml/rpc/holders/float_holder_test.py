import unittest
import math

from wsit.main.pyx.xml.rpc.holders.float_holder import FloatHolder

class TestFloatHolder(unittest.TestCase):

    exception_values = ["value", 'string', 'a', "b", '', "", True, False, "True", "False", "0", "1", '0', '1',
                        '124.9090798', '-0.126155', "-803485.9457897", "4564690846908.4059680458960", "485739857",
                        "-4573875937", None, "None", 'None']

    exception_text_values = ["value", 'string', 'a', "b", '', "", True, False, "True", "False", None, "None", 'None']

    valid_values = [
        1.175494e-38,
        3.402823e38,
        0.0,
        1.4e-45,
        3.4028235e38,
        16777216,
        -16777216,
        0,
        1,
        -389475,
        -1.4e-45,
        -3.4028235e38,
        -0,
        -1
    ]

    def test_init(self):
        float_holder = FloatHolder()
        self.assertTrue(math.isclose(float_holder.get(), 0.0)) 

    def test_private_field(self):
        float_holder = FloatHolder()
        with self.assertRaises(AttributeError):
            float_holder.value = 123

    def test_init_param(self):
        for tested_value in TestFloatHolder.valid_values:
            float_holder = FloatHolder(tested_value)
            self.assertTrue(math.isclose(float_holder.get(), tested_value)) 

    def test_init_param_exception(self):
        for tested_value in TestFloatHolder.exception_values:
            with self.assertRaises(Exception):
                float_holder = FloatHolder(tested_value)

    def test_to_string(self):
        for tested_value in TestFloatHolder.valid_values:
            float_holder = FloatHolder(tested_value)
            self.assertTrue(float_holder.__str__().__eq__(float(tested_value).__str__())) 

    def test_equals(self):
        float_holder_1 = FloatHolder()
        float_holder_2 = FloatHolder()
        self.assertTrue(float_holder_1.__eq__(None) is False) 
        self.assertTrue(float_holder_1.__eq__(int("123")) is False) 
        self.assertTrue(float_holder_1.__eq__(float_holder_1) is True) 
        self.assertTrue(float_holder_1.__eq__(float_holder_2) is True) 
        float_holder_2.set(123456.12)
        self.assertTrue(float_holder_1.__eq__(float_holder_2) is False) 
