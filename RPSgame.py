import random
import math

def game():
    user = input("choice ? 'r' for rock, 'p' for paper, 's' for scissors \n")
    user = user.lower()
    
    computer=random.choice(['r','p','s'])
    
    if user==computer:
       
       return (0,user,computer)
     
    if is_win(user,computer):
     
       return (1,user,computer)
    
    return (-1,user,computer)
       
def is_win(player, opponent):

    if(player=='r' and opponent=='s') or (player=='s' and opponent=='p')or (player =='p' and opponent =='r'):
    
       return True
       
    return 
    
def play_best_of(n):

    player_wins = 0
    computer_wins =0
    wins_necessary = n/2
    while player_wins < wins_necessary or computer_wins < wins_necessary:
          result,user,computer=game()
          
          if result==0:
             print("It is a tie.You and the computer have both chosen {}\n".format(user))
          
          elif result==1:
               player_wins+=1
               print("You chose {} and computer chose {} You won\n".format(user,computer))
          
          else:
               computer_wins+=1
               print("You chose {} and computer chose {} You lost\n".format(user,computer))
               print("\n") 
          
    if player_wins > wins_necessary:
        print("you have won the best of {} games".format(n))
             
    else:
        print("you have lost the best of {} games".format(n))     
          
    
play_best_of(3)


