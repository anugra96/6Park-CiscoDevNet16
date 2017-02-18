import random

x = random.choice(list(range(1,3)))


def computer_choice ():
    computer = x
    if computer == 1:
        computer = "rock"
        return computer
    elif computer == 2:
        computer = "paper"
        return computer
    else:
        computer = "scissors"
        return computer
    
def f2 ():
    user_choice = str(input("Choose rock, paper, or scissors:"))
    comp_choice = computer_choice()
    if user_choice == comp_choice:
        print("Tie, choose again")
        return f2()
    elif user_choice == "rock":
        if comp_choice == "paper":
            print("Computer chose paper, you lose!")
        elif comp_choice == "scissors":
            print("Computer chose scissors, you win!")
    elif user_choice == "paper":
        if comp_choice == "rock":
            print("Computer chose rock, you win!")
        elif comp_choice == "scissors":
            print("Computer chose scissors, you lose!")
    elif user_choice == "paper":
        if comp_choice == "rock":
            print("Computer chose rock, you win!")
        elif comp_choice == "scissors":
            print("Computer chose scissors, you lose!")