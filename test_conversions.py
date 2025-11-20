import unittest
import conversions
import math

class TestConversions(unittest.TestCase):

    def test_meters_to_feet(self):
        self.assertAlmostEqual(conversions.meters_to_feet(1), 3.28084, places=5)

    def test_feet_to_meters(self):
        self.assertAlmostEqual(conversions.feet_to_meters(3.28084), 1, places=5)

    def test_kilograms_to_pounds(self):
        self.assertAlmostEqual(conversions.kilograms_to_pounds(1), 2.20462, places=5)

    def test_pounds_to_kilograms(self):
        self.assertAlmostEqual(conversions.pounds_to_kilograms(2.20462), 1, places=5)

    def test_grams_to_pounds(self):
        self.assertAlmostEqual(conversions.grams_to_pounds(1000), 2.20462, places=5)

    def test_pounds_to_grams(self):
        self.assertAlmostEqual(conversions.pounds_to_grams(2.20462), 1000, places=3)

    def test_ounces_to_grams(self):
        self.assertAlmostEqual(conversions.ounces_to_grams(1), 28.3495, places=4)

    def test_grams_to_ounces(self):
        self.assertAlmostEqual(conversions.grams_to_ounces(28.3495), 1, places=4)

    def test_inches_to_millimeters(self):
        self.assertAlmostEqual(conversions.inches_to_millimeters(1), 25.4, places=5)

    def test_millimeters_to_inches(self):
        self.assertAlmostEqual(conversions.millimeters_to_inches(25.4), 1, places=5)

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(conversions.celsius_to_fahrenheit(0), 32)

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(conversions.fahrenheit_to_celsius(32), 0)

    def test_degrees_to_radians(self):
        self.assertAlmostEqual(conversions.degrees_to_radians(180), math.pi, places=5)

    def test_radians_to_degrees(self):
        self.assertAlmostEqual(conversions.radians_to_degrees(math.pi), 180, places=5)

    def test_psi_to_bar(self):
        self.assertAlmostEqual(conversions.psi_to_bar(100), 6.89476, places=5)

    def test_bar_to_psi(self):
        self.assertAlmostEqual(conversions.bar_to_psi(6.89476), 100, places=4)

if __name__ == '__main__':
    unittest.main()
