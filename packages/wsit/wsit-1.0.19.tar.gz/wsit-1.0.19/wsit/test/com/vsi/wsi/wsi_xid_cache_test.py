import unittest

from wsit.main.com.vsi.wsi.i_xid import IXid
from wsit.main.com.vsi.wsi.wsi_xid_cache import WsiXidCache

class TestWsiXidCache(unittest.TestCase):

    def test_init(self):
        wsi_xid_cache = WsiXidCache()
        self.assertTrue(wsi_xid_cache.is_empty() is True) 

    def test_add_if(self):
        wsi_xid_cache = WsiXidCache()
        ixid1 = IXid()
        ixid2 = IXid()
        self.assertTrue(wsi_xid_cache.has_xid(ixid1) is False) 
        self.assertTrue(wsi_xid_cache.has_xid(ixid2) is False) 
        self.assertTrue(wsi_xid_cache.is_empty() is True) 

        wsi_xid_cache.add_if(ixid1)
        wsi_xid_cache.add_if(ixid2)
        self.assertTrue(wsi_xid_cache.has_xid(ixid1) is True) 
        self.assertTrue(wsi_xid_cache.has_xid(ixid2) is True) 
        self.assertTrue(wsi_xid_cache.is_empty() is False) 

    def test_drop_if(self):
        wsi_xid_cache = WsiXidCache()
        ixid1 = IXid()
        ixid2 = IXid()
        self.assertTrue(wsi_xid_cache.is_empty() is True) 

        wsi_xid_cache.add_if(ixid1)
        wsi_xid_cache.add_if(ixid2)
        self.assertTrue(wsi_xid_cache.is_empty() is False) 
        self.assertTrue(wsi_xid_cache.has_xid(ixid1) is True) 
        self.assertTrue(wsi_xid_cache.has_xid(ixid2) is True) 

        wsi_xid_cache.drop_if(ixid1)
        self.assertTrue(wsi_xid_cache.has_xid(ixid1) is False) 
        self.assertTrue(wsi_xid_cache.has_xid(ixid2) is True) 
        self.assertTrue(wsi_xid_cache.is_empty() is False) 

        wsi_xid_cache.drop_if(ixid1)  # try to drop non-existing Xid
        self.assertTrue(wsi_xid_cache.has_xid(ixid1) is False) 
        self.assertTrue(wsi_xid_cache.is_empty() is False) 

        wsi_xid_cache.drop_if(ixid2)
        self.assertTrue(wsi_xid_cache.has_xid(ixid1) is False) 
        self.assertTrue(wsi_xid_cache.has_xid(ixid2) is False) 
        self.assertTrue(wsi_xid_cache.is_empty() is True) 

    def test_private_field(self):
        wsi_xid_cache = WsiXidCache()
        with self.assertRaises(AttributeError):
            wsi_xid_cache.value = 123

if __name__ == '__main__':
    unittest.main()
