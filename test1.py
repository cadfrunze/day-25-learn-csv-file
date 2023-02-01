import pandas as pd
from main import data_temp

num_check = 0

for num in data_temp:
    num_check = num_check + num


print(f"Num_check este {num_check}")
print(f"data_temp cu sum este{sum(data_temp)}")