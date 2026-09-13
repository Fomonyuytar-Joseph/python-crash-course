age = input("What is your age: ")
converted_age = int(age)


number_of_days_ninety = 90 *  365
number_of_weeks_ninety = 90 *  52
number_of_months_ninety = 90 * 12


days_lived = converted_age * 365
weeks_lived = converted_age *  52
months_lived = converted_age * 12

days_remaining = number_of_days_ninety - days_lived
weeks_remaining = number_of_weeks_ninety - weeks_lived
months_remaining = number_of_months_ninety - months_lived

print(f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} left.")
