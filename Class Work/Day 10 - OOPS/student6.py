class Student:
    rollNo = 10

    def printRoll(self):
        print(self.rollNo)


s1  = Student()
print(s1.rollNo) #10

s1.rollNo = 11
print(s1.rollNo) #11

s2 = Student()
print(s2.rollNo) #10

Student.rollNo = 100 

s3 = Student()
print(s3.rollNo) #100


s1.printRoll()
s2.printRoll()