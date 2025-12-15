def make_pizza(size:int, *toppings):
    print(f"\n making a {size}-inch pizza with the following toppings")
    for topping in toppings:
        print(f"- {topping}")
