class Student:
    def __init__(self):
        self.rollno = 0
    
    def modify(self,x):
        self.rollno = x

s1 = Student()
s2 = Student()

print(s1.rollno)
print(s2.rollno)

s1.modify(1)

print(s1.rollno)
print(s2.rollno)


