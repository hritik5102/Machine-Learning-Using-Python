class Parent:
    
    def print_last_name(self):
        print('Rathor')
    

class Child(Parent):
    
    def print_first_name(self):
        print('Gabbar')
    
    def print_last_name(self):
        print('Singh')

user = Child()
user.print_first_name()
user.print_last_name()