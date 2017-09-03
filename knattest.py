import unittest

from country import Country

class CountryDataTypeTest(unittest.TestCase):
	def setUp(self):
		surnames = ["bakken", "Normann", "Trå", "Lund", "Tokerud"]
		female_names = ["lise", "Oda", "Kari", "Mari", "Line", "Frida"]
		male_names = ["per", "Peder", "Espen", "Ola", "Marius", "Håvard"]
		cities = ["oslo", "Hamar", "Lillehammer", "Bergen", "Trondheim"]

		self.keyword_arguments = {"name": "norge", "english_name": "norway",
							 "country_letter": "n", "passport_font": "arial",
							 "len_person_number": 11,
							 "surnames": surnames,
							 "female_names": female_names,
							 "male_names": male_names,
							 "cities": cities}
	
		self.country = Country(**self.keyword_arguments) 

	def are_country_values_correct(self):
		for k, v in vars(self.country).items():
			if type(v) == list:
				self.assertEqual([x.title() for x in self.keyword_arguments[k]], v)
			elif type(v) == str:
				self.assertEqual(v, self.keyword_arguments[k].title())

	def test_json(self):
		pass


	def test_make_family(self):
		pass
		# test om etternavn ble fjernet fra etternavnlisten

unittest.main()
