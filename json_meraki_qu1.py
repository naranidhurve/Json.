# import json
# x='{ "name":"John", "age":30, "city":"New York"}'
# y=json.loads(x)
# print(y["age"]) 


import json
x = {
  "name": "Ken",
  "age": 45,
  "married": True,
  "children": ("Alice","Bob"),
  "pets": ['Dog'],
  "cars": [
    {"model": "Audi A1", "mpg": 15.1},
    {"model": "Zeep Compass", "mpg": 18.1}
  ]
}
# sorting result in asscending order by keys:
sorted_string = json.dumps(x, indent=4, sort_keys=True)
print(sorted_string)

