import unittest

from wsit.main.com.vsi.wsi.wsi_exception import WsiException
from wsit.main.com.vsi.wsi.wsi_server_exception import WsiServerException
from wsit.test.com.vsi.wsi.wsi_exception_test import TestWsiException

class TestWsiServerException(unittest.TestCase):
    def test_init(self):
        wsi_server_exception = WsiServerException()
        self.assertTrue(wsi_server_exception.get_status() == 0) 
        self.assertTrue(wsi_server_exception.get_facility() == 0) 
        self.assertTrue(wsi_server_exception.get_vms_status() == 0) 
        self.assertTrue(wsi_server_exception.get_severity() == 0) 

        self.assertTrue(wsi_server_exception.WSIsK_WARNING == 0) 
        self.assertTrue(wsi_server_exception.WSIsK_SUCCESS == 1) 
        self.assertTrue(wsi_server_exception.WSIsK_ERROR == 2) 
        self.assertTrue(wsi_server_exception.WSIsK_INFO == 3) 
        self.assertTrue(wsi_server_exception.WSIsK_SEVERE == 4) 
        self.assertTrue(wsi_server_exception.WSIsK_FAC_IPC == 1) 
        self.assertTrue(wsi_server_exception.WSIsK_FAC_RTL == 2) 
        self.assertTrue(wsi_server_exception.WSIsK_FAC_MGR == 3) 
        self.assertTrue(wsi_server_exception.WSIsK_FAC_SVR == 4) 

        self.assertTrue(isinstance(wsi_server_exception, WsiException) is True) 

    def test_init_from_er_msg(self):
        for str_value in TestWsiException.str_valid_values:
            wsi_server_exception = WsiServerException.init_from_er_msg(str_value)
            self.assertTrue(wsi_server_exception.get_message().__eq__(str_value)) 
            self.assertTrue(wsi_server_exception.get_status() == 0) 
            self.assertTrue(wsi_server_exception.get_facility() == 0) 
            self.assertTrue(wsi_server_exception.get_vms_status() == 0) 
            self.assertTrue(wsi_server_exception.get_severity() == 0) 

    def test_init_from_er_msg_ex_code_vms_code(self):
        for str_value in TestWsiException.str_valid_values:
            for int_value in TestWsiException.int_valid_values:
                wsi_server_exception = WsiServerException.init_from_er_msg_ex_code_vms_code(str_value, int_value,
                                                                                            int_value)
                self.assertTrue(str_value.__eq__(wsi_server_exception.get_message())) 
                self.assertTrue(int_value == wsi_server_exception.get_status()) 
                self.assertTrue(int_value == wsi_server_exception.get_vms_status()) 

    def test_init_from_er_msg_ex_code_vms_code_severity_facility(self):
        for str_value in TestWsiException.str_valid_values:
            for int_value in TestWsiException.int_valid_values:
                for facility_value in TestWsiException.facility_values:
                    for severity_value in TestWsiException.severity_values:
                        wsi_server_exception = WsiServerException.init_from_er_msg_ex_code_vms_code_severity_facility(
                            str_value,
                            int_value, int_value,
                            severity_value,
                            facility_value)
                        self.assertTrue(str_value.__eq__(wsi_server_exception.get_message())) 
                        self.assertTrue(int_value == wsi_server_exception.get_status()) 
                        self.assertTrue(int_value == wsi_server_exception.get_vms_status()) 
                        self.assertTrue(severity_value == wsi_server_exception.get_severity()) 
                        self.assertTrue(facility_value == wsi_server_exception.get_facility()) 

    def test_private_field(self):
        wsi_server_exception = WsiServerException()
        with self.assertRaises(AttributeError):
            wsi_server_exception.value = 123

if __name__ == '__main__':
    unittest.main()
