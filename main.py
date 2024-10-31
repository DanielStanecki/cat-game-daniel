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
            cat_attributes["intelligence"] += 5
    elif option == "3": 
        if cat_attributes["weight"] >= 30 and cat_attributes["energy"] >= 100:
            print(f"{name} is too energetic AND needs to eat a bit less!!")
        elif cat_attributes["energy"] >= 100:
            print(f"{name} is already too energetic!!")
        elif cat_attributes["weight"] >= 30: 
            print(f"{name} needs to eat less!!")
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
    elif option == "5": 
        print(cat_attributes)
    else:
        pass

    if cat_attributes['energy'] <= 0 or cat_attributes["weight"] <= 0:
        print(f"{name} is dead due to your actions.")
        x = False 
        

    
