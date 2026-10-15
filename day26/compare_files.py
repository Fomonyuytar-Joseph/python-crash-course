with open("file1.txt") as file1:
    file1_contents = file1.read().splitlines()
    # print(contents)

with open("file2.txt") as file2:
    file2_contents = file2.read().splitlines()

# print(file1_contents)
# print(file2_contents)


common_list = [int(item) for item in file2_contents if item in file1_contents]

print(common_list)
