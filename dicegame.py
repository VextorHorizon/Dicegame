import random as rd

def one_dice():
    while True:
        try:
            user_number = int(input("Guess number between 1-6: "))

        except ValueError:
            print("Please use an integer!")
            continue

        random_number = rd.randint(1,6)

        if user_number > 6:
            print("Your number is beyond the reach!")
            continue

        elif user_number == random_number:
            print(f"Correct! the number was {random_number}!")
            correct_one_dice = input("Do you want to continue?(y/n): ")
            if correct_one_dice == 'y':
                continue
            elif correct_one_dice == 'n':
                break
            


        else:
            print(f"Incorrect! the number was {random_number}")

            user_choice = input("Do you want to continue?(y/n): ")
            if user_choice == 'y':
                continue
            elif user_choice == 'n':
                break
        

def two_dice():
    while True:
        try:
            user_number = int(input("Guess number between 2-12: "))
        except ValueError:
            print("Please use an integer!")
            continue

        random_number1 = rd.randint(1,6)
        random_number2 = rd.randint(1,6)
        random_number = random_number1 + random_number2

        '''
        I don't think you need to do this 
        You can just do random_number = rd.randint(2,12) XD
        '''


        if user_number > 12:
            print("Your number is beyond the reach!")
            continue

        elif user_number == random_number:
            print(f"Correct! the number was {random_number}!")
            correct_two_dice = input("Do you want to continue?(y/n): ")
            if correct_two_dice == 'y':
                continue
            elif correct_two_dice == 'n':
                break

        else:
            print(f"Incorrect! the number was {random_number}")

            user_choice = input("Do you want to continue?(y/n): ")
            if user_choice == 'y':
                continue
            elif user_choice == 'n':
                break
        