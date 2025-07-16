import random
cards=[]
suits=["spades","clubs","hearts","diamonds",]
ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])
def shuffle():
    random.shuffle(cards)
 
def deal(number):
    cards_dealts=[]
    for x in range(number):
        card=cards.pop()
        cards_dealts.append(card)
        return cards_dealts
shuffle()

card=deal(1)[0]
print(card)
# card=card_delta[0]
# rank=card[1]

# if rank=="A":
#     value = 10
# elif rank=="J" or rank=="Q" or rank=="K":
#     value=10
# else:
#     value =rank
# print(rabk_dict["rank"],rank_dict["value"])
