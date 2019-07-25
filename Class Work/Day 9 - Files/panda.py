import pandas
result = pandas.read_csv('./Social_Network_Ads.csv',sep=',')
print(type(result))
print(result.to_dict())