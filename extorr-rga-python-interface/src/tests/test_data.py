import unittest
from data import calculate_total_pressure

class TestData(unittest.TestCase):
    def test_calculate_total_pressure(self):
        """
        Test case for the calculate_total_pressure function in the data module.

        This test case checks that the function correctly calculates the total pressure from the partial pressures of the
        detected gas species for a given set of input data.
        """
        partial_pressures = [1.0, 2.0, 3.0, 4.0, 5.0]  # Example input data
        expected_result = sum(partial_pressures)  # The expected result for the example input data
        result = calculate_total_pressure(partial_pressures)  # Calculate the result using the function being tested
        self.assertAlmostEqual(result, expected_result, places=2)  # Verify that the calculated result is within 2 decimal places of the expected result

