import unittest

from wsit.main.com.vsi.wsi.wsi_structure import WsiStructure
from wsit.main.pyx.xml.rpc.holders.structure_holder import StructureHolder


class TestStructureHolder(unittest.TestCase):
    def test_init(self):
        structure_holder = StructureHolder()
        self.assertTrue(structure_holder.get() is None) 

        wsi_structure = WsiStructure()
        structure_holder = StructureHolder.init_by_wsi_structure(wsi_structure)
        self.assertTrue(structure_holder.get().__eq__(wsi_structure)) 

    def test_to_string(self):
        structure_holder = StructureHolder()
        tested_value = "None"
        self.assertTrue(str(structure_holder).__eq__(tested_value)) 

    def test_equals(self):
        structure_holder = StructureHolder()
        structure_holder_same = StructureHolder()
        structure_holder_other = StructureHolder()

        self.assertTrue(structure_holder.__eq__(None) is False) 
        self.assertTrue(structure_holder.__eq__(int(5)) is False) 
        self.assertTrue(structure_holder.__eq__(structure_holder) is True) 
        self.assertTrue(structure_holder.__eq__(structure_holder_same) is True) 
        structure_holder_other.set(WsiStructure())
        self.assertTrue(structure_holder.__eq__(structure_holder_other) is False) 

    def test_private_field(self):
        byte_holder = StructureHolder()
        with self.assertRaises(AttributeError):
            byte_holder.value = 123
