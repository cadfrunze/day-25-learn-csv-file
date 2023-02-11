import pandas as pd

fisier = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fisier_data = pd.DataFrame(fisier)

data_color = fisier_data['Primary Fur Color']
print(type(data_color))
# data_color = data_color.tolist()
#
# data_dict = {}
# data_dict['Fur Color'] = ['grey', 'red', 'black']
# data_dict['Count'] = []
#
# print(data_dict)
data_dict = data_color.value_counts().to_dict()
print(data_dict)
data_dict1 = {}
data_dict1['Fur Color'] = ['grey', 'red', 'black']
data_dict1['count'] = []
for element in data_dict.values():
    data_dict1['count'].append(element)

data_final = pd.DataFrame(data_dict1)
data_final.to_csv('squirrel_count.csv')
