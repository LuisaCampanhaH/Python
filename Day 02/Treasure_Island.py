print("Welcome to Treasure Island\n" + "Your misson is to find the treasure\n")
choise1 = input("You're at a cross road.Where do you want to go?\n" + " Type left or right: ")
if choise1 == "left":
    print("You come to a lake. There is an island in the midle of the lake.")
    choise2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across: ")
    if choise2 == "swim":
        print("Game Over")
    else: 
        print("You arrive at the island unharmed. Ther is a house with 3 doors")
        choise3 = input("One red, one yellow and one blue. Which colour do you choose? ")
        if choise3 == "yellow": 
            print("You Win!")
        else: print("Game Over")
else: print("Game over")