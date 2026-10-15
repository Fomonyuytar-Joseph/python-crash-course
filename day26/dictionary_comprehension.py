weather_c = {
    "Monday":12,
    "Tuesday":14,
    "Wednesday":15,
    "Thursday":14,
    "Friday":21,
    "Saturday":22,
    "Sunday":24
}
def convert_fah(temp):
    calc_temp = (temp * 9/5) + 32
    return round(calc_temp , 1)


weather_f = {day:convert_fah(temp) for (day , temp) in weather_c.items()}

print(weather_f)






# sentence = "What is the AirSpeed Velocity of an Unladen Swallow?"

# #make an array of words
# word_list =  sentence.split()

# print(word_list)
# #make an
# len_word_dict = {word:len(word) for word in word_list}

# print(len_word_dict)



# import random
# names = ["Myrtle","Olivia","Jesus","Amelia","Noah"]

# students_scores = {student:random.randint(1,100) for student in names}


# passed_students = {student:score for(student , score) in students_scores.items() if score >= 60}



# print(students_scores)

# print(passed_students)