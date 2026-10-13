import pandas

# data = pandas.read_csv("weather_data.csv")

# temp_list = data["temp"].to_list()
# print(temp_list)


# print(data["temp"].mean())
# print(data["temp"].max())


# Get data in columns
# print(data["condition"])
# print(data.condition)


# Get data in row
# print(data[data.day == "Monday"])

# Get row of data with max temperature
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp.iloc[0])

# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# Creating a Data Frame
data_dict = {
    "students": ["joe", "max", "christy"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)

# print(monday.condition)
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)


# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)


# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
