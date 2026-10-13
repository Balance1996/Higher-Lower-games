#from higherlowerdic import HL_dic #HL_dic contains dictionary datasets
from higherlowerdic import HL_dic
from higherlowerart import logo
from higherlowerart import vs
from higherlowerart import fireworks
import random

#print(higherlowerart.logo)
#print(higherlowerart.vs)
def display_contender(contender):
    print(f'{contender["Name/club"]} is a {contender["Jobs/description"]} from {contender["Country"]}.')
    
def eval_score(current_contender, challenger, user_choice, score):
    if user_choice == 'A':
        correct = current_contender["Followers"] > challenger["Followers"]

    elif user_choice == 'B':
        correct = challenger["Followers"] > current_contender["Followers"]

    else:
        correct = False

    if correct:
        score += 1
        print("You answered correctly.")
        print(f"Your current score is {score}.")
        status = "Keep going"
    else:
        print(f"You lose. Your final score is {score}.")
        status = "Loser"

    return score, status
def get_challenger(current_contender):
    available = [c for c in HL_dic if c["Followers"] != current_contender["Followers"]]

    if not available:
        return None

    return random.choice(available)        
def main():
    score=0
    Gameover=False
    status=None
    current_contender=random.choice(HL_dic)
    challenger=random.choice(HL_dic)
    print(logo)
    while not Gameover:
        contender_display=display_contender(current_contender)
        print(vs)
        challenger_display=display_contender(challenger)
        user_choice=input("Who has the most followers? Enter (A/B):\n").upper()
        score, status = eval_score(current_contender,challenger,user_choice,score)
        if status=="Loser":
            
            Gameover=True
        elif score==19:
            print(fireworks)
            Gameover=True
       
        elif status == "Keep going":
            if challenger["Followers"] > current_contender["Followers"]:
                # B wins: B becomes the new A
                frozen_c = current_contender
                HL_dic.remove(frozen_c)

                current_contender = challenger
                challenger = get_challenger(current_contender)

            else:
                # A wins: A stays; B is removed
                frozen_c = challenger
                HL_dic.remove(frozen_c)

                challenger = get_challenger(current_contender)

            if challenger is None:
                print(f"You win with the full score of {score}.")
                print(fireworks)
                Gameover = True

        
if __name__=="__main__":
    main()
            
         
        
        
    
    
    
    
    
        
