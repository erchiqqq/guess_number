import random
print('Welcome to the number guessing game!')
new_game = 'yes'
def is_valid(stroka):
    if stroka.isdigit() and 1 <= int(stroka) <= top_granica:
        return True
    else:
        return False

while new_game == 'yes':
    top_granica = int(input('Enter the maximum number we can guess: '))
    num = random.randint(1, top_granica)
    popitki = 0
    flag = False
    while flag == False:
        x = input(f'Write a number from 1 to {top_granica}: ')
        if is_valid(x):
            x = int(x)
            popitki += 1
            if x < num:
                print('Your number is LESS than the hidden number, try again')
            elif x > num:
                print('Your number is MORE than the hidden number, try again')
            elif x == num:
                print('You guessed it, congratulations!!!')
                print(f'There were {popitki} attempts')
                flag = True
        else:
            print(f'Or maybe we’ll still enter an integer from 1 to {top_granica}?')
    print('If you want to play again write "yes"')
    new_game = input('Want to play more?: ')
print('Thanks for playing the number guessing game. See you again!')
