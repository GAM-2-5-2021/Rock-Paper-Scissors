import random

print('Welcome to the Rock, Paper, Scissors game!')
print()
print('Winning Rules: \n'
      'Rock vs paper -> paper wins \n'
      'Rock vs scissor -> rock wins \n'
      'Paper vs scissors -> scissors win \n')
input('Press Enter to start. ')

your_score = 0
comp_score = 0

while True:
    print()
    your_choice = input('Rock, paper or scissors? ').lower()
    while your_choice != 'rock' and your_choice != 'paper' and your_choice != 'scissors':
        your_choice = input('Invalid input, try again: ').lower()

    random_num = random.randint(0, 2)
    if random_num == 0:
        comp_choice = 'rock'
    elif random_num == 1:
        comp_choice = 'paper'
    elif random_num == 2:
        comp_choice = 'scissors'

    print()
    print('Your choice:', your_choice)
    print("Computer's choice:", comp_choice)
    print()

    if your_choice == 'rock':
        if comp_choice == 'rock':
            print("It's a tie!")
        elif comp_choice == 'paper':
            print('You lose!')
            comp_score += 1
        elif comp_choice == 'scissors':
            print('You win!')
            your_score += 1
    elif your_choice == 'paper':
        if comp_choice == 'rock':
            print('You win!')
            your_score += 1
        elif comp_choice == 'paper':
            print("It's a tie!")
        elif comp_choice == 'scissors':
            print('You lose!')
            comp_score += 1
    elif your_choice == 'scissors':
        if comp_choice == 'rock':
            print('You lose!')
            comp_score += 1
        elif comp_choice == 'paper':
            print('You win!')
            your_score += 1
        elif comp_choice == 'scissors':
            print("It's a tie")

    print('You have', your_score, 'wins')
    print('The computer has', comp_score, 'wins')
    print()

    play_again = input('Play again? (Y/N) ').lower()
    while play_again != 'n' and play_again != 'y':
        play_again = input('Invalid input, try again: ').lower()

    if play_again == 'n':
        break

    print('\n ............. \n')
