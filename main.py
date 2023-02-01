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
import pandas
# import pandas as pd
#
# data = pd.read_csv("weater_data.csv")
# print(data)

import pandas as pd

data = pd.read_csv("weater_data.csv")
# data_dict = data.to_dict()
#
# print(data_dict)
#
# data_temp = data["temp"].tolist()
# # print(data_temp)
# # # average_temp = sum(data_temp) / len(data_temp)
# # # print(round(average_temp))
# #
# # average = data["temp"].mean()
# # print(average)
# print(max(data_temp))
# max_num = data["temp"].max()
# print(max_num)

# print(data[data.vremea == "ploaie"])

# max_temp = data.temp.max()
# print(max_temp)
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# temperature = int(monday.temp)
# # temp_fah = (temperature * 1.8) + 32
# # print(int(temp_fah))
# print(int((temperature * 1.8) + 32))

data_dict = {
    "students": ("Maryus", "Iulia", "Sebi"), #hmmmmm....sa incercam cu tuple
    "skill": (10, 20, 30) # same
}

data1 = pandas.DataFrame(data_dict)
print(data1)
data1.to_csv("testing")

