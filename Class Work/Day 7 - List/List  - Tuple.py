#empty
list = []

#append
list.append("Hi")
list.append("Hey")
list.append("Hlo")

#insert
list.insert(2,"Hello")

#extend
list.extend(["Hnji",0])

print(list)
#remove 
list.remove(0)
print(list)

#pop
list.pop() #last
list.pop(0) #index

print(list)

#clear
#list.clear()
#print(list)

#index
# ch = 'dh'
# s = "sdhjfhlsdjgjfshfjhsgfksdgf"

# for item in ch:
#     print(s.index(item))



list= [4,56,3,2,5,67,342,32]

list.sort(reverse = True)

print(list)
#list.reverse()

del list

#print(sum(list))

list1 = [1,23,5,46,47,56]

del list1[:2] #delete multiple using slice
print(list1)
del list1  #delete whole list
#print(list1)


list1 = [1,2,3,4]
list2 = [2,3,54,5]
list3 = list1 + list2

print(list3)



t1 = tuple(list3)
t2 = ([1,2,3],[4,5,6])
t2[0].append(1)
#t2[0]=[]
print(t2[0][1])


t3 = 1,2,3
print(t3)

t4= (1)

