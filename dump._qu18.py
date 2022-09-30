

import json
a={"name":"pavni" ,
   "class":"json" ,
   "age":4
   }
f=open('narani.json','w')
v=json.dump(a,f,indent=1)
print(v)


# a="eshu"
# b="nav"
# c="gurukul"
# d=2.5
# e=int (d)
# f=b+c
# print(a,f)

# a="eshu"
# b="navgurukul"
# c="navgurukul"
# d=b+c
# e=a+d
# print(e)
