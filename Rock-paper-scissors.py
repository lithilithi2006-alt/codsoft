import random
choices = ["rock", "paper" , "scissors"]
user_score=0
computer_score=0
while True:
    user= input("Enter rock, paper, or scissors: ").strip().lower()

    if user not in choices:
        print("Invalid choice! Please enter rock,paper, or scissors. ")
        continue
    
    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "Paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("you Win!")
        user_score+=1
        
    else:
        print("Computer Wins!")
        computer_score+=1
        

    print(f"\nScore -> You: {user_score} | computer: {computer_score}")

    while True:
        again  = input("\nplay again? (Yes/no): ").strip().lower()

        if again == "yes":
            break
        elif again == "no":
            print("\nFinal Score")
            print(f"You: {user_score} | computer:{computer_score}")
            print("Thanks for playing!")
            exit()

        else:
            print("please enter only 'yes' or 'no'.")
