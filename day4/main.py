row1 = ["✅", "✅", "✅"]
row2 = ["✅", "✅", "✅"]
row3 = ["✅", "✅", "✅"]


map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

choice = input("where do you want to insert ? ")

column = int(choice[0]) - 1
row = int(choice[1]) - 1

map[row][column] = "🎉"


print(map)



# import random

# guest_names = input("What is the name of the guests? ")

# list_names = guest_names.rstrip().split(",")

# chosen_index = random.randint(0, len(list_names) - 1)


# print(f"{list_names[chosen_index]} is going to pay Today!")
# print(random.choice(list_names))


# import random

# random_number = random.randint(0,1)

# if random_number == 1:
#     print("Heads")
# else:
#     print("Tails")


# random_integer = random.randint(1,10)
# print(random_integer)


# random_float = random.random() * 5
# print(random_float)
