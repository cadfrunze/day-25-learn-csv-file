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

data = pd.read_csv("weater_data.csv")
data_dict = data.to_dict()

print(data_dict)

data_temp = data["temp"].tolist()
print(data_temp)
average_temp = sum(data_temp) / len(data_temp)
print(round(average_temp))