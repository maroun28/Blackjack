suits = ["spades", "clubs", "hearts", "diamonds"]
suit = suits[2]
rank = "k"
value = 10
# print(f"Your card is : {rank} of {suit}" )
print("Your card is : " + rank + " of " + suit)
suits.append("snakes")
# suits += ["snakes"]
for suit in suits:
    print(suit)