class Bank:
    
    def __init__(self):
        print("Constructor Call hogya")
        #self.bal = 0

    def setbalance(self,x):
        self.bal = x

    def printbalance(self):
        print("Balance: ",self.bal)
    

aman = Bank()  
aman.bal = 10 
print(aman.bal)

aman = Bank()   
print(aman.bal)
#aman.setbalance(10)
#aman.printbalance()

