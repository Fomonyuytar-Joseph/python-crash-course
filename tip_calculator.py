print("Welcome to the Tip Calculator")
bill = input("What is your bill: ")
tip = input("What is your tip: ")
persons = input("How may people are going to pay: ")

formatted_bill = float(bill)
formatted_tip = int(tip)
formatted_persons = int(persons)

tip_amount = (formatted_tip / 100 ) * formatted_bill
total_bill = formatted_bill + tip_amount

amount_per_person = (total_bill / formatted_persons)
formatted_amount_per_person = round(amount_per_person , 2)

print(f"Each person should pay: ${formatted_amount_per_person}")

