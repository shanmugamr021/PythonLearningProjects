from art import logo
# TODO-1: Ask the user for input
print(logo)
print("Welcome to the secret auction program.")
is_other_bidder = "yes"
person_bids = {}
while is_other_bidder == "yes":
    name = input("What is your name? ")
    bid = int(input("What's your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    person_bids[name] = bid
    # TODO-3: Whether if new bids need to be added
    is_other_bidder = input("Are there any other bidders? Type 'yes' or 'no' \n")
    while is_other_bidder != "yes" and is_other_bidder !="no":
        is_other_bidder = input("Your selection is wrong. Are there any other bidders?? Type 'yes' or 'no' \n")
    print("\n"*100)
# TODO-4: Compare bids in dictionary
max_bid = 0
max_bedded_person = ""
for key in person_bids:
    if max_bid < person_bids[key]:
        max_bid = person_bids[key]
        max_bedded_person = key

print(f"The winner is {max_bedded_person} with a bid of ${max_bid}.")