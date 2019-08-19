from random import choice, random
from random import shuffle

# This is a good example of how to use funtion calls, and shuffling of a list

def ask_user():
    check = str(input("Would you like to randomize Owners list? (Y/N): ")).lower().strip()
    try:
        if check[0] == 'y':
            return True
        elif check[0] == 'n':
            return False
        else:
            print('Invalid Input')
            return ask_user()
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return ask_user()

owners = {"Winston": 1, "Jesse": 2, "Alfrado": 3}
order = list((owners.keys()))
if ask_user() == True:
    shuffle(order)
    print (order)
else :
    ask_user()

