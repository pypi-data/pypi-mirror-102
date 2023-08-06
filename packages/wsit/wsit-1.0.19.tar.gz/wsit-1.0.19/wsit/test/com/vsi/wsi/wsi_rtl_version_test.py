import unittest

from wsit.main.com.vsi.wsi.wsi_rtl_version import WsiRtlVersion

class TestWsiRtlVersion(unittest.TestCase):
    def test_init(self):
        tested_value = "V1.1-8"
        self.assertTrue(WsiRtlVersion.get_version() == tested_value) 

    def test_private_field(self):
        wsi_rtl_version = WsiRtlVersion()
        with self.assertRaises(AttributeError):
            wsi_rtl_version.value = 123

if __name__ == '__main__':
    unittest.main()
