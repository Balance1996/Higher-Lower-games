from higherlowerdic import HL_dic # HL_dic contains dictionary datasets
from higherlowerart import logo
from higherlowerart import vs
from higherlowerart import fireworks
import random

#print(higherlowerart.logo)
#print(higherlowerart.vs)
def display_contender(contender):
    print(f'{contender["Name/club"]} is a {contender["Jobs/description"]} from {contender["Country"]}.')
    
def available_contender(contender):
    available=[c for c in HL_dic if c["Followers"]!=contender["Followers"]]# get all possible c not dup
    new_contender=random.choice(available)
    return new_contender
    
def eval_score(current_contender,challenger,user_choice, score):
    if current_contender["Followers"]==challenger["Followers"]:
        status="Tie"
    elif user_choice=='A' and current_contender["Followers"]>challenger["Followers"]:
        print("You have answer correctly.")
        score+=1
        print(f"Your current score is {score}.")
        status="Keep going"
    elif user_choice=='B' and challenger["Followers"]>current_contender["Followers"]:
        print("You have answer correctly")
        score+=1
        print(f"Your current score is {score}.")
        status="Keep going"
    
    else:
        print(f"Gameover.You lose. Your final score is {score}.")
        print(fireworks)
        status="Loser"
    return score,status
        
def main():
    score=0
    Gameover=False
    status=None
    current_contender=random.choice(HL_dic) #independent selections
    challenger=random.choice(HL_dic) #independent selections
    print(logo)
    while not Gameover:
        contender_display=display_contender(current_contender)
        print(vs)
        challenger_display=display_contender(challenger)
        user_choice=input("Who has the most followers? Enter (A/B):\n").upper()
        #score_fate=compare_followers(current_contender,challenger)
        score, status = eval_score(current_contender,challenger,user_choice,score)
       
        if status == "Tie":
            challenger = available_contender(current_contender)

        elif status == "Loser":
           Gameover = True

        elif status == "Keep going":
           if user_choice == "A":
               # A wins and stays as A
               challenger = available_contender(current_contender)

           elif user_choice == "B":
               # B wins and becomes the new A
               current_contender = challenger
               challenger = available_contender(current_contender)
            
if __name__=="__main__":
    main()
                       

        
            
