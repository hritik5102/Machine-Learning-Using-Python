f = open("data.txt")      # equivalent to 'r' or 'rt'
# or f = open("data.txt",mode = 'r',encoding = 'utf-8')
try:
    f = open("data.txt",mode = 'w',encoding = 'utf-8')
   
except PermissionError:
    print("Writeable flag",f.writable())
    print("File is not writeable by the program")

print(f.readable())
print(type(f.read()))
print(f.read(5))
print(f.read(5))
print(f.tell())
print(f.seek(0))
lines = f.readlines()

for line in lines:
    print(line,end='')

print()

