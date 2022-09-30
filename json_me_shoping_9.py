
# import json
# q={
#     "shopping_list":
#         { 
#             "chaco":"15",
#             "Biscuits":"50",
#             "Diary_milk":"30",
#             "ice_cream":"20",
#         } 
# }
# z=json.dumps(q)
# print(z)
# # print(type(z))

import json
q={"shopping_list":{ "choco":"15",
                    "Biscuits":"50",
                    "Diary_milk":"30",
                    "ice_cream":"20",}}
item=input("enter the item:")
quantity=int(input("how much you want to buy:"))
a=q["shopping_list"][item]
r=int(a)-quantity
q["shopping_list"][item]=r
print(q)
