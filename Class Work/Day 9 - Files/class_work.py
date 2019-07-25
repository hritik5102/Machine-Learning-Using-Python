# f = open('sample.txt','')
# f.write("Hello There!\n Hi")
# f.close()
def createfile(filename,mode='r'):
    #f = 0
    try:
        f = open(filename,mode)
        #f.write()
        print("Writable flag ",f.writable())
        print("Readable Flag ",f.readable())
    except PermissionError:
        print("File is not writable")    
    except FileNotFoundError:
        print("File doesn't exist")  
    except UnboundLocalError:
        print("Something went wrong")      
    finally:    
        f.close()

filename = input("Enter new file name")
createfile(filename)
