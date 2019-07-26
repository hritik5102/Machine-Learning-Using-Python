class Student:
    course = "B.Tech"

    def setRollNo(self,x):
        self.rollNo = x 
    
    def printDetails(self):
        print(self.rollNo, self.course)
    
    def changeCourse(self, c):
        self.course = c
        

s1 = Student()
s1.setRollNo(101)
s1.printDetails()

s2 = Student()
s2.setRollNo(102)
s2.printDetails()


s2.changeCourse("B.Sc")
s2.printDetails()

s3 = Student()
s3.setRollNo(103)
s3.printDetails()



