from rooms import* 

def main():
    #Samuel
    stats = [0, 0, 0, 50]
    stat_name = ["Strength", "Charisma", "Intelligence", "Max Health"]
    inventory_name = ["Current HP", "Gold", "Weapon", "HealthPotion", "Map"]
    inventory = [50, 50, ["stick", 5], 0, False] 
    shopItem = [["[sword]", 30], ["[HP]Heal Potion",10], ["[H]Increase Max Health Points", 10], ["[S]Strength Points", 10], ["[C]Charisma Points", 10], ["[I]Intelligence Points", 10]]
    
    name = input("What is your name? ")
    print()
    trait_points = 5
    
    print("Split your trait points between the below traits. Choose wisely!")
    print("Traits: Strength, Charisma, Intelligence")
    
    while True: #Daniel
        print(f"{trait_points} Trait Points remaining")
        stats[0] = int(input("Strength: ")) 
        while stats[0] > trait_points:
            stats[0] = int(input("Invalid. Strength: "))
        trait_points -= stats[0]
        print(f"{trait_points} Trait Points remaining")
        stats[1] = int(input("Charisma: ")) 
        while stats[1] > trait_points:
            stats[1] = int(input("Invalid. Charisma: "))
        trait_points -= stats[1]
        print(f"{trait_points} Trait Points remaining")
        stats[2] = int(input("Intelligence: "))
        while stats[2] > trait_points:
            stats[2] = int(input("Invalid. Intelligence: "))
        print("")
        print("Do you confirm your traits?")
        Confirm = input("[Y]es or [N]o? ").lower()
        if Confirm == "y":
            print()
            break
        else:
            trait_points = 5
            print()
    
    # Samuel
    while True:
        print("Welcome to Adventure, " + name)
        print("Where do you want to go?")
        print("Options:")
        print()
        print("- [S]hop")
        print("- [D]ungeon")
        print("- [I]nventory")
        print("- [C]astle")
        print("- [L]ibrary")
        print("- [P]rison")
        o = input().lower()
        if o == "s":
            inventory, stats = shop(shopItem, inventory, stats)
            
        elif o == "i":
            print("Your current stats:")
            for i in range(len(stats)):
                print(f"{stat_name[i]}: {stats[i]}")
            for i in range(len(inventory)):
                print(f"{inventory_name[i]}: {inventory[i]}")
    
        elif o == "d":
            dungeon(inventory, stats)
    
        elif o == "c":
            result, new_inventory = castle(inventory, stats)
            if result:
                print("You have beat the game. Here is your prize: ")
                trophy_art = """
                ___________
                '._==_==_=_.'
                .-\:      /-.
               | (|:.     |) |
                '-|:.     |-'
                  \::.    /
                   '::. .'
                     ) (
                   _.' '._
                   '''''''
                """
                print(trophy_art)
                break

        elif o == 'l':
            inventory, stats = library(inventory, stats)

        elif o == 'p':
            prison(inventory, stats)

if __name__ == "__main__":
    main()