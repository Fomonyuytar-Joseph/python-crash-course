import math
def paint_cal(height ,width , cover):
    num_of_cans = (height * width) / cover
    print(f"You will need {math.ceil(num_of_cans)} of paint")

test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))

coverage = 5

paint_cal(height=test_h , width= test_w , cover=coverage)


