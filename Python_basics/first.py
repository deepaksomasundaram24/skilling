import random 
def get_player_value():
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = str(input("type either rock,paper or scissors"))
    choices = {"player": player,"computer":computer}
    return choices

def check_win(player,computer):
    print(f"You chose {player} and computer chose {computer}")
    print(type(player),type(computer))
    if player == computer:
        return "It is a tie!"
    elif player == "rock":
        if computer == "paper":
            return "paper covers rock, computer wins !"
        else:
            return "player wins !"
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock, player wins !"
        else:
            return "computer wins !"
    else:
        if computer == "paper":
            return "scissors cut paper, player wins !"
        else:
            return "computer wins !"

values = get_player_value()
print(check_win(values["player"],values["computer"]))
            
import Learning.Python_basics.lib.mod as mod
mod.cat()
        
