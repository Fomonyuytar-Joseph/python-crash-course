def calculate(**kwargs):
    print(kwargs)
    for key , value in kwargs.items():
        print(key, value)


calculate(add=2, multiply=5)



# def addNumbers(*args):
#     print(args[0])
#     sum = 0
#     print(args)
#     for n in args:
#         sum += n
#     return sum


# print(addNumbers(2, 3, 4, 5, 6, 7, 8, 90))
