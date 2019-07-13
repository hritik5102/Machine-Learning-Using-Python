
#from 0 to 10
for x in range(10):
    print(x)
print("")

#from 5 to 12
for x in range(5, 12):
    print(x)
print("Loop ends")

#from 10 to 40 increment value 5
for x in range(10, 40, 5):
    print(x)
print("")

#While loop
count = 5
while(count < 10):
    print(count)
    count += 1

# For loop with list
fruits = ['apple','banana','mango']

for f in fruits:
    print(f)
    print(len(f))

# Print the numbers which are not available in the list
numbersTaken = [2, 5, 77, 12, 13, 17, 23]

print("Here are the numbers that are still available")

for n in range(1,20):
    if n in numbersTaken:
        continue
    print(n)

# Program to find the magic number
magicNumber = 26

for n in range(101):
    if n is magicNumber:
        print(n, "is the magic number ! ")
        break
    else:
        print(n)

#program to find those numbers which are divisible by 7 and multiple of 5, 
#between 1500 and 2700 (both included).
nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))