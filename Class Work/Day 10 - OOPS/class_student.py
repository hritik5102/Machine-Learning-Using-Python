class Student:
    def saveRoll(self, x):
        self.rollno = x

s1 = Student()
s1.saveRoll(101)

print(s1.rollno)

s2 = Student()
s2.rollno = 102
print(s2.rollno)




