class Student:
    __private = 0
    def printData(self):
        print(self._Student__private)


class Boy(Student):
    
    def __init(self,name):
        self.name = name

    def printBoth(self):
        print(self.name)
    



s1 = Student()
s1.printData()
s1._Student__private = 1
print(s1._Student__private) #name mangling
s1.printData()

_Student__private = 3
s1.printData()

s2 = Student()
s2.printData()