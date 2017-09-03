import json

class GlobalValues:
	def __init__(self, age_groups={"young":(0,0), "adult":(0,0), "old":(0,0)}, 
				 character_number_traits={0:"", 1: "", 2:'', 3:'', 4:'', 5:''}):
		self. age_groups = age_groups
		self.character_number_traits = character_number_traits

	def write_to_json(self):
		with open("global_values.txt", "w") as f:	
			dump = json.dump(vars(self), f)


if __name__ == "__main__":
	age_groups = {
		"young":(15, 24),
		"adults":(30,50),
		"olds":(50,80)
	}
	character_number_traits = {
		0: "doctor",
		1: "terrorist"
	}

	global_values = GlobalValues(
						age_groups = age_groups,
						character_number_traits = character_number_traits
					)
	global_values.write_to_json()

