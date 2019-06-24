import random

player_name = input('Hello, what is your name? \n')
while 1:
    number = random.randrange(101)
    # number = 23
    # computer will chose the number between 0 n 100 and let the user guess for that number
    print('Well ' + player_name + ', try to guess the number I have in mind!')
    guess_time = 0
    while 1:
        guess_time += 1
        guess_number = int(input())
        if number < guess_number:
            print('Too high, try again!')
            continue
        elif number > guess_number:
            print('Too low, try again!')
            continue
        else:
            if guess_time == 1:
                print('You won in 1 turn only, that’s amazing!')
            else:
                print('It took you ' + str(guess_time) + ' turns to guess my number which was ' + str(number) + '!')
            # return_condition = 1
            break
    while 1:
        play_again = input('Do you want to play again? [Y/N] \n')
        if play_again == 'Y':
            break
            # break out this loop and start the game again
        elif play_again == 'N':
            print('Ok, bye ' + player_name + '! See you later!')
            exit()
            # this function will quit the program immediately
        else:
            print('Sorry, I did not understand. Let me repeat:')
            continue
            # go to this loop again and for the right input
