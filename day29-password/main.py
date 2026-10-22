facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass
        



print(total_likes)













# fruits = ["Apple" , "Pear" , "Orange"]

# def make_pie(index:int):
    
#     try:
#         fruit = fruits[index]
#     except IndexError as error_message:
#         print("Fruit Pie")
#         print(f"You could not print out of index because of {error_message}")
#     else:
#         print(fruit+ " pie")

# make_pie(4)



# height  = float(input("Height: "))
# weight  = int(input("Weight: "))


# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")

# bmi = weight / height ** 2

# print(bmi)



#FileNotFound

# try:
#     file = open("a_file.txt")
#     a_dict = {"id":"value"}
#     # print(a_dict["id"])
# except FileNotFoundError:
#     file = open("a_file.txt","w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError
    # raise TypeError("This is an error I made up")
    # file.close()
    # print("File was closed")

 