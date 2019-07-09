import array as arr


roll_no =arr.array('i',[1,2,3,4,5,6,7]) 
#accesing single element
print(roll_no[5])

#Iteration
for i in roll_no:
    print(i)

#Slicing
print(roll_no[1:6])

#Concatination
new_roll = arr.array('i',[8,9])
roll_no = roll_no + new_roll

print(roll_no)

#Typecodes
print(roll_no.typecode)

#ItemSize
print(roll_no.itemsize)

# #Append
roll_no.append(10)
print(roll_no)

# #insert 
roll_no.insert(0,0)
print(roll_no)

# #pop
roll_no.pop(0) #index
print(roll_no)


# #remove
roll_no.insert(0,0) #adding new element
roll_no.insert(0,0) #adding again

print(roll_no)
roll_no.remove(0)  #removing first occurence of 0
print(roll_no)


# #index
print("Index of 7 is : {index}".format(index = roll_no.index(7)))

# #reverse
# roll_no.reverse()
# print(roll_no)

# #count
# count = roll_no.count(4)
# print(count)

# #convert it to list
roll_list = roll_no.tolist()
print(roll_list)

firse_roll_arr = arr.array('i',roll_list)
print(firse_roll_arr)


# #Buffer info
print(firse_roll_arr.buffer_info())

# #Extend Array
firse_roll_arr.extend([11,12])
print(firse_roll_arr)
new_list = list(firse_roll_arr) 
print(new_list)
