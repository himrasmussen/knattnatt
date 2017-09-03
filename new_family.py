import math
import json

from make_passport import make_passport


class NewFamily:
	def __init__:(self, n_members, n_young, 
				  n_adult, n_old, age_percentage,
				  n_male, n_female, gender_percentage,
				  country):
		if age_percentage:
			self.n_young = round(n_members / 100 * n_young)
			self.n_adult = round(n_members / 100 * n_adult)
			self.n_old   = round(n_members / 100 * n_old)
			while sum([self.n_young, self.n_adult, self.n_old]) < n_members:
				self.n_young += 1
		else:
			self.n_young = n_young
			self.n_adult = n_adult
			self.n_old = n_old
			self.n_members = sum([n_young, n_adult, n_old])

		if gender_percentage:
			self.n_male   = round(n_members / 100 * n_male)
			self.n_female = round(n_members / 100 * n_female)
		else:
			self.n_male   = n_male
			self.n_female = n_female

		self.country = country
		self.surname = self.get_surname()

		## bytt dir til der landdata er lagret
		self.country_data = load_json(country)

	def get_surname(self):
		#load country json
		#get random surname and delete it from the country data
		#save modified country data to its json file

	def make_dem_passports(self):
		def make_passport_for_age_group(self, n, group
