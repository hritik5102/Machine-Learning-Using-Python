#print("Hi")


#No param no return
def printSquare():
    print("Square")

#With param w/o return
def printSquare2(x):
    print("Square : ",x*x)

#with param with return
def getSquare(x,y):
    printSquare()
    return x*x

def defaultSquare(i=1):
    print(i*i)

#printSquare()
#printSquare2(10)
#sq = getSquare(5)
#print("Square is ", sq)

defaultSquare()
defaultSquare(5)
