import unittest

from wsit.main.pyx.xml.rpc.holders.int_holder import IntHolder
from wsit.main.pyx.xml.rpc.holders.object_holder import ObjectHolder


class TestObjectHolder(unittest.TestCase):
    valid_values = ["value", 'string', 'a', "b", '', "", True, False, "True", "False", "0", "1", '0', '1', 234.890,
                    -7389457908.39485797, '124.9090798', '-0.126155', "-803485.9457897", "4564690846908.4059680458960",
                    "485739857", "-4573875937", None, "None", 'None', IntHolder()]

    def test_init(self):
        object_holder = ObjectHolder()
        self.assertTrue(object_holder.get() is None) 

    def test_init_param(self):
        for tested_value in TestObjectHolder.valid_values:
            object_holder = ObjectHolder(tested_value)
            self.assertTrue(object_holder.get() == tested_value) 

    def test_private_field(self):
        object_holder = ObjectHolder()
        with self.assertRaises(AttributeError):
            object_holder.value = 123

    def test_to_string(self):
        for tested_value in TestObjectHolder.valid_values:
            object_holder = ObjectHolder(tested_value)
            self.assertTrue(str(tested_value).__eq__(object_holder.__str__())) 

    def test_equals(self):
        tested_value = -117
        object_holder_1 = ObjectHolder(tested_value)
        object_holder_2 = ObjectHolder(tested_value)
        object_holder_3 = ObjectHolder(4)

        self.assertTrue(object_holder_1.__eq__(None) is False) 
        self.assertTrue(object_holder_1.__eq__(tested_value) is False) 
        self.assertTrue(object_holder_1.__eq__(object_holder_1) is True) 
        self.assertTrue(object_holder_1.__eq__(object_holder_2) is True) 
        self.assertTrue(object_holder_1.__eq__(object_holder_3) is False) 
