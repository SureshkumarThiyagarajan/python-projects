
import random

#list of choices
choice_list = ["rock", "paper", "scissors"]

#computer's choice
computer_choice = random.choice(choice_list)

#decision making
def decision_making():
    if ((user_choice == 'paper') & (computer_choice == 'rock')) or ((user_choice == 'scissors') & (computer_choice == 'paper')) or ((user_choice == 'rock') & (computer_choice == 'scissors')) :
        print("You Win!")
    elif ((computer_choice == 'paper') & (user_choice == 'rock')) or ((computer_choice == 'scissors') & (user_choice == 'paper')) or ((computer_choice == 'rock') & (user_choice == 'scissors')) :
        print("Computer Wins!")
    else:
        print("It's a tie")

while True:
    #user's choice
    user_choice = input("Enter rock, paper or scissors (or 'q' to quit): ").lower()

    if user_choice in choice_list:
       print("You choose " + user_choice +", " + "Computer choose " + computer_choice)
       decisiion = decision_making()

    elif user_choice == 'q':
        print("Exiting Bye")
        break

    else:
        print("Invalid input & Enter the choice in the list")
    


