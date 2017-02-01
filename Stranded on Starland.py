import time
global name

def start():
    alive = 1
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

def jungle():
        print("You have entered the Junge Area!") 
        time.sleep(2)
        print("You are walking down the path when there is a fork in the road, go right or go left.")
        fork = ""
        while fork!="right" and fork!="left":
            fork = input("left/right: ")
            if fork == "right":
                            print ("You head down the right path.")
                            time.sleep(5)
                            print("You have been walking for quite awhile when you get another call.")
                            time.sleep(3)
                            print("You pick up and it is Andrew on the line and he says that you are getting close to the Gem.")
                            time.sleep(2)
                            print("You hear a creepy growl from the bushes")
                            time.sleep(2)
                            print("As you aproach the bushes huge spider comes out and approaches you.")
                            time.sleep(2)
                            print("You don't have anything to defend yourself with.")
                            time.sleep(3)
                            print("The huge spider slays you.")
                            time.sleep(3)
                            print("Game Over.")
                            time.sleep(3)
                            print("The game will automatically start from where you were.")
                            time.sleep(2)
                            alive = 0
                            jungle()
                            
            if fork == "left":
                print("You walk down the left path and find a huge treehouse!")
                time.sleep(3)
                print("A little boy runs out of the treehouse and takes you inside, he says its to dangerous aroud here and you should head back")
                time.sleep(5)
                print("You explain your ship crashed and that you had to come here to get the next power gem.")
                time.sleep(3)
                print("He says that if you continue you will eventually encounter a dangerous beast.")
                time.sleep(3)
                print("You leave the house and continue at your own risk.")
                time.sleep(2)
                print("As you are walking you see a child down at the river.")
                river = ""
                while river!="check" and river!="dont" and river!="don't":
                    river = input("check/dont: ")
                    if river == "check":
                        print("You walk up to the child but it was an illusion!")
                        time.sleep(3)
                        print("The monster turns around and kills you.")
                        time.sleep(3)
                        print("Game Over.")
                        time.sleep(3)
                        print("The game will automatically start from where you were.")
                        time.sleep(2)
                        alive = 0
                        jungle()

                    else:
                        print("You continue to walk down the path.")
                        time.sleep(3)
                        print("When you reach the end of the path you see a chest.")
                        time.sleep(2)
                        print("Loot it or turn back?")
                        sword = ""
                        while sword!="loot" and sword!="turnback":
                            sword = input("loot/turnback: ")
                        if sword == "loot":
                           print("You loot the chest and hey! A sword! Could be helpful later.")
                           time.sleep(3)
                           print("You head back to the fork in the path because there is no more things to do on the left path.")
                           time.sleep(2)
                           print("You head down the right path and it looks way longer than the left.")
                           time.sleep(5)
                           print("You have been walking for quite awhile when you get another call.")
                           time.sleep(3)
                           print("You pick up and it is Andrew on the line and he says that you are getting close to the Gem.")
                           time.sleep(2)
                           print("You hear a creepy growl from the bushes")
                           time.sleep(2)
                           print("As you aproach the bushes huge spider comes out and approaches you.")
                           time.sleep(2)
                           print("Good thing you found the sword.")
                           time.sleep(2)
                           print("You slay the beast and he drops the second power gem.")
                           time.sleep(2)
                           print("Andrew says you should head back imediately. So you go as fast as you can.")
                           time.sleep(3)
                           print("Once you return to the ship you hand Andrew the power gem.")
                           time.sleep(3)
                           print("He explains that this is the Engine Gem and that it is one of the more important power gems.")
                           time.sleep(2)
                           print("A new area has appeared on your map!")
                           time.sleep(3)
                           print("Ok " +name+ "head out as soon as you can after you get some sleep.")
                           Snow()


                           if sword == "turnback":
                               print("It was probably a trap anyway.")
                               time.sleep(3)
                               print("You head back to the fork in the road because there is no more things to do on the left path.")
                               time.sleep(2)
                               print("You head down the right path and it looks way longer than the left.")
                               time.sleep(5)
                               print("You have been walking for quite awhile when you get another call.")
                               time.sleep(3)
                               print("You pick up and it is Andrew on the line and he says that you are getting close to the Gem.")
                               time.sleep(2)
                               print("You hear a creepy growl from the bushes.")
                               time.sleep(2)
                               print("As you aproach the bushes huge spider comes out and approaches you.")
                               time.sleep(2)
                               print("You don't have anything to defend yourself with.")
                               time.sleep(3)
                               print("The huge spider slays you.")
                               time.sleep(3)
                               print("Game Over.")
                               time.sleep(3)
                               print("The game will automatically start from where you were.")
                               time.sleep(2)
                               alive = 0
                               jungle()

def snow()
    print("You have entered the Snow Area!")
    time.sleep(2)
    print("Its exremely cold here! Get some protection soon!")
    time.sleep(3)
    print("When you enter you see a huge igloo.")
    igloo = ""
    while igloo!="enter" and igloo!="ignore:
        igloo = input("enter/ignore: ")
        
        if igloo = "ignore":
            print("You make it a bit but die of frostbite.")
            time.sleep(3)
            print("Game Over.")
            time.sleep(3)
            print("The game will automatically start from where you were.")
            time.sleep(3)
            alive = 0
            snow()
            
        if igloo == "enter":
            print("You enter the igloo to see a... bar full of polar bears?")
            time.sleep(2)
            print("You are greeted by one of the bears and you tell him your ship crashed and you are trying to repair your ship.")
            time.sleep(3)
            print("He gives you a fur coat to pretect yourself in the cold! Could come handy later.")
            time.sleep(2)
            print("When you start walking down the path and not freezing you meet a strange penguin.")
            time.sleep(3)
            print("He tells you you need to find a cave and he saw some one take a mysterious gem.")
            time.sleep(2)
            print("When you continue walking you see a cave with somehing glowing inside.")
            cave = ""
            while cave!="enter" and cave!="keepwalking":
                cave = input("enter/keepwalking: ")

                if cave == "keepwalking":
                    print("You make it a bi but a snowleopard smells the pelt and kills you")
                    time.sleep(3)
                    print("Game Over.")
                    time.sleep(3)
                    print("The game will automatically start from where you were.")
                    time.sleep(3)
                    alive = 0
                    snow()
                    
                if cave == "enter":
                    print("You enter the cave and see an old man sitting in a chair holding something.")
                    time.sleep(3)
                    print("He sees you have come in without asking.")
                    time.sleep(2)
                    print("He turns out to be a nice friendly guy who lets you have some food. You ask him if he has seen anythin and he says that he has heard nothing")
                    time.sleep(4)
                    print("When you leave he tells you directions to the right cave you follow his directions and he leads you right to it.")
                    time.sleep(3)
                    print("You hear dripping noises from the cave you turn around the corner and... its an evil snowman? tanning? SO MANY PLOT TWISTS.")
                    time.sleep(3)
                    print("He pulls out his shurikins and starts to run at you. NEVER INTERUPT A SNOWMAN TANNING... super awkward.")
                    time.sleep(3)
                    print("You pull out your sword and don't know what to do.")
                    snowman = ""
                    while snowman!="fight" and snowman!="run":
                        snowman = input("fight/run: ")
                        
                        
                    
    
    
start()
