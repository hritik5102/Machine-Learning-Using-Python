class Student:
    x =10

s1 = Student()
s2 = Student()

print(id(s1.x))
print(id(s2.x))

s1.x = 20
print(s1.x)
print(id(s1.x))
del s1.x
print(s1.x)
print(id(s1.x))







