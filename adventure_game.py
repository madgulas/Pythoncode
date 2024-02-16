name = input( "Type your name: ")
print("Welcome" +" " + name + " " + "to this Amazing Adventure Journey")


answer = input( "You have two options in front of you turn left or right ").lower()

if answer == "left":
    answer = input("You have come to a river and you can walk around it or swim accross, Type your answer either swim and walk ").lower()
    
    if answer == "swim":
        print("You swam across and were eaten by a crocodile.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print('Not a valid option. You lose')

elif answer == "right":
    answer = input("You have come across a Mountain you can either climb it or go around it, Type (climb or around) ").lower()
        
    if answer == "climb":
        print("You climbed and missed your footing and died due to fall")
    
    elif answer == "around":
        print("You walked around the mountain, Found a person how helped you come back to civilization. You Won!")
    else:
        print('Not a valid option. You lose')

else:
    print('Not a valid option. You lose')