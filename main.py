cat_attributes = {
    "intelligence": 10,
    "energy": 50,
    "weight": 30,
    # change the inital values above
}

print("Welcome to my cat game!!")

# Take the user inputs for name and colour:
name = input("Please enter the name of your cat: ")
colour = input("Please enter the colour of the cat: ")
x = True
# start the while loop
while x == True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. show stats ")
    if option == '1':
        print("You are playing with your cat!!")
        cat_attributes["energy"] -= 5
        pass
    elif option == '2':
        print("You are training your cat!!")
        cat_attributes["energy"] -= 10
        cat_attributes["weight"] -= 5
        cat_attributes["intelligence"] += 5
    elif option == "3": 
        print(cat_attributes)
    else:
        pass

    # finish off the if statements below
    if cat_attributes['energy'] < 0 or cat_attributes["weight"] < 0:
        print("The cat is dead due to your actions.")
        x = False 
        pass
    # elif ...
    
