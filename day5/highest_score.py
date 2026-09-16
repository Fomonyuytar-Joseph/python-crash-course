student_scores = input("Input a list of student scores: ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)


highest_score = student_scores[0]

for index in range(1 , len(student_scores)):
    if student_scores[index] > highest_score:
        highest_score = student_scores[index]

print(f"The highest score in the class is: {highest_score}")


sum = 0

for number in range(1,101):
    sum+=number

print(sum)
# 78 65 89 86 55 91 64 89
