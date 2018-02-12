import json

student = {"101":{"class":'V', "Name":'Rohit',  "Roll_no":7},
           "102":{"class":'V', "Name":'David',  "Roll_no":8},
           "103":{"class":'V', "Name":'Samiya', "Roll_no":12}}
print student
print '---------'
print(json.dumps(student,sort_keys = True))


x = -456;
y = -1.406;
z =  2.12e-10
print(json.dumps(x));
print(json.dumps(y));
print(json.dumps(z));