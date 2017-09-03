import os

def delete_country(country_name):
	country_name = country_name.title()
	filename = country_name + ".txt"
	## bytt dir til der land lagres
	os.remove(filename)

def delete_family(surname):
	surname = surname.title()
	## bytt dir til dir der pass lagres
	filename = surname + ".xlsx"
	os.remove(filename)
