import csv

def asList(filepath):
    
    #as a list
    with open(filepath,'rt')as f:
        data = csv.reader(f)
        print(data)
        count = 0
        for row in data:
          print(row)
          count = count+1
    print(count)    

def asDict(filepath):
    
    #as a dictionary
    reader = csv.DictReader(open(filepath))
    print(reader)
    for raw in reader:
        print(raw)


filepath = './Social_Network_Ads.csv'
asList(filepath)
asDict(filepath)