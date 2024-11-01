cat_attributes = {
    "intelligence": 10,
    "energy": 50,
    "weight": 10,
}

print("Welcome to my cat game!!")

name = input("Please enter the name of your cat: ").title()
colour = input("Please enter the colour of the cat: ")
x = True

while x == True:
    
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. Feed your cat 4. Put your cat to sleep 5. Show cat stats ")
    if option == '1':
        if cat_attributes["energy"] <= 5:
            print(f"{name} is too tired")
        else:
            print(f"You are playing with {name}!!")
            cat_attributes["energy"] -= 5
    elif option == '2':
        if cat_attributes["energy"] <= 5:
            print(f"{name} is too tired")
        else: 
            print(f"You are training {name}!!")
            cat_attributes["energy"] -= 10
            cat_attributes["weight"] -= 2
            cat_attributes["intelligence"] += 10
    elif option == "3": 
        if cat_attributes["energy"] >= 100:
            print(f"{name} is already too energetic!!")
        else:
            print(f"You are feeding {name}!!")
            cat_attributes["energy"] += 5
            cat_attributes["weight"] += 5
    elif option == "4": 
        if cat_attributes["energy"] >= 100: 
            print(f"{name} is too energetic too sleep right now!!")
        else:
            print(f"{name} is sleeping.")
            cat_attributes["energy"] += 10
            cat_attributes["intelligence"] -= 5
    elif option == "5": 
        print(cat_attributes)
    else:
        pass

    if cat_attributes['energy'] <= 0:
        print(f"{name} is dead due to inhumane extortion over the cat, and you overworking it.")
        x = False 
    elif cat_attributes["weight"] <= 0: 
        print(f"{name} is dead due to malnourisment. You have neglected it, how dare you?")
        x= False
    elif cat_attributes["weight"] >= 40:
        print(f"{name} is dead due to excess obesity, due to you forcefeeding them.")
        x = False
    elif cat_attributes["intelligence"] <= 0:
        print(f"{name} is dead because they became so stupid that they drank a litre of perfume.")
        x = False
    elif cat_attributes["intelligence"] >= 100:
        print(f"{name} has become too smart and has taken over the world!!")
        x = False