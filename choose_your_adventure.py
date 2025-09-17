name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input(
    'You are on a dirt road, it has come to an end and you can go left or right. Which way would like to go (left/right)? '
    ).strip().lower()
if answer == 'left':
    answer = input('You come to a river, you can walk aroung it or swim across? Type walk around or swim to swim across (walk/swim) ?'
                   ).strip().lower()
    if answer == 'swim':
        print('You swim acorss and were eaten by an alligator.')
    elif answer == 'walk':
        print('You walked for many miles, ran out of water and you lost the game.')
    else:
        print("Not a valid option, You lose!")

elif answer == 'right':
    answer = input('You come to a bridge, it looks woobly, do you want to cross it or head back (cross/back)? '
                   ).strip().lower()
    if answer == 'back':
        print(f"You go back and lose.")
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").strip().lower()
        if answer == 'yes':
            print('You talk to the stranger and they give you gold. You win!')
        elif answer == 'no':
            print('You ignore the strnager and they are offended and you lose!')
        else:
            print('Not a valid option. You lose!')
    else:
        print('Not a valid option. You lose!')
else:
    print(f"Not a valid option. You lose!")

print(f'Thak you for trying, {name}.')