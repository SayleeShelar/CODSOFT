import random

item_list = ["Rock", "Paper", "Scissor"]

while True:
    user_choice = input("Enter your move (Rock, Paper, Scissor) or 'exit' to quit: ").capitalize()

    if user_choice == 'Exit':
        print("Thanks for playing! Goodbye.")
        break

    if user_choice not in item_list:
        print("Invalid move! Please enter Rock, Paper, or Scissor.")
        continue

    comp_choice = random.choice(item_list)

    print(f"\nUser choice = {user_choice}, Computer choice = {comp_choice}")

    if user_choice == comp_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and comp_choice == "Scissor") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissor" and comp_choice == "Paper"):
        print("You win!")
    else:
        print("Computer wins!")

