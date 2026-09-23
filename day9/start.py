travel_log = [
    {
        "country" : "Cameroon",
        "visits": 12,
        "cities" : ["Buea","Bamenda","Limbe"]
    },
    {
    "country" : "Germany",
    "visits" :5,
    "cities": ["Berlin", "Dortmund" , "Hamburg"]
    },
]

def add_new_country(destination , visited , cities_visited):
    result = {}

    result["country"] = destination
    result["visits"] = visited

    result["cities"] = cities_visited

    travel_log.append(result)

add_new_country(destination="Russia" , visited=2, cities_visited=["Moscow","Saint Petersburg"])

print(travel_log)













# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# student_grades = {}

# for key, value in student_scores.items():
#     if value <= 70:
#         student_grades[key] = "Fail"
#     elif value <= 80: 
#         student_grades[key] = "Acceptable"
#     elif value <= 90:  
#         student_grades[key] = "Exceeds Expectation"
#     else:
#         student_grades[key] = "Outstanding"

# print(student_grades)
