from dicegame import one_dice, two_dice

print("Welcome to the Dice Game!")

while True:
    try:
        user_choice = int(input("Pick your minigames!(1-2)\n1.One dice\n2.Two dices\n: "))
    except ValueError:
        print("Please use an integer!")
        continue
        
    if user_choice == 1:
        one_dice()
    elif user_choice == 2:
        two_dice()
    else:
        print("Not in an option!")
