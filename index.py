import random

def get_choices():
    player_chioces = input("enter user choice")
    computer_choice = ["rock","paper","seciors"]
    choices = {"player" : player_chioces,"computer" : random.choice(computer_choice)}
    return choices
 
#random is used atking think from list aur dic randomly
def check_win(player,computer):
    print(f"your choice {player},computer choice  {computer}")
    if player == computer:
        return "it tie"
    elif player=="rock" :
     if computer=="paper":
        return "computer win"
     else:
       return "you win" 
    elif player=="paper" :
     if computer=="scissors":
        return "computer win"
     else:
        return "you win"
    elif player==  "scissors" :
     if computer=="rock":
        return "computer win"
     else:
        return "you win"
     
     
x=get_choices()
result=check_win(x["player"],x["computer"])
print(x)

# if i want to value of of dictionary passes variable and [] put key and print





# def check_win(player,computer):
#     print(f"your choice {player},computer choice  {computer}")
#     if player == computer:
#         return "it tie"
#     elif player=="rock" and computer=="paper":
#         return "computer win"
# check_win("rock","paper")
    




















