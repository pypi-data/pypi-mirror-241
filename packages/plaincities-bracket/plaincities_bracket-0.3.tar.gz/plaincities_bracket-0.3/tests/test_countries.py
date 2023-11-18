import unittest
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from plaincities import Countries

class PlainCitiesTestCase(unittest.TestCase):

    def test_country_select(self):
        countries = Countries()
        
        self.assertIn('Yemen', countries)
        self.assertIn('Vietnam', countries)
        self.assertIn('Cuba', countries)

        self.assertEqual(countries['Cuba'].alpha2, 'CU')

        self.assertEqual(countries['Cuba'].alpha3, 'CUB')
        self.assertEqual(countries['Cuba'].fips, 192)
        self.assertEqual(countries['Vietnam'].alpha3, 'VNM')
        self.assertEqual(countries['Yemen'].fips, 887)
        self.assertEqual(countries['VNM'].name, 'Vietnam')
        self.assertEqual(countries['CU'].alpha3, 'CUB')

        self.assertEqual(countries['Djibouti'].continent, 'AF')
        self.assertEqual(countries['Cuba'].continent, 'NA')
        self.assertEqual(countries['Dominican Republic'].continent, 'NA')
        self.assertEqual(countries['India'].continent, 'AS')

    def test_state_select(self):
        countries = Countries()
        countries['IN'].load_cities()
        countries['CN'].load_cities()
        countries['IQ'].load_cities()
        countries['IR'].load_cities()
        countries['MX'].load_cities()
        self.assertNotIn('Texas', countries['IN'].states)
        self.assertIn('Kerala', countries['IN'].states)
        self.assertIn('Xinjiang', countries['CN'].states)
        self.assertIn('Basra', countries['IQ'].states)
        self.assertIn('Fars', countries['IR'].states)
        self.assertIn('Yucatan', countries['MX'].states)

    def test_city_select(self):
        countries = Countries()
        germany = countries['DE']
        germany.load_cities()
        self.assertIn('Cologne District', germany.states['North Rhine-Westphalia'].districts)
        self.assertGreater(len(germany.states['North Rhine-Westphalia'].\
            districts['Cologne District'].cities), 0)
        koln = germany.states['North Rhine-Westphalia']\
            .districts['Cologne District'].cities['Cologne']
        self.assertEqual(koln.name, 'Cologne')
        turkiye = countries['TR']
        turkiye.load_cities()
        self.assertIn('Ankara', turkiye.states)
        self.assertIn('Ankara', turkiye.cities)
        ankara_city = turkiye.cities['Ankara']
        self.assertEqual(ankara_city.timezone.key, 'Europe/Istanbul')
        iraq = countries['IQ']
        iraq.load_cities()
        self.assertIn('Baghdad', iraq.cities)

    def test_countries_load_options(self):
        countries = Countries(countries_to_load=['IN'])
        self.assertIn('Kerala', countries['IN'].states)
        countries = Countries(continents_to_load=['AF'])
        self.assertIn('Eastern Cape', countries['ZA'].states)
        countries = Countries(load_all=True)
        self.assertIn('Bağcılar', countries['TR'].states['Istanbul'].cities)
        self.assertIn('Bagcilar', countries['TR'].states['Istanbul'].cities)

    def test_city_properties(self):
        countries = Countries(countries_to_load=['CN', 'RU'])
        china = countries['CN']
        guangzhou = china.cities['Guangzhou']
        xining = china.cities['Xining']
        self.assertLess(guangzhou.latitude, xining.latitude)
        self.assertGreater(guangzhou.longitude, xining.longitude)
        russia = countries['RU']
        kaliningrad = russia.cities['Kaliningrad']
        moscow = russia.cities['Moscow']
        self.assertGreater(moscow.population, 1000000)
        self.assertGreater(moscow.population, kaliningrad.population)

    def test_timezones(self):
        countries = Countries(countries_to_load=['US', 'JP'])
        usa = countries['US']
        japan = countries['JP']
        ny_time = datetime(2010, 1, 1, 0, 0, 0, tzinfo=usa.cities['New York'].timezone)
        tokyo_time = datetime(2010, 1, 1, 0, 0, 0, tzinfo=japan.cities['Tokyo'].timezone)
        self.assertEqual((tokyo_time - ny_time).total_seconds(), 60 * 60 * -14)

    def test_city_name_suggestions(self):
        countries = Countries(countries_to_load=['TR', 'GR'])
        turkiye = countries['TR']
        greece = countries['GR']
        ankara_suggestions = list(turkiye.cities.suggest('nkara'))
        self.assertIn('Ankara', ankara_suggestions)
        thessaloniki_suggestions = list(greece.cities.suggest('Tesaloniki'))
        self.assertIn('Thessaloniki', thessaloniki_suggestions)

    def test_filters(self):
        countries = Countries(countries_to_load=['CU'])
        cuba = countries['CU']
        large_cities = cuba.cities.filter(lambda x: x.population > 100000)
        self.assertIn(cuba.cities['Havana'], large_cities)

    def test_languages(self):
        countries = Countries(language='zh', countries_to_load=['CN'])
        china = countries['CN']
        self.assertEqual(china.name, '中国')
        self.assertIn('北京', china.cities)
        countries = Countries(language='tr', countries_to_load=['DE'])
        germany = countries['DE']
        self.assertEqual(germany.name, 'Almanya')
        self.assertIn('Berlin', germany.cities)
        self.assertIn('Münih', germany.cities)
        countries = Countries(language='ar', countries_to_load=['LB'])
        lebanon = countries['LB']
        self.assertEqual(lebanon.name, 'لبنان')
        self.assertIn('بيروت', lebanon.cities)

if __name__ == '__main__':
    unittest.main()
