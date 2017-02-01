import time
import os
global name
def clear():
    os.system("clear")
    os.system("cls")
def start():
    print("Hello! to start this game we need to know your name.")
    time.sleep(3)
    name = input("What's your name?")
    print("Alright "+name+" have a good time!")
    time.sleep(3)
    print("Welcome to the to the SS Penguin, a ship made to orbit the planet of Starland....")
    time.sleep(2)
    print("Unlike other ships this ship runs on power gems instead of fuel...")
    time.sleep(3)
    print("Hey! Hey "+name+" wake up! It's your friend Andrew, your friend from 1st grade.")
    time.sleep(4)
    print("It's the big day! The day you get to finally work on the SS Penguin! I see you left the T.V. on getting ready for today.")
    time.sleep(5)
    print("Let's go already!")
    time.sleep(4)
    print("25 years later.....")
    time.sleep(2)
    phone = ""
    while phone!="yes":        
        print("Brrring... Brrring..")
        time.sleep(2)
        print("Your phone rings in your pocket. Answer the call?")
        phone = input("yes/no: ")
    if phone == "yes":
        print("You pick up your phone and its your friend in the control room.")
        time.sleep(2)
        print(""+name+" GET DOWN HERE WE ARE GONNA CRASH!!!!!!!!!")
        time.sleep(2)
        print("You rush down but its too late.")
        time.sleep(3)
        print("You hear on the comms, BRACE FOR IMPACT!!")
        time.sleep(5)
        print("BAAAANNNG")
        time.sleep(3)
        print("You wake up and you don't know what has happened you don't see anyone except your friend on the floor.")
        time.sleep(3)
        print("You shake him up and it takes awhile but he finally wakes up.")
        time.sleep(2)
        print("You and your friend try to escape the control room but the exit is blocked off.")
        time.sleep(3)
        print("You decide to search the control room for any power gems...")
        time.sleep(6)
        print("Hey!! You find the Fixer Gem! This gem makes the ship indestructible but it only works when you are in orbit.")
        time.sleep(2)
        print("but it was also designed to fix the ship if it ever crashed.")
        time.sleep(2)
        print("Andrew puts in in the control panel and it boots the ship right up.")
        time.sleep(2)
        print("As the ship reboots a part of the map glows up.")
        time.sleep(3)
        print("Andrew points out it is another power Gem and that you should head out to find it as soon as possible.")
        time.sleep(6)
        jungle()

def jungle()
        print("A man greets you from a little hut, he says that it is a bad idea because there are many dangerous animals in the jungle but you continue at your own risk")
        time.sleep(2)
        print("You are walking down the path when there is a fork in the road, go right or go left.")
        fork = ""
        while fork!="right" and fork!="left"
    

        
while 1:
    clear()
    whattodo=''
    while whattodo!='p' and whattodo!='e':
        print("Welcome to Stranded on Starland!")
        print("Type p to play")
        print("Type e to exit")
        whattodo=input()
        clear()
    if whattodo=='p':
        start()
    else:
        exit()
    
