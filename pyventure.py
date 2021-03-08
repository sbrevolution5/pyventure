# a space based text adventure
from sys import exit
startofgame = True
inventory = []
equipped = ["clothes"]
def charmaker():
    print("What's your name?")
    name = input("> ")
    return name
def cockpit(charname, firsttime):
    print(f"You sit in your cockpit, aboard the starship Everess, as it comes out of hyperspace.  You take a second to remember your bearings.  You are {charname}, esteemed captain of the Everess, not that anyone really reports to you, since you are a lone mercenary, sailing the black winds of space, pinpricks of starlight on the horizon.  In the cockpit you see your laser pistol, water bottle, snack stash, Oxygen rebreather, the picture of Becky (your long ago love that you bought the Everess to impress before she.... well... better to focus on you for now....) and emergency flashlight. \n Red lights begin to blink across the console of your ship.  You see your engines begin to fail, oxygen levels dropping, and just before the screen goes blank, you see the characters 'INTRU' crawl across the screen. ")
    print(f"now is the time for action.")
    whatdo(charname, "cockpit")

def hallway(charName):
    print(f"As {charName}, who is you just in case you forgot, enters the hallway, you remember the general layout.  You can go to the following locations: \n\t(1) Cockpit\n\t(2) Mess Hall\n\t(3) Armory\n\t(4) Airlock \n\t(5) Medbay\n\t(6) Cargo Hold\n\t(7) Escape Hatch\n\t(8) Janitor Closet")
    print("Which do you choose?")
    while(True):
        choice = input("> ")
        if "1" in choice:
            print("You are headed to the cockpit")
            cockpit(charName)
            return
        if "2" in choice:
            print("You are headed to the Mess Hall")
            messHall(charName)
            return
        if "3" in choice:
            print("You are headed to the Armory")
            armory(charName)
            return
        if "4" in choice:
            print("You are headed to the airlock")
            airlock(charName)
            return
        if "5" in choice:
            print("You are headed to the medbay")
            medbay(charName)
            return
        if "6" in choice:
            print("You are headed to the cargo hold")
            cargoHold(charName)
            return
        if "7" in choice:
            print("You are headed to the escape hatch")
            escapeHatch(charName)
            return
        if "8" in choice:
            print("You are headed to the Janitor Closet")
            janitorCloset(charName)
            return
        print("please enter a proper response!")
def messHall(charName):
    print("You arrive in the mess hall.")
def armory(charName):
    print("You arrive in the Armory.")
def airlock(charName):
    print("You arrive in the airlock.")
    if "oxygen rebreather" not in equipped:
        dead("You can't breathe outside the ship without your oxygen rebreather, you have suffocated!", charName)
    else:
        print("As you push out of the airlock you breathe a sigh of relief that you can breathe through your oxygen rebreather.")
        
def cargoHold(charName):
    print("You arrive in the cargo hold.")
def medbay(charName):
    print("You arrive in the medbay.")
def escapeHatch(charName):
    print("You arrive in the escape hatch.")
    dead("There isn't air in the escape hatch", charName)
def janitorCloset(charName):
    print("You arrive in the Janitor's closet")

# command functions -----------------
def equip(item, choice, itemalt=None):
    if item in choice or itemalt in choice:
        if item not in equipped:
            if item in inventory:
                print(f"You have attached your {item} to your helmet, you can now breathe easily")
                return
            else:
                print(f"You don't have {item}")
                return
        else:
            print(f"You have {item} equipped, use 'unequip' to return to inventory")
            return

def unequip(item, choice, itemalt=None):
    if item in choice or itemalt in choice:
        if item in equipped:
            print(f"You have returned your {item} to your inventory")
            return
        else:
            print(f"You don't have {item} equipped, use 'equip' to retrieve from inventory")
            return
# Utility functions ____________
def whatdo(charname, roomname):
    print(f"What do you do?")
    while(True):
        choice= input("> ")
        if "leave" in choice:
            print("you go into the hallway")
            hallway(charname)
        elif "EXIT" in choice or "QUIT" in choice:
            quitter()
        elif "equip" in choice:
            if "oxygen" in choice or "rebreather" in choice:
                if "oxygen rebreather" not in equipped:
                    if "oxygen rebreather" in inventory:
                        print("You have attached your oxygen rebreather to your helmet, you can now breathe easily")
                    else:
                        print("You don't have an oxygen rebreather")
                else:
                    print("You have the rebreather equipped, use 'unequip' to return to inventory")

        elif "take" in choice:
            if "laser" in choice or "pistol" in choice:
                print("You pick up the laser pistol")
                inventory.append("Laser Pistol")
            if "oxygen" in choice:
                print("You pick up the Oxygen rebreather")
                inventory.append("oxygen rebreather")
            if "snack" in choice:
                print("You pick up the Snacks")
                inventory.append("Snack")

            if "picture" in choice:
                print("You pick up the picture of Becky")
                inventory.append("Becky's Picture")

            if "flashlight" in choice:
                print("You pick up the emergency flashlight, only to find that it isn't working, batteries must be dead...  You remember that there were some battery powered toys in the cargo bay, but without the computer it will be tough to sort through the inventory.")
                inventory.append("dead flashlight")

            if "water" in choice:
                print("You pick up the water bottle")
                inventory.append("water bottle")
        elif "HELP" in choice:
            help()
        elif "INV" in choice:
            get_inventory()
        else:
            print("Please input a valid action, type HELP for some examples")

def dead(why,charName):
    print(why, f"  Nice going, but {charName}'s dead!")
    print("GAME OVER")
    exit(0)
def get_inventory():
    print("listing inventory")
    print(inventory)
def get_equip():
    print("Your equipment")
    print(equipped)
def help():
    print("If you are given a list of numbers, type in a number to make a choice.  Otherwise, use simple verb-noun commands like 'take flashlight', 'leave cockpit', 'open door' etc. use capital letters to access 'Out of character' functions like HELP, EXIT or INVentory")
    return
def quitter():
    print("are you sure you want to quit?  y/n")
    while(True):
        quitting = input("> ")
        if "y" in quitting:
            print("goodbye!")
            exit()
        elif "n" in quitting:
            return
def game():
    print("Game start!")
    charname = charmaker()
    cockpit(charname,startofgame)
    exit(0)

game()
