import random

dice = [1, 2, 3, 4, 5, 6]
result = 0
print('Welcome to the dices game!')
while 1:
    number_dices = input('Enter the number of dices you want to roll: ')
    if number_dices.isdigit() and (1 <= int(number_dices) <= 8):
        number_dices = int(number_dices)
        if number_dices == 1:
            dice_value = random.choice(dice)
            print('RESULT: ' + str(dice_value))
        elif number_dices > 1:
            for i in range(0, number_dices):
                dice_value = random.randrange(1, 7)
                result = result + dice_value
                print('Dice ' + str(i+1) + ': ' + str(dice_value))
            print('==========')
            print('RESULT: ' + str(result))
            print('==========')
    else:
        print('USAGE: The number must be between 1 and 8')
        continue
    break
