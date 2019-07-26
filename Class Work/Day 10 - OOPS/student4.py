class Student:
    rollno = 10

    @classmethod
    def modify(cls):
        cls.rollno = 11


s1 = Student()
s2 = Student()

print(s1.rollno)
print(s2.rollno)

s1.modify()

print(s1.rollno)
print(s2.rollno)


