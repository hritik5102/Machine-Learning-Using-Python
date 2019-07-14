months = {}
months = { 1 : "January", 
     	2 : "February", 
    	3 : "March", 
        4 : "April", 
     	5 : "May", 
     	6 : "June", 
    	7 : "July",
        8 : "August",
     	9 : "September", 
    	10 : "October", 
        11 : "November",
    	12 : "December" } 
print ("The dictionary contains the following keys: ", months.keys())

whichMonth = months[1]
print(whichMonth)

del(months[5])
print(months.keys())

months[5] = "May"
print(months.keys())

sortedkeys = months.keys()
print (sortedkeys)

for key in months:
    print(key, months[key])

for key, value in months.items():
    print (key, value)

print ("The entries in the dictionary are:")
for item in months.keys():
    print ("months[ ", item, " ] = ", months[ item ])

customers = [{"uid":1,"name":"John"},{"uid":2,"name":"Smith"},{"uid":3,"name":"Andersson"}]
print(customers)
for x in customers:
    print(x["uid"], x["name"])

customers[2]["name"]="charlie"
print (customers)

for x in customers:
    x["password"]="123456" # any initial value

print(customers)

del customers[1]
print (customers)

for x in customers:
    del x["id"]

print(customers)