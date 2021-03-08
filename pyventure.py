# a very brief text adventure, with easter eggs for my wife, like milking the monster.
from sys import exit
startofgame = True
inventory = []
def charmaker():
    print("What's your name?")
    name = input("> ")
    return name
def cockpit(charName, firsttime):
    print(f"You sit in your cockpit, aboard the starship Everess, as it comes out of hyperspace.  You take a second to remember your bearings.  You are {charName}, esteemed captain of the Everess, not that anyone really reports to you, since you are a lone mercenary, sailing the black winds of space, pinpricks of starlight on the horizon.  In the cockpit you see your laser pistol, water bottle, snack stash, Oxygen rebreather, the picture of Becky (your long ago love that you bought the Everess to impress before she.... well... better to focus on you for now....) and emergency flashlight. \n Red lights begin to blink across the console of your ship.  You see your engines begin to fail, oxygen levels dropping, and just before the screen goes blank, you see the characters 'INTRU' crawl across the screen. ")
    print(f"now is the time for action.")
    print(f"What do you do?")
    while(True):
        choice= input("> ")
        if "leave" in choice:
            print("you go into the hallway")
            hallway(charName)
        elif "take" in choice:
            if "laser" in choice or "pistol" in choice:
                print("You pick up the laser pistol")
                inventory.append("Laser Pistol")
            if "oxygen" in choice:
                print("You pick up the Oxygen rebreather")
                inventory.append("Oxygen Rebreather")
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
def cargoHold(charName):
    print("You arrive in the cargo hold.")
def medbay(charName):
    print("You arrive in the medbay.")
def escapeHatch(charName):
    print("You arrive in the escape hatch.")
    dead("There isn't air in the escape hatch", charName)
def janitorCloset(charName):
    print("You arrive in the Janitor's closet")
def dead(why,charName):
    print(why, f"  Nice going, but {charName}'s dead!")
    print("GAME OVER")
    exit(0)
def get_inventory():
    print("listing inventory")
    print(inventory)

def help():
    print("If you are given a list of numbers, type in a number to make a choice.  Otherwise, use simple commands like take flashlight, leave cockpit, open door etc. use capital letters to access 'Out of character' functions like HELP or INVentory")
    return
def game():
    print("Game start!")
    charname = charmaker()
    cockpit(charname,startofgame)
    exit(0)

game()
