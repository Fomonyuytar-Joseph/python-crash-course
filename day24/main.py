invited_guests = []
sample_letter = ""

with open("input/Names/invited_names.txt") as file:
    contents = file.read()
    invited_guests = contents.splitlines()

# print(invited_guests)


with open("input/Letters/sample_letter.txt") as file:
    contents = file.read()
    sample_letter = contents
    # print(contents.replace("[name]","Max"))

for invited_guest in invited_guests:
    with open(f"output/ReadyToSend/letter_for_{invited_guest}.txt", "w") as file:
        file.write(sample_letter.replace("[name]", invited_guest))


# file=open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()


# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("new_file.txt", mode="w") as file:
#     file.write("\nHello My name is Joseph")
