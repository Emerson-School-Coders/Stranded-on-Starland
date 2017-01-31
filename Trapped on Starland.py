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
    print("Hey! Hey "+name+" wake up!")
    time.sleep(2)
    print("It's the big day! The day you get to finally work on the SS Penguin! I see you left the T.V. on getting ready for today.")
    time.sleep(2)
    print("Let's go already!")
    time.sleep(2)
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
        time.sleep(2)
        print("You hear on the comms, BRACE FOR IMPACT!!")
        time.sleep(1)
        print("BAAAANNNG")
        time.sleep(3)
        print("You wake up and you don't know what has happened you don't see anyone except your friend on the floor.")
        sleep(3)
        print("You shake him up and it takes awhile but he finally wakes up.")

        
        
        

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
    
