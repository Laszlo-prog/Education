mport random

def get_ash_choice():
    while True:
     choice = input("Choose Your Pokemon(cubone/pikachu/starmie/bulbasaur):").lower()
    if choice in ["cubone","pikachu","starmie","bulbasaur"]:
        return choice
    print("Choose another Pokemon:")
    
def get_dan_choice():
    return random.choice(["cubone","pikachu","starmie","bulbasaur"])
    
def determine_winner(ash_choice, dan_choice):
    if ash_choice == dan_choice:
        return "It's a crash!"
    elif(
        (ash_choice == 'pikachu' and dan_choice == 'cubone') or
        (ash_choice == 'bulbasaur' and dan_choice == 'starmie')or
        (ash_choice == 'cubone' and dan_choice == 'pikachu')or
        (ash_choice == 'starmie' and dan_choice == 'bulbasaur')
        ):
            return "You win"
    else:
            return "Opponet win"

def play_battle():
    ash_score = 0
    dan_score = 0
    
    
    while True:
    
         ash_choice = get_ash_choice()
         dan_choice = get_dan_choice()
         
         print(f"\nYou chose{ash_choice}")
         print(f"Opponet chose{dan_choice}")
    result = determine_winner(ash_choice, dan_choice)
    print(result)
    
    if "You win" in result:
        ash_score += 1
    elif "Opponet win" in result:
        dan_score += 1
    
    print(f"\nScore - You: {ash_score}, Opponet: {dan_score}")
    
def play_battle():
    play = input("Do  you want play again? (yes/no):").lower()
    if play != "yes":
       print('lets go')
    elif play != "no":
        print("Goodby").exit()
    else:    
         print("\nThanks for playeing")



if __name__ == "main":

  play_battle()
