# a space based text adventure
from sys import exit
import shipareas
from shipflavortext import *
startofgame = True
inventory = []
equipped = ["clothes"]
power = False #determines whether power is on or off.  
alienHealth = 5 # Health of alien, if 0, alien is dead
playerHealth = 1 # You aren't armored
playerAmmo = 0
maintenanceDoorOpen = False
ipawed_playing = None
def charmaker():
    print("What's your name?")
    name = input("> ")
    return name
def cockpit(charname, firsttime):
    print(opening_text1, charname, opening_text2)
    print(f"now is the time for action.")
    whatdo(charname, "cockpit")

def hallway(charName):
    print(hall_text1, charName, hall_text2)
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
            print("You are headed to the maintenance area ")
            maintenence(charName)
            return
        if "9" in choice:
            print("You are headed to the engine room ")
            engines(charName)
            return
        print("please enter a proper response!")
def messHall(charName):
    print("You arrive in the mess hall.")
    print(mess_hall_1)
    whatdo(charName, "messHall")
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
    print(cargo_text)
def medbay(charName):
    print("You arrive in the medbay.")
def escapeHatch(charName):
    print("You arrive in the escape hatch.")
    dead("There isn't air in the escape hatch", charName)
def maintenence(charname):
    if power:
        print(maintenence_power)
        whatdo(charname, "Maintenance")
    if not power:
        print(maintenence_no_power)
def engines(charname):
    print("You arrive in the engine room")
# command functions -----------------
def equip(item, choice, itemalt=None):
    if item in choice or itemalt in choice:
        if item not in equipped:
            if item in inventory:
                print(f"You have equipped {item}")
                if item == "laser pistol":
                    playerAmmo = 2
                    print(f"Your gun has {playerAmmo} shots remaining, ")
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
            return
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

        
        if "open door" in choice and roomname == "Maintenance" and maintenanceDoorOpen == False:
            print(maintenence_door_powerless)
            maintenanceDoorOpen = True
            whatdo(charname, "Maintenance")
        elif "HELP" in choice:
            help()
        elif "INV" in choice:
            get_inventory()
        else:
            # possible room specific command, or it doesn't return any of those?
            # do with if switch statement.
            if roomname=="cockpit":
                do_cockpit(choice)
            else:
                print("Please input a valid action, type HELP for some examples")
def do_cockpit(choice):
    if "take" in choice:
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
    else:
        print("Please input a valid action, type HELP for some examples")
def do_mess(choice):
    if "use ipawed" in choice:
        print(ipawed_text_init)
        pawed_chooser()
    else:
        print("Please input a valid action, type HELP for some examples")
def pawed_chooser():
    while(True):
        choice= input("> ")
        if '1' in choice:
            print("You play some dubstep, which you can't resist.....dancing to, at least it feels like its supposed to be dancing, which you continue until the ....music (?) stops")
            ipawed_playing = None
            return
        if '2' in choice:
            print("You hear an awful screeching noise that begins to sound harmonious, but across the ship you hear a scream of terror from something, somehow more awful than the noises coming from the iPawed")
            ipawed_playing = "Screechy"
            return
        if '3' in choice:
            print("Sir Thomas Whittleby's voice comes over the speakers, telling you of the life and times of Charles Dickens.")
            ipawed_playing = "Dickens"
            return
        if '0' in choice:
            print("You play nothing and step away")
            return
        else:
            print("please input a valid choice(0 will cancel choosing")
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
