import random

print("7 chances to guess the number and win the game!")

lucky_number = random.randrange(100)

chances = 5

guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    user_guess = int(input('Please Guess a Number : '))

    if user_guess == lucky_number:
        print(f'You guessed {lucky_number} in {guess_counter} attempts.')
        break
    elif guess_counter >= chances and user_guess != lucky_number:
        print(f'The correct number is {lucky_number}. Better luck next time!')
        
    elif user_guess < lucky_number:
        print('Your guess is lower!')

    elif user_guess > lucky_number:
        print('Your guess is higher!')