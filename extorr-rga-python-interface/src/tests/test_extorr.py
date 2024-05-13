import unittest
from extorr import ExtorrRGA

class TestExtorrRGA(unittest.TestCase):
    """
    A unit test class for testing the ExtorrRGA class.

    Attributes:
        rga (ExtorrRGA): An ExtorrRGA object for testing.
    """
    
    def setUp(self):
        """
        Initializes an ExtorrRGA object for testing.
        """
        self.rga = ExtorrRGA()
        
    def test_set_mass_range(self):
        """
        Tests the set_mass_range method of the ExtorrRGA class.
        """
        # Test setting the mass range to 1-10
        self.rga.set_mass_range(1, 10)
        self.assertEqual(self.rga.instrument.StartMass, 1)
        self.assertEqual(self.rga.instrument.EndMass, 10)
        
    def test_start_scan(self):
        """
        Tests the start_scan method of the ExtorrRGA class.
        """
        # Test starting a scan
        self.rga.start_scan()
        self.assertTrue(self.rga.is_scan_complete())
        
    def test_get_data(self):
        """
        Tests the get_data method of the ExtorrRGA class.
        """
        # Test getting RGA data
        self.rga.set_mass_range(1, 10)
        self.rga.start_scan()
        while not self.rga.is_scan_complete():
            pass
        data = self.rga.get_data()
        self.assertIsInstance(data, tuple)
        self.assertIsInstance(data[0], list)
        self.assertIsInstance(data[1], list)
        
if __name__ == '__main__':
    unittest.main()
