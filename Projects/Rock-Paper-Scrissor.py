# Beginner Project

import random
items = ['Rock','Paper','Scissors']
while True:
  user_choice = input('Enter your move (Rock / Paper / Scissors) : ')
  comp_choice = random.choice(items)
  print(f"\nYou chose {user_choice}, computer chose {comp_choice}.\n")

  if user_choice == comp_choice:
    print(f"Both players selected {user_choice}. It's a tie!")
  elif user_choice.lower() == 'rock':
    if comp_choice == 'Scissors':
        print('Rock smashes scissors! You win!')
    else:
        print('Paper Covers rock! You lose.')
  elif user_choice.lower() == 'paper':
    if comp_choice == 'Rock':
        print('Paper Covers rock! You win!')
    else:
        print('Scissors cuts paper! You lose.')
  elif user_choice.lower() == 'scissors':
    if comp_choice == 'Paper':
        print('Scissors cuts paper! You win!')
    else:
        print('Rock smashes scissors! You lose.')
  else:
      print('Invalid input you write!')
  play_again = input("Play again? (y/n): ")
  if play_again.lower() != "y": 
     break

