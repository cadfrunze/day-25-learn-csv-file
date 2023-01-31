# import csv
#
# with open("weater_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatura = []
#     for rand in data:
#         new_element = rand
#         if new_element[1] == "temp":
#             pass
#         else:
#             element = new_element[1]
#             element = int(element)
#             temperatura.append(element)
#     print(temperatura)

# import pandas as pd
#
# data = pd.read_csv("weater_data.csv")
# print(data)

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data)