import csv

# with open("Social_Network_Ads.csv") as f:
#     #here


f = open("Social_Network_Ads.csv")
data = csv.reader(f)
print(type(data))
count = 0
purchased = 0
nonpurchased = 0
men = 0
women = 0
salary = []
for single in data:
    if count==0:
        count = count + 1
        continue    
    count = count +1 #for total

    #Purchase
    if single[4] == '1':
        purchased +=1
    else:
        nonpurchased+=1
    
    #Gender Ratio code
    if single[1] == "Male":
        men+=1
    else:
        women+=1
    
    #Create custom list for salary
    salary.append(int(single[3]))

    
print("Total Records: ", count-1)
print("Purchased : ", purchased)
print("Non-Purchased : ", nonpurchased)
print("Total Men : ", men)
print("Total Females : ", women)
print("Min Sal: {min} Max Sal:{max} Average Sal: {avg}".format(min= min(salary),avg=(sum(salary)/count-1), max = max(salary)))
