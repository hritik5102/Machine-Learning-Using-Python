import csv 

def asList(filepath):
    #as a list
    with open(filepath,'rt') as f:
        data = csv.reader(f)
        print(data,type(data))
        for row in data: 
                print(type(row))

def asDict(filepath):
    #as a dictionary
    reader = csv.DictReader(open(filepath))
    for raw in reader:
        print(raw["Programming language"])

def aslistofDict(filepath):
    #as a list   
        lst = []
        reader = csv.DictReader(open(filepath))
        for raw in reader:
                lst.append(raw)
        return lst
        
def writeFile(filepath):
    with open(filepath, mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        #way to write to csv file
        writer.writerow(['Programming language', 'Designed by', 'Appeared', 'Extension'])
        writer.writerow(['Python', 'Guido van Rossum', '1991', '.py'])
        writer.writerow(['Java', 'James Gosling', '1995', '.java'])
        writer.writerow(['C++', 'Bjarne Stroustrup', '1985', '.cpp'])

filepath = './languages.csv'
#asList(filepath)
#asDict(filepath)
json = aslistofDict(filepath)
print(type(json))
for one in json:
        print(one['Programming language'])

# newfile = './writeData.csv'
# writeFile(newfile)
