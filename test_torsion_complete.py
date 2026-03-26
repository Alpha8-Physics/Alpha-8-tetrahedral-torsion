import unittest
from torsion_efficiency import TorsionEfficiency

class TestTorsionEfficiency(unittest.TestCase):

    def test_efficiency_case1(self):
        te = TorsionEfficiency(measurements=[1, 2, 3])
        result = te.calculate_efficiency()
        self.assertAlmostEqual(result, expected_value1, places=2)

    def test_efficiency_case2(self):
        te = TorsionEfficiency(measurements=[4, 5, 6])
        result = te.calculate_efficiency()
        self.assertAlmostEqual(result, expected_value2, places=2)

    def test_efficiency_case3(self):
        te = TorsionEfficiency(measurements=[7, 8, 9])
        result = te.calculate_efficiency()
        self.assertAlmostEqual(result, expected_value3, places=2)

if __name__ == '__main__':
    unittest.main()