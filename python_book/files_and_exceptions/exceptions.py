from pathlib import Path


path = Path("joe.txt")

try:
    contents = path.read_text()
except FileNotFoundError:
    print(f"sorry, the file {path} does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")




# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")


# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break

#     second_number = input("\nSecond number: ")
#     if second_number == "q":
#         break

#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by Zero⚠️")
#     else:
#         print(answer)


# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by Zero⚠️")
