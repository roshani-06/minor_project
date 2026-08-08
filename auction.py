def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Highest bidder is {winner} with bid amount ${highest_bid}")

bids = {}

continue_bidding = True
while continue_bidding:
    name = input("what is your name?\n")
    price = int(input("what is your bid?\n$"))
    bids[name] = price
    should_continue = input("Would you like to continue bidding? Type 'yes' or 'no'\n").lower()
    if  should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n"*20)

