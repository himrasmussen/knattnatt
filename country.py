import json

class Country():
	def __init__(self, name='', english_name='', 
				country_letter='', passport_font='', 
				len_person_number='',surnames='', 
				female_names='', male_names='',
				cities=''):
                                     
		self.name = name.title()
		self.english_name = english_name .title()

		self.country_letter = country_letter .title()
		self.passport_font = passport_font.title()
		self.len_person_number = len_person_number

		self.surnames = [x.title() for x in surnames]
		self.female_names = [x.title() for x in female_names]
		self.male_names = [x.title() for x in male_names]
		self.cities = [x.title() for x in cities]
			
		self.write_to_json()

	def make_title(self, array):
		return [x.title() for x in array]

	def write_to_json(self):
		filename = self.english_name + ".txt" ## NOE KAN CRASHE HER!!! ## Kan man kreve at et felt fylles ut i PyQt?
											  ## Fyll ut English_Name-feltet med landet som er valgt
		with open("{}.txt".format(self.english_name), "w") as f:
			json.dump(vars(self), f)

if __name__ == "__main__":
		norway = Country(
			name="Norge", 
			english_name="Norway",
			country_letter="N",
			len_person_number = 11,
			surnames = ["Jansen", "Moen", "Bakken", "Rusta", "Berg"],
			male_names = ["Ola", "Per", "Jens", "Tor", "Tom", "Odd", "Ask", "Tov"],
			female_names = ["Siv", "Liv"],
			cities = ["Lillehammer", "Oslo", "Bergen", "trondheim"]
			)
		norway.write_to_json()



