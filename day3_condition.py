print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

game_over_text = "Game Over"
choice1 = input("Which direction do you want to head to? left or right ")
choice2 = ''
choice3 = ''

if choice1 == 'left':
    choice2 = input("What do you want to do ? swim or wait ")
    if choice2 == 'wait':
        choice3 = input("Which door will choose to open? red , blue or yellow ")
        if choice3 == 'yellow':
            print("You win!")
        else:
          print(game_over_text)
    else:
        print(game_over_text)
else:
   print(game_over_text)


















# print("Welcome to the Love Calculator")
# name1 = input("What is your name? ")
# name2 = input("What is their name? ")

# combined_name = name1 + name2
# lowercase_name = combined_name.lower()
# message = ''

# t = lowercase_name.count('t')
# r = lowercase_name.count('r')
# u = lowercase_name.count('u')
# e = lowercase_name.count('e')

# true = t + r + u + e

# l = lowercase_name.count('l')
# o = lowercase_name.count('o')
# v = lowercase_name.count('v')
# e = lowercase_name.count('e')

# love = l + o + v + e

# combined_score = int(str(true) + str(love))

# if combined_score < 10 or combined_score > 90:
#     message = f"Your score is {combined_score}, you go together like coke and mentos"
# elif combined_score >= 40 and combined_score <= 50:
#     message = f"Your score is {combined_score}, you are good together."
# else:
#  message = f"Your score is {true}{love}"

# print(message)






















# print("Welcome to Python Pizza Deliveries")
# size = input("What size of pizza do you want? S, M or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# bill = 0

# if size == "S":
#     bill = 15

# elif size == "M":
#     bill = 20

# else:
#     bill = 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill +=2
#     else:
#         bill +=3

# if extra_cheese == "Y":
#     bill +=1

# print(f"Your final bill is ${bill}")




# year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 == 0:
#        if year % 400 == 0:
#           print("This is a leap year.")
#        else:
#           print("This is not a leap year.")
#     else:   
#         print("This is a leap year")
        
# else:
#   print("Not a leap year")




# number = int(input("Which number do you want to check: "))

# if number % 2 == 0:
#     print("This is an even number!")
# else:
#   print("This is an odd number!")  


# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))

# if height > 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Children tickets are $5.")
#     elif age<=18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adults tickets are $12.")

#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#          bill +=3
#     print(f"Your final bill is {bill}")
# else:
#   print("Sorry, you have to grow taller before you can ride.")  
