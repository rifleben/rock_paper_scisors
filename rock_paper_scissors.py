import random
rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


hands = [rock, paper, scissors]
user_hand = int(input("Please enter 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if user_hand != 1 or user_hand != 2 or user_hand != 0:
    print("You typed an invalid number")
else:
    print('User chose: \n', hands[user_hand])
    computer_hand = random.randint(0, 2)
    print("Computer chose: \n", hands[computer_hand])

    if user_hand == 0 and computer_hand == 2:
        print('You win!')
    elif computer_hand == 0 and user_hand == 2:
        print("You loose")
    elif computer_hand > user_hand:
        print("You loose!")
    elif user_hand > computer_hand:
        print("You win")
    elif computer_hand == user_hand:
        print("Draw")