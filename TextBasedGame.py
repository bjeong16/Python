# -*- coding: UTF-8 -*-
import time
from time import sleep
import string
import random
import graphics.py
from graphics.py import *

def Intro():

    print("Welcome to Dungeon, a text based game")
    
    sleep(0.3)
    gender = raw_input("Please enter the gender of your character \n 1. Male \n 2. Female \n")
    sleep(0.3)
    print("You are a " + gender)
    sleep(0.3)
    username = raw_input("Please enter the name of your character: \n")
    print("Your name is " + username)
    sleep(0.3)
    job = raw_input("Please select what your fighting style \n 1. Melee \n 2. Mage \n ")

    global userInfo
    userInfo = {'Gender' : gender , 'Name' : username, 'Style' : job}

def BaseStatInitialization():

    maleMeleeInfo = {'Health' : 500, 'AttackPower' : 50, 'Speed' : 10, 'CritChance' : 10, 'Mana' : 250}
    femaleMeleeInfo = {'Health' : 450, 'AttackPower' : 55, 'Speed' : 20,'CritChance' : 10, 'Mana' :200}

    maleMageInfo = {'Health' : 300, 'AttackPower' : 70, 'Speed' : 25, 'CritChance' : 20, 'Mana' : 500}
    femaleMageInfo = {'Health' : 250, 'AttackPower' : 75, 'Speed' : 30, 'CritChance' : 20, 'Mana' : 475}
    print("Here are the base stats for the character you have created: ")
    sleep(0.5)
    global markCharacterInfo
    if userInfo['Gender'] == 'Male' :
        if userInfo['Style'] == 'Melee':
            markCharacterInfo = maleMeleeInfo
            print(maleMeleeInfo)
        else:
            markCharacterInfo = maleMageInfo
            print(maleMageInfo)
    else:
        if userInfo['Style'] == 'Melee':
            markCharacterInfo = femaleMeleeInfo
            print(femaleMeleeInfo)
        else:
            markCharacterInfo = femaleMageInfo
            print(femaleMageInfo)

def ItemInitialization():
    global Money
    Money = 300

    redPotion = {"Name" : "RedPotion", "Description" : 100, "Cost" : 50}  # health
    bluePotion = {"Name" : "BluePotion", "Description" : 75, "Cost" : 50} # mana
    CritBoost = {"Name" : "CritBoost", "Description" : 1.5, "Cost" : 50} # crit chance

    LongSword = {"Name" : "LongSword", "Description" : 25, "Cost" : 100} # perm att.dmg
    BaseShield = {"Name" : "BaseShield", "Description" : 200, "Cost" : 100} #perm health growth

    global itemlist
    itemlist = {1: {"Name" : "RedPotion", "Description" : 100, "Cost" : 50},
                2: {"Name" : "BluePotion", "Description" : 75, "Cost" : 50},
                3: {"Name" : "CritBoost", "Description" : 1.5, "Cost" : 50},
                4: {"Name" : "LongSword", "Description" : 25, "Cost" : 100}, # perm att.dmg
                5: {"Name" : "BaseShield", "Description" : 200, "Cost" : 100}} #perm health growth}

def creepInitialization():

    global creepLvl1
    global bossLvl1
    creepLvl1 = {1 : {"Name" : "Wild Pig", "Health" : 200, "AttackPower" : 10, "Speed" : 5, "CritChance" : 0, 'Mana' : 0, 'Exp' : 50, 'Gold' : 50},
             2 : {"Name" : "Wild Slime", "Health" : 100, "AttackPower" : 20, "Speed" : 10, "CritChance" : 0, 'Mana' : 0, 'Exp' : 50, 'Gold' : 50}}

    bossLvl1 = {"Name" : "Barbarian", "Health" : 2000, "AttackPower" : 40, "Speed" : 15, "CritChance" : 0, 'Mana' : 0, 'Exp' : 250, 'Gold' : 500}

def store():

    global Money
    print "Welcome to the store: \n"
    sleep(4)

    print "Here is a list of items available \n"
    print itemlist
    Money = 300
    global markCharacterInfo
    print "You currently have " + str(Money) + "Gold"
    option = input("To buy an item, press 1, to go to dungeon, press 2")
    if option == 1:
        print itemlist
        number = input("Which item would you like to purchase?")
        sleep(2)
        print "You have chosen to buy " + itemlist[number]["Name"]
        print "----- Applying item -----"
        if number == 4:
            markCharacterInfo["AttackPower"] += 25
            Money -= 100
            print "You have equipped the Long Sword. You will gain an additional 25 Attack Power"
            print "Your attack power is now " + str(markCharacterInfo["AttackPower"])
            print "You now have " + str(Money)
        if number == 5:
            markCharacterInfo["Health"] += 100
            Money -= 100
            print "You have equipped the BaseShield. You will gain an additional 100 health"

    sleep(2)

    print "Your Transaction has been complete. You will now be taken to the Dungeon"
    sleep(2)
    firstLevelDungeon()



def firstLevelDungeon():

    print " Welcome to the first level of the dungeon : \n"
    sleep(3)
    counter = 0
    while counter < 3:
        creepLvl1[2]["Health"] = 100
        creepLvl1[1]["Health"] = 200
        print " ----- Randomly Generating Creep ----- \n"
        sleep(5)
        x = random.randint(1,2)
        monster = creepLvl1[x]

        print monster

        print "----- Starting Battle with " + creepLvl1[x]["Name"] + " ----- \n"

        while creepLvl1[x]["Health"] > 0:
            if markCharacterInfo["Health"] < 0:
                print "You have died"
                return

            myturn = input("1. Basic Attack \n 2. Regeneration \n 3. LuckyLightning \n ")
            if myturn == 1:
                creepLvl1[x]["Health"] -= markCharacterInfo["AttackPower"]
                print "You dealed" + str(markCharacterInfo["AttackPower"]) + " damage! \n"
                if creepLvl1[x]["Health"] <= 0:
                    creepLvl1[x]["Health"] = 0
                print "The wild creature's health is now \n" + str(creepLvl1[x]["Health"])
            elif myturn == 2:
                markCharacterInfo["Health"] += 75
                markCharacterInfo["Mana"] += 75
                print "Your health and mana are now " + str(markCharacterInfo["Health"]) + str(markCharacterInfo["Mana"])
            else:
                markCharacterInfo["Mana"] -= 50
                if markCharacterInfo["Mana"] < 50:
                    print("You do not have enough mana to use this ability")
                else:
                    damage = (markCharacterInfo["AttackPower"] + random.randint(50, 150))
                    creepLvl1[x]["Health"] -= damage
                    print "You dealt " + str(damage) + " damage!"
                    if creepLvl1[x]["Health"] <= 0:
                        creepLvl1[x]["Health"] = 0
                    print "The wild creature's health is now " + str(creepLvl1[x]["Health"])

            sleep(2)

            if creepLvl1[x]["Health"] <= 0:
                break

            print("The wild creep attacked! \n")
            sleep(3)
            markCharacterInfo["Health"] -= creepLvl1[x]["AttackPower"]
            print "Your Health is now " + str(markCharacterInfo["Health"])
        counter += 1
        print "You have defeated monster number " + str(counter)

    print "The Barbarian has appeared!"
    print "--------------"
    print "|  ^     ^   |"
    print "|     o      |"
    print "|   uuuuuu   |"
    print "--------------"
    print "   |      |"
    while bossLvl1["Health"] > 0:
        if markCharacterInfo["Health"] <= 0:
            print "You have died"
            return

        myturn = input("1. Basic Attack \n 2. Regeneration \n 3. LuckyLightning")
        if myturn == 1:
            bossLvl1["Health"] -= markCharacterInfo["AttackPower"]
            print "You dealt" + str(markCharacterInfo["AttackPower"]) + " damage! \n"
            if bossLvl1["Health"] <= 0:
                bossLvl1["Health"] = 0
            print "The Barabarian's health is now \n" + str(bossLvl1["Health"])
        elif myturn == 2:
            markCharacterInfo["Health"] += 75
            markCharacterInfo["Mana"] += 75
            print "Your health and mana are now " + str(markCharacterInfo["Health"]) + "  " + str(markCharacterInfo["Mana"])
        else:
            damage = (markCharacterInfo["AttackPower"] + random.randint(50, 150))
            bossLvl1["Health"] -= damage
            print "You dealt " + str(damage) + " damage!"
            if bossLvl1["Health"] <= 0:
                bossLvl1["Health"] = 0
            print "The Barbarian health is now " + str(bossLvl1["Health"])

        sleep(2)

        if bossLvl1["Health"] <= 0:
            break

        if bossLvl1["Health"] < 500:
            print "The Barbarian is angry!! He will gain Attack Damage"
            print "The Barbarian has appeared!"
            print "--------------"
            print "|  ;     ;   |"
            print "|     o      | 나 화났어 ㅅㄱ"
            print "|   uuuuuu   |"
            print "--------------"
            print "   |      |"
            bossLvl1["AttackPower"] += 10
        print("The Barbarian attacked! \n")
        sleep(3)
        markCharacterInfo["Health"] -= bossLvl1["AttackPower"]
        print "Your Health is now " + str(markCharacterInfo["Health"])

    print "You have slain the Barbarian! You have cleared the first floor!"



def startGame():
    print("Hello. Welcome to the first level of the dungeon. You will be able to access your items immediately after combat with a monster. \n During battle, you will only be able to access potions, and this will consume a turn with the monster \n")
    sleep(4)
    print("In the first level of the dungeon, you will have to defeat 3 randomly generated creeps, and then the Barbarian. After completing the dungeon, you will able to go home, which restores your health and mana. \n")
    sleep(4)
    print("In the first level of the dungeon, your character will have 2 skills besides the basic attack. \n")
    sleep(4)
    if userInfo["Style"] == "Melee":
        print("Skill1 : Everlasting (Gain 100 hp back, consumes 30 mana) \n")
        sleep(4)
        print("Skill2 : DoubleSlash (Attack with twice the attack dmg of your character) \n ")

    if userInfo["Style"] == 'Mage':
        print("Skill1 : Regeneration (Gain 75 hp, 75 mana back, consumes no mana) \n")
        sleep(4)
        print("Skill2 : LuckyLightning (Attack with a random AttackPower between 50 - 150 in addition to your base Attack, consumes 100 mana) \n")

    sleep(4)
    shop = input("To use the shop before proceeding, press 1 \n To proceed to the dungeon press 2")

    if shop == 1:
        store()
    if shop == 2:
        firstLevelDungeon()

    print"Congratulations, You have completed the first level of the Dungeon"
    sleep(2)
    print"You will now be transported to the second level of the Dungeon"
    sleep(2)


if __name__ == '__main__':
    Intro()
    BaseStatInitialization()
    ItemInitialization()
    creepInitialization()
    start = input("To start the game, press 1: \n")
    if start == 1:
        sleep(2)
        startGame()