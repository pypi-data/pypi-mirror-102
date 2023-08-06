import unittest

from wsit.main.com.vsi.wsi.no_server_exception import NoServerException
from wsit.main.com.vsi.wsi.wsi_exception import WsiException
from wsit.test.com.vsi.wsi.wsi_exception_test import TestWsiException


class TestNoServerException(unittest.TestCase):
    def test_init(self):
        no_server_exception = NoServerException()
        self.assertTrue(no_server_exception.get_status() == 0) 
        self.assertTrue(no_server_exception.get_facility() == 0) 
        self.assertTrue(no_server_exception.get_vms_status() == 0) 
        self.assertTrue(no_server_exception.get_severity() == 0) 

        self.assertTrue(no_server_exception.WSIsK_WARNING == 0) 
        self.assertTrue(no_server_exception.WSIsK_SUCCESS == 1) 
        self.assertTrue(no_server_exception.WSIsK_ERROR == 2) 
        self.assertTrue(no_server_exception.WSIsK_INFO == 3) 
        self.assertTrue(no_server_exception.WSIsK_SEVERE == 4) 
        self.assertTrue(no_server_exception.WSIsK_FAC_IPC == 1) 
        self.assertTrue(no_server_exception.WSIsK_FAC_RTL == 2) 
        self.assertTrue(no_server_exception.WSIsK_FAC_MGR == 3) 
        self.assertTrue(no_server_exception.WSIsK_FAC_SVR == 4) 

    def test_init_from_er_msg(self):
        for str_value in TestWsiException.str_valid_values:
            no_server_exception = NoServerException.init_from_er_msg(str_value)
            self.assertTrue(no_server_exception.get_message().__eq__(str_value)) 
            self.assertTrue(no_server_exception.get_status() == 0) 
            self.assertTrue(no_server_exception.get_facility() == 0) 
            self.assertTrue(no_server_exception.get_vms_status() == 0) 
            self.assertTrue(no_server_exception.get_severity() == 0) 
            self.assertTrue(isinstance(no_server_exception, WsiException) is True) 

    def test_private_field(self):
        no_server_exception = NoServerException()
        with self.assertRaises(AttributeError):
            no_server_exception.value = 123

if __name__ == '__main__':
    unittest.main()
