import pandas

data = pandas.read_csv("squirrel_count.csv")

fur_color = ["grey" , "red" ,"black"]

grey_squirrel = data[data["Primary Fur Color"] == "Gray"]
red_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrel = data[data["Primary Fur Color"] == "Black"]


print(type(red_squirrel))
num_grey = len(grey_squirrel)
num_red = len(red_squirrel)
num_black = len(black_squirrel)

squirrel_num_list = [num_grey , num_red , num_black]


data_dict ={
    "Fur Color": fur_color,
    "Count":squirrel_num_list
}

new_squirrel_data = pandas.DataFrame(data_dict)
new_squirrel_data.to_csv("squirrel_data.csv")




# print(len(grey_squirrel))
# print(len(red_squirrel))
# print(len(black_squirrel))