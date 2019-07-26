class Student:
    x =10

s1 = Student()
print(s1.x) # 10

s1.x = 11 # 10 chnaged to 11 in s1 obj

print(s1.x) # print 11

s2 = Student() # new s2 obj with value 10

print(s2.x) # 10 inherited from class

s2.x = 30  # 10 in s2 changed to 30
Student.x = 100 #Class variable changed to 100

print(s2.x) #30 from s2 obj
print(s1.x) #11 from s1 obj

s3 = Student() #new s3 obj with value 100 

print(s3.x) # 100 copied from class space
