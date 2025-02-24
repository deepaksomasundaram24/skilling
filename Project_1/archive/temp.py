# import pandas as pd

# # # Creating a DataFrame
# # # data = {
# # #     "Name": ["Alice", "Bob", "Charlie"],
# # #     "Age": [25, 30, 22],
# # #     "Salary": [50000, [70000,20,30,40], 45000]
# # # }
# # # df = pd.DataFrame(data)

# # # # Updating a cell (row label 1, column "Salary")
# # # df.at[1, "Salary"].append(90) 
# # # print(df.at[1, "Salary"])

# # venika = []
# # print(len(venika))
# # # temp = [1,2,3,4,5,6,7,8]

# # # for venika in temp:
# # #     print(venika)

# import pandas as pd

# df = pd.DataFrame({
#     "Category": ["A", "A", "B", "B", "C", "C", "A"],
#     "Value": [10, 20, 15, 25, 30, 5, 35]
# })

# grouped = pd.DataFrame(df.groupby("Category")["Value"].get_group("A").head(1).reset_index())
# print(grouped["Value"].to_list())

# print(df.loc[2])

# # # Iterate and print each group
# # for key, group in grouped:
# #     print(f"Group: {key}")
# #     print(group)
# #     print()

# x = [1,2,4,3]
# y = [1,2,3,4,5,6,7,8]

# for z in x:
#     if z in y
#         print(z)
import json
from os import path
# with open ('temp.json','r') as file:
#     data = json.load(file)

# print(data)
file_name = "/Users/user/Projects/Learning/Project_1/archive/temp.json"
new_data = { "1001" : {"title" : "dumsharades damaka","genre" : "Romance", "rating": 9 ,"release_year": 2017,"cast": ["Badrinath Wife","Marcus Aurelius","Ram Paul"]}}

if path.isfile(file_name) ==  False:
    raise Exception ("File not found.")

with open(file_name) as file:
    try:
        json_dict = json.load(file)
        json_dict.update(new_data)
    except json.decoder.JSONDecodeError:
        json_dict = {}

with open(file_name,'w') as json_file:
    json.dump(json_dict,json_file,indent = 4)





