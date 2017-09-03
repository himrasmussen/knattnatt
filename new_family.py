import math
import json

from make_passport import make_passport


class NewFamily:
	def __init__:(self, n_members=0, n_young, 
				  n_adult, n_old, age_percentage,
				  n_male, n_female, country):
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

		self.n_male   = n_male
		self.n_female = n_female

		assert self.n_male + self.n_female == self.n_members, "imbalance n_gender and n_members"

		self.country = country
		self.surname = self.get_surname()

		## bytt dir til der landdata er lagret
		self.country_data = load_json(country)

	def get_surname(self):
		#load country json
		#get random surname and delete it from the country data
		#save modified country data to its json file

	def make_dem_passports(self):
		## refactor, make a new_person method ?
		agegroup_numbers = ["n_young", "n_adult", "n_old"]
		gender_numbers   = ["n_female", "n_male"]
	
		while (n_young, n_adult, n_old, n_female, n_male) != 0:
			agegroup_n = random.chioce(agegroup_numbers)
			vars(self)[agegroup_n] -= 1

			gender_n   = random.choice(gender_numbers)
			vars(self)[gender_n] -= 1
			
			if agegroup_n == "n_young":
				agegroup = "young"
			elif agegroup_n == "n_adult":
				agegroup = "adult"
			else
				agegroup = "old"
			
			if gender_n = "n_female":
				gender = "female"
			else
				gender = "male"

			name = random.choice(self.country_data[gender + "_names"]
		 	city = random.choice(self.country_data["cities"])	

		make_passport(
			name=name, surname=self.surname,
			gender=gender, agegroup=agegroup,
			city=city, country=self.country,
			self.surname)	
