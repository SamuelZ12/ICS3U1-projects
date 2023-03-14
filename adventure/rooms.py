# Leo 
import random
def shop(item, inventory, stats):
    print("Welcome to the Beast Store. (type 'leave' to leave the shop)\n")
    print('Items\n')
    for i in range(len(item)):
        print(item[i][0] + ": " + str(item[i][1]) + " gold")
    print()
    while True:
        print(f"You currently have {inventory[1]} gold")
        buy = input("What do you want to buy? Or enter [steal] to attempt to steal or [leave]: ").lower()
        if buy == 'h' and inventory[1]-10 >=0:
            stats[3] += 1
            inventory[1] -= 10
        elif buy == 's' and inventory[1]-10 >=0:
            stats[0] += 1
            inventory[1] -= 10
        elif buy == 'c' and inventory[1]-10 >=0:
            stats[1] += 1
            inventory[1] -= 10
        elif buy == 'i' and inventory[1]-10 >=0:
            stats[2] += 1
            inventory[1] -= 10
        elif buy == 'steal':
            prison(inventory, stats)
            break
        elif buy == 'sword' and inventory[1]-30 >=0:
            inventory[2] = ['sword', 30]
            inventory[1] -= 30
        elif buy == 'hp':
            inventory[1] -= 10
            inventory[3] +=1
        elif buy == 'leave':
            break
        else:
            print("That's an invalid option or insufficient gold\n")
    return (inventory, stats)

# Kevin
def dungeon(inventory, stats):
    print("You enter the dungeon, a Goblin appears to be holding something shiny.")
    print("upon closer examination, you realize its a gold key.")
    print()
    print("Goblin stats:")
    print("Health: 50")
    print("Strength: 10")
    print("Intelligence: 0")
    check = input("Do you choose to [F]ight or [R]un ").lower()
    if check == "f":
        result, inventory = fightzone(["Goblin", 50, 10, 3], stats, inventory)
        if result:
            print("The goblin ran at the fireplace thinking it was you.")
            print("It died.")
            print("You gained 20 coins")
            inventory[1] += 20
        else:
            print("You died")
    elif check =="r":
        print('You ran out of the dungeon, and found yourself in a room full of ancient books')
        library(stats)
    return (inventory,stats)

# Daniel
def prison(inventory, stats):
    print("You have committed a crime")
    print("You are now stuck in a prison cell")
    print("These is a wizard next to you selling shiny gemstones")
    print()
    convo = input("Do you engage in coversation with the wizard? [Y]es or [N]o? ").lower()
    if convo == 'n':
        print("The wizard is mad you ignored him! He decided to fight you.")
        result, inventory = fightzone(["Wizard", 100, 20, 6], stats, inventory)
        if result == True:
            print("")
            print("You beat the wizard!")
            print("You earn 20 gold!")
            inventory[1] += 20
    while True:
        if convo == 'n':
            break
        print()
        print("The Wizard notices that you are interested in his gemstones, but offers you his wand instead.")
        item = input("Do you choose to bargain for his [G]emstones or [W]and? ").lower()
        print()
        if item == 'g':
            print("The Wizard tells you that the gemstone costs 10 gold")
            gem = input("Do you want to buy the gemstone for 10 gold? [Y]es or [N]o? ").lower()
            print("")
            if gem == 'y':
                if inventory[1] >= 10 and stats[1] >= 3:
                    inventory[1] -= 10
                    print("You now own a gemstone!")
                    print("However the gemstone is explosive, the wizard tricked you")
                    print("The gemstone all of a sudden blows up and renders you unconcious")
                    print("")
                    if inventory[0] > 10:
                        inventory[0] -= 10
                        print("You wake up in a room full of ancient books")
                        convo = 'n'
                        library(stats)
                    else:
                        print("You do not have enough health to survive the explosion")
                        print("You died")
                        print("Game over")
                        break
                elif inventory[1] < 10:
                    print("You do not have enough gold!")
                elif stats[1] < 3:
                    print("You do not have enough charisma to bargain with the Wizard")
        elif item == 'w':
            print("")
            print("The wizard points the wand at you and you instantly fall asleep")
            print("You finally wake up")
            print("")
            convo = 'n'
            dungeon(inventory, stats)
    print("")

# Kevin and Samuel
def library(inventory, stats):
    print('Three books catch your eye:')
    print('A sleek gold coated cover at the top shelf')
    print('A matte black cover with a silver lining on the middle shelf')
    print('A map on the bottom shelf')
    print('Pick a book: [T]op shelf, [M]iddle shelf, or [L]ower shelf')
    o = input().lower()
    if o == "t":
        print("You read the contents of the golden book and gain 3 intelligence.")
        stats[2] += 3
    elif o == "m":
        print("You read the black book and gained 2 strength points.")
        stats[0] += 2
    elif o == "l":
        print("You found a map which tells you the location of the castle")
        print("Do you want to steal the map and store in it your inventory? [Y]es or [N]o")
        i = input().lower()
        if i == "y":
            if stats[2] >= 3:
                print("You were intelligent enough to steal the map. You have now acquired it")
                inventory[4] = True
            elif stats[2] < 3:
                print("You were too dumb to steal, you got caught, and died. Game over")
        else:
            print("You left the library without stealing anything. :O")
    return (inventory, stats)
        
# Leo
def fightzone(enemy, stats, inventory): #enemy[name, health, damage, luck]
    print(f"\nYou've entered a fight with {enemy[0]}")
    result = False
    damage = inventory[2][1] + stats[0]
    while True:
        if inventory[0] > 0 and enemy[1] > 0:
            print(f"\nYou have: {inventory[0]}/{stats[3]}HP | {inventory[3]} Healing Potion | {inventory[2]}")
            print(f"{enemy[0]} has {enemy[1]}HP")
            fightChoice = input("[A]ttack, [D]odge, [H]eal\n").lower()
            if fightChoice == 'a':
                if 1 == random.randint(1,enemy[3]):
                    print(f"You've hit a Critical Shot for {damage*2}!")
                    enemy[1] -= damage*2
                    print(f"{enemy[0]} hit you for {enemy[2]}")
                    inventory[0] -= enemy[2]
                else:
                    print(f"You hit the enemy for {damage}")
                    enemy[1] -= damage
                    print(f"{enemy[0]} hit you for {enemy[2]}")
                    inventory[0] -= enemy[2]
            elif fightChoice == 'd':
                if 1 == random.randint(1,enemy[3]):
                    print("You've dodge the shot, and healed 20 HP")
                    if inventory[0] + 20 <= stats[3]:
                        inventory[0] + 20
                    else:
                        inventory[0] = stats[3]
                else:
                    print("You've dodged too slow, and got hit")
                    inventory[0] -= enemy[2]
            elif fightChoice == 'h' and inventory[3] > 0:
                inventory[3] -= 1
                print(f"{enemy[0]} hit you for {enemy[2]}")
                inventory[0] -= enemy[2]
                print("You heal for 30 HP")
                if inventory[0] + 30 <= stats[3]:
                    inventory[0] + 30
                else:
                    inventory[0] = stats[3]
            else:
                print("Invalid Choice")
        elif enemy[1] <= 0:
            inventory[0] = stats[3]
            print("You Win!")
            result = True
            break
        else:
            inventory[0] = 0
            print("You Lose")
            result = False
            break
        
    return (result, inventory)
# stat_name = ["Strength", "Charisma", "Intelligence", "Max Health"]
# inventory = [Current HP, Gold, Weapon, HealthPotion, Map]

# Samuel
def castle(inventory, stats):
    if not inventory[4]:
        print("You must attain the secret map to find the castle!")
        return (False, inventory)
    print("You have entered the final room of the game! THE CASTLE!")
    print("To beat this game you must kill the final boss. The dragon!")
    result, new_inventory = fightzone(["Dragon", 200, 40, 8], stats, inventory)
    if result:
        print("Congrations you have accomplished an impossible feat! You defeated the Dragon!")
        return (True, new_inventory)
    else:
        print("You have failed to beat the dragon. :(")
        return (False, new_inventory)
    # return = (win/lose, inventory)