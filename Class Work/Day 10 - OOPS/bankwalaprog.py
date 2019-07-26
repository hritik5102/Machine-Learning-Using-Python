class Bank:

    ifsc = "ABCD1234"
    _lock = "Diamond"
    __pwd = '1234'

    def setbalance(self,bal): #setter
        self.balance = bal
    
    def printDetails(self): 
        print("Balance",self.balance)

    def getIFSC(self):
        return self.ifsc

    def showmethepwd(self):
        print(self._Bank__pwd)    


amn = Bank()
amn.setbalance(10)

rmn = Bank()
rmn.setbalance(20)

#amn.printDetails()
#rmn.printDetails()


print(amn.__pwd)


