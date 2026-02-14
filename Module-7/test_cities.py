from city_country import get_formated_city
import unittest


class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):

      self.assertEqual(get_formated_city("Santiago", "Chile"), "Santiago, Chile")



    def test_city_country_with_population(self):

      self.assertEqual(get_formated_city("Santiago", "Chile", population="12,000"), "Santiago, Chile - population 12,000")



    def test_city_country_with_language(self):

      self.assertEqual(get_formated_city("Santiago", "Chile", language="spanish"), "Santiago, Chile, spanish")



if __name__ == "__main__":

    unittest.main()