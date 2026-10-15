sentence = "What is the AirSpeed Velocity of an Unladen Swallow?"

#make an array of words
word_list = [item for item in sentence.split()]

#make an
len_word_dict = {word:len(word) for word in word_list}





print(len_word_dict)



# import random
# names = ["Myrtle","Olivia","Jesus","Amelia","Noah"]

# students_scores = {student:random.randint(1,100) for student in names}


# passed_students = {student:score for(student , score) in students_scores.items() if score >= 60}



# print(students_scores)

# print(passed_students)