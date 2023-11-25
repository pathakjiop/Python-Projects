from random import randint

# Start the program with basic setup
lower_num, upper_num = 1, 10

random_number: int = randint(lower_num, upper_num)
print(f'\n\t\t\t\t\t\t\tGuess the number in the range from {lower_num} to {upper_num}.')

#Attempts to guess the number is 5
max_attempts = 5
attempts =0
# Run loop for 5 times the game 
while attempts < max_attempts:
    
# making sure the number of attempts is at least one   
    attempts += 1
    # Get the user guess
    
    try:
        user_guess: int = int(input(f'Attempt {attempts} Guess: '))
    except ValueError as a:
        print('Please enter a valid number.')
        continue

    # Check the user guess
    if user_guess > random_number:
        print('The number is lower')
    elif user_guess < random_number:
        print('The number is higher')
    else:
        print('You guessed it!')
        break
 

if attempts == max_attempts:
    print(f'Sorry, you could not guess the number in {max_attempts} attempts. The correct number was {random_number}.')