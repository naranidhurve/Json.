
# import json
# a={'lalalala':3}
# mystring = json.dumps(a)
# print(mystring)


import json
dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
#         "age": "24",
        "salary": "40000"
    },
}
out_file = open("myfile.json", "w")
# json
# ("dict1",out_file,indent=6)
out_file.close()
print(dict1)




