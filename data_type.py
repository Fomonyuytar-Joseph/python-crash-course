weight = input("What is your weight: ")
height = input("What is your height: ")

bmi = int(weight) / ( float(height) ** 2)
rounded_bmi = round(bmi , 1)



print(f"Your BMI is {round(rounded_bmi)}")


if rounded_bmi <= 18.5:
    print("You are underweight!")
elif rounded_bmi <= 25:
    print("Your are normal weight!")
elif rounded_bmi <= 30:
    print("You are slightly overweight!")
elif rounded_bmi <= 35:
    print("You are Obese!")
else:
   print("You are clinically Obese!.")
   


