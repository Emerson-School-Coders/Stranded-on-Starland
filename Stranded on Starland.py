import time
import os
global name
def clear():
    os.system("clear")
    os.system("cls")
def start():
    alive = 1
    print("Hello! to start this game we need to know your name.")
    time.sleep(1)
    name = input("What's your name?")
    print("Alright "+name+" have a good time!")
    time.sleep(3)
    print("Welcome to the SS Dolphin, a ship made to orbit the planet of Starland....")
    time.sleep(2)
    print("Unlike other ships this ship runs on power gems instead of fuel...")
    time.sleep(3)
    print("Hey! Hey "+name+" wake up! It's your friend Andrew, your friend from 1st grade.")
    time.sleep(4)
    print("It's the big day! The day you get to finally work on the SS Dolphin! I see you left the T.V. on getting ready for today.")
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
        print("Hey!! You find the FIXER GEM! This gem makes the ship indestructible but it only works when you are in orbit.")
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
        print("You have entered the Jungle Area!") 
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
                print("A little boy runs out of the treehouse and takes you inside, he says its to dangerous around here and you should head back")
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
                           print("Its the ENGINE GEM!")
                           time.sleep(2)
                           print("Andrew says you should head back immediately. So you go as fast as you can.")
                           time.sleep(3)
                           print("Once you return to the ship you hand Andrew the power gem.")
                           time.sleep(3)
                           print("A new area has appeared on your map!")
                           time.sleep(3)
                           print("Okay, head out as soon as you can after you get some sleep.")
                           time.sleep(3)
                           snow()


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

def snow():
    print("You have entered the Snow Area!")
    time.sleep(2)
    print("Its extremely cold here! Get some protection soon!")
    time.sleep(3)
    print("When you enter you see a huge igloo.")
    igloo = ""
    while igloo!="enter" and igloo!="ignore":
        igloo = input("enter/ignore: ")
        
        if igloo == "ignore":
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
            print("He tells you you need to find a cave and he saw someone take a mysterious gem.")
            time.sleep(2)
            print("When you continue walking you see a cave with somehing glowing inside.")
            cave = ""
            while cave!="enter" and cave!="keepwalking":
                cave = input("enter/keepwalking: ")

                if cave == "keepwalking":
                    print("You make it awhile but a snowleopard smells the pelt and kills you")
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
                    print("He turns out to be a nice friendly guy who lets you have some food. You ask him if he has seen anything and he says that he has heard nothing")
                    time.sleep(4)
                    print("When you leave he tells you directions to the right cave you follow his directions and he leads you right to it.")
                    time.sleep(3)
                    print("You hear dripping noises from the cave you turn around the corner and... its an evil snowman? tanning? SO MANY PLOT TWISTS.")
                    time.sleep(3)
                    print("He pulls out his shurikins and starts to run at you. NEVER INTERRUPT A SNOWMAN TANNING... super awkward.")
                    time.sleep(3)
                    print("You pull out your sword and don't know what to do.")
                    snowman = ""
                    while snowman!="fight" and snowman!="run":
                        snowman = input("fight/run: ")

                        if snowman == "run":
                            print("You manage to get out of the cave but his guards catch you and kill you.")
                            time.sleep(3)
                            print("Game Over.")
                            time.sleep(3)
                            print("The game will automatically start from where you were.")
                            time.sleep(3)
                            alive = 0
                            snow()

                        if snowman == "fight":
                            print("Its a long fight but eventually he runs out of shurikins and you charge him.")
                            time.sleep(3)
                            print("He runs away and drops the next gem!")
                            time.sleep(2)
                            print("Its the WING GEM!")
                            time.sleep(2)
                            print("Andrew calls, and wants you back as soon as you can.")
                            time.sleep(3)
                            print("He puts it back into the control panel.")
                            time.sleep(3)
                            print("A new area has appeared on your map!")
                            time.sleep(3)
                            print("Okay, head out as soon as you can after you get some sleep.")
                            time.sleep(3)
                            swamp()
                            
def swamp():
    print("Welcome to the Swamp Area!")
    time.sleep(3)
    print("You walk through the mushy brush and leaves.")
    time.sleep(3)
    print("You see an alligator in the water.")
    alligator = ""
    while alligator!="fight" and alligator!="run":
        alligator = input("fight/run: ")

    if alligator == "fight":
        print("You walk up to the creature he turns aroud and grabs your leg.")
        time.sleep(2)
        print("You make it away but the pain is to excruciating and you faint.")
        time.sleep(3)
        print("A man finds you and he knows magic.")
        time.sleep(2)
        print("He heals your leg, what a nice guy!")
        time.sleep(2)
        print("When he takes you back to his hut you see a cage in the back")
        time.sleep(2)
        print("Very suspicious.")
        cage = ""
        while cage!="check" and cage!="dont" and cage!="don't":
            cage = input("check/dont: ")
        if cage == "check":
            print("I mean he is a very suspicious man!")
            time.sleep(3)
            print("He finds you as you turn around he cast a spell on you.")
            time.sleep(2)
            print("Game Over.")
            time.sleep(3)
            print("The game will automatically start from where you were.")
            time.sleep(3)
            alive = 0
            swamp()

        if cage == "dont" and "don't":
            print("Yeah he probably was suspicous but don't ruin his privacy")
            time.sleep(2)
            print("He takes you inside and gives you some soup...")
            time.sleep(2)
            print("But it was a trick! The soup was poison!")
            time.sleep(2)
            print("Game Over.")
            time.sleep(3)
            print("The game will automatically start from where you were.")
            time.sleep(3)
            alive = 0
            swamp()

    if alligator == "run":
        print("Good idea, alligators are strong.")
        time.sleep(2)
        print("You continue to walk when a little frog is in your way")
        time.sleep(2)
        print("He says that to pass you have to answer the riddle.")
        time.sleep(2)
        print("If you say my name I will no longer exist")
        riddle = ""
        while riddle!="silence":
            riddle = input("What is the answer?")

    if riddle == "silence":
            print("Wow! I didnt expect for you to get that right! Good job!")
            time.sleep(2)
            print("Just dont tell my boss! and if you're looking for the gem, he wont just give it that easily!")
            time.sleep(3)
            print("You continue to walk and see a castle.")
            time.sleep(2)
            print("You see a very hefty man inside and go to ask about the gem.")
            time.sleep(3)
            print("He says he has it but can only give it to you if you accept the duel")
            deul = ""
            while deul!="yes" and deul!="no":
                deul = input("yes/no: ")

    if deul == "no":
            print("Ok then, I geuss I will take you to the dungeon until you are ready!")
            time.sleep(3)
            print("Game Over.")
            time.sleep(3)
            print("The game will automatically start from where you were.")
            time.sleep(3)
            alive = 0
            swamp()

    if deul == "yes":
            print("You must be a fool, no one can beat the mighty KING!")
            time.sleep(2)
            print("You pull out you sword and are ready to destroy the king.")
            time.sleep(3)
            print("He charges you.")
            king = ""
            while king!="block" and king!="dodge":
                king = input("block/dodge: ")

    if king == "block":
            print("You block one attack but are no match for his others")
            time.sleep(3)
            print("Game Over.")
            time.sleep(3)
            print("The game will automatically start from where you were.")
            time.sleep(3)
            alive = 0
            swamp()

    if king == "dodge":
            print("He completely misses and you get a nice clean swing.")
            time.sleep(3)
            print("The king has fallen and the gem drops out of his hand.")
            time.sleep(3)
            print("Its the FUEL GEM!")
            time.sleep(3)
            print("Andrew calls, and wants you back as soon as you can.")
            time.sleep(3)
            print("He puts it back into the control panel.")
            time.sleep(3)
            print("A new area has appeared on your map!")
            time.sleep(3)
            print("Okay, head out as soon as you can after you get some sleep.")
            time.sleep(3)
            desert()

def desert():
    print("Welcome to the Desert Area!")
    time.sleep(3)
    print("Its pretty barren and there is no path to take.")
    time.sleep(2)
    print("A chicken walks up to you, you are very confused because it is a desert.")
    time.sleep(3)
    print("He asks you in chicken language what you are looking for.")
    time.sleep(2)
    print("You tell him about the gem and he says that the last power gem is in the dungeon.")
    time.sleep(3)
    print("He leads you to the kingdom and says you are on your own from here")
    time.sleep(2)
    print("You walk into the kingdom and see a shop.")
    shop = ""
    while shop!="enter" and shop!="walk":
        shop = input("enter/walk: ")

        if shop == "enter":
            print("You enter the shop and see a shiny new sword.")
            time.sleep(2)
            print("The manager asks why you are still here.")
            time.sleep(2)
            print("He says its past closing hours and that monsters will be in here at any moment.")
            time.sleep(2)
            print("The door slams down and a creature comes from behind and kills you.")
            time.sleep(2)
            print("Game Over.")
            time.sleep(3)
            print("The game will automatically start from where you were.")
            time.sleep(3)
            alive = 0
            desert()

        if shop == "walk":
            print("You walk down the path and you get a call from Andrew.")
            time.sleep(2)
            print("He says you are getting close but the system is glitching out.")
            time.sleep(2)
            print("You here something move behind you and there stands a shadowy person that doesn't look real.")
            time.sleep(2)
            print("It has the last gem Andrew points out.")
            time.sleep(3)
            print("You pull out your sword and get ready because this is gonna be a good fight.")
            time.sleep(2)
            print("He glitches toward you.")
            boss = ""
            while boss!="block" and boss!="dodge":
                boss = input("block/dodge: ")

        if boss == "dodge":
            print("There isn't anything to dodge and the shadowy figure kills you.")
            time.sleep(2)
            print("Game")
            time.sleep(3)
            print("The game will automatically start from where you were.")
            time.sleep(3)
            alive = 0
            desert()

        if boss == "block":
            print("You block his shawdow hand and notice something weird...")
            time.sleep(2)
            print("He looks like someone you know...")
            time.sleep(2)
            print("You realize who it is, it one of the other crew members but it looks like he is hypnotized.")
            time.sleep(2)
            print("Try and get your friend back without hurting him.")
            time.sleep(2)
            print("He comes at you again, but this time way faster.")
            boss1 = ""
            while boss1!="block" and boss1!="dodge":
                boss1 = input("block/dodge: ")

        if boss1 == "block":
            print("You can't block his attack this time and he kills you.")
            time.sleep(2)
            print("Game Over.")
            time.sleep(3)
            print("The game will automatically start from where you were.")
            time.sleep(3)
            alive = 0
            desert()

        if boss1 == "dodge":
            print("Because he is moving fast this time you can dodge the attack")
            time.sleep(2)
            print("You hear sirens coming towards you.")
            time.sleep(3)
            print("It's the police and they are after the shadow person.")
            time.sleep(3)
            print("He flees but the last gem is left behind!")
            time.sleep(3)
            print("It's the CONTROL GEM!")
            time.sleep(3)
            print("This is the last gem and lets you control the ship!")
            time.sleep(3)
            print("You head back with the last gem when Andrew isn't in the ship.")
            time.sleep(3)
            print("He isn't anywhere to be seen and without him you can't return home.")
            end()

def end():
    print("TO BE CONTINUED.")
    time.sleep(6)
    print("This is the end of the game thanks for playing and congratulations for making it this far!")
    time.sleep(6)
    print("Also did you find the Easter Egg in the beginning?")
    time.sleep(5)
    print("Big thanks to Eliot this game wouldn't have been possible without him. Alright I promise I will go now. BYE!")
    time.sleep(5)

while 1:
    clear()
    whattodo=''
    while whattodo!='p' and whattodo!='e':
        print("What would you like to do?")
        print("Type p to play")
        print("Type e to exit")
        whattodo=input()
        clear()
    if whattodo=='p':
        start()
    else:
        exit()
                                           
start()
