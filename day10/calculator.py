


def calc(f_num , s_num , operand):
    if operand == "+":
      result = f_num + s_num
      return result
    elif operand == "-":
        result = f_num - s_num
    elif operand == "*":
       result = f_num * s_num
    elif operand == "/":
       result = f_num / s_num
    else:
       return 

first_number = int(input("What's the first number: "))
finish_calculation = False

def calculator():
 while not finish_calculation:
   operation = input("What operation do you choose\n +\n -\n *\n / \n Pick an operation: ")
   second_number = int(input("What's the second number: "))

   answer = calc(f_num=first_number , s_num=second_number , operand=operation)
   print(f"{first_number} {operation} {second_number} = {answer}")
   choice = input("Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
   if choice == 'y':
      first_number = answer
   else:    
      finish_calculation = True

calculator()


