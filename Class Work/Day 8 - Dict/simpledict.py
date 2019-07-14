# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': { 'age': 21}, 1: [2, 4, 3]}
print(my_dict[1][2])
print(my_dict['name']['age'])



# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])

print(my_dict)






#create an empty dictionary
x = {}

#create a three items dictionary
x = {"one":1, "two":2, "three":3}

#access an element
x['two']

#get a list of all the keys
x.keys()

#get a list of all the values
x.values()

#add an entry
x["four"]=4

#change an entry
x["one"] = "uno"

#delete an entry
del x["four"]

#make a copy
y = x.copy()

#remove all items
x.clear()

#number of items
z = len(x)


#looping over keys
for item in x.keys(): 
    print (item)

#looping over values
for item in x.values(): print (item)

#using the if statement to get the values
if "one" in x:
    print(x['one'])

if "two" not in x:
    print ("Two not found")

if "three" in x:
    del x['three']