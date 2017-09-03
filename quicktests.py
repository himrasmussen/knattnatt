import json

foo = {"name":"mari", "age":2, "names":["one", "two", "three"]}
foo = json.dumps(foo)

with open("jsontest.txt", "w") as f:
	f.write(foo)

with open("jsontest.txt", "r") as f:
	data = json.load(f)
	print(data)	
