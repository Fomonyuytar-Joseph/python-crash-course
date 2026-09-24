

bid_dictionary = {}


def add_bid_dictionary(buyer , bid_amount):
      """takes a name and account and create a dictionary from
      this values"""
      bid_dictionary[buyer] = bid_amount


def calc_highest_bid(final_bid):
     winner = ""
     highest_bid = 0
     for key ,value in final_bid.items():
        if value > highest_bid:
             winner = key
             highest_bid = value
     print(f"The winner is {winner} with a bid of  ${highest_bid}")

bidding_finished = False

while not bidding_finished:
    name = input("Enter your name: ")
    amount = int(input("Enter your bid: $"))

    add_bid_dictionary(buyer=name , bid_amount=amount)


    should_continue = input("Are there any other bidders? type 'yes' or 'no'.\n")

    if should_continue == 'no':
         bidding_finished = True
         calc_highest_bid(bid_dictionary)

    