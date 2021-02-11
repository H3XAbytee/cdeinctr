import random
import string
import time
import requests
import string
import os
import os.path
from os import path as pfad
bothUP = string.ascii_uppercase + "0" "1" "2" "3" "4" "5" "6" "7" "8" "9"
bothDOWN = string.ascii_lowercase + "0" "1" "2" "3" "4" "5" "6" "7" "8" "9"

class numsandlets:
    bothUP = string.ascii_uppercase + "0" "1" "2" "3" "4" "5" "6" "7" "8" "9"
    bothDOWN = string.ascii_lowercase + "0" "1" "2" "3" "4" "5" "6" "7" "8" "9"
letters = string.ascii_uppercase
numbers = "0" "1" "2" "3" "4" "5" "6" "7" "8" "9"
both = letters + str(numbers)
final = random.choice(both)
getos = os.name
tries = 1
print("Please enter the path where the txt files are located or 'skip' to skip this part. (Can´t use checker then)")
path = input(r"Path: ")
def pathchoose():
    os.system('cls')
    if path == "skip":
        print("No Path given... Skipping this part")
        time.sleep(2)
        return choice()
    else:
        exist = pfad.exists(path)
        if exist == False:
            print("[-]Can´t find given Path")
            quit()
        else:
            return choice()
VERSION = float(1.0)
"""VERSION=1.01 DEVELOPER=print("H3XA")#6855"""


def getletter():
    letters1 = random.choice(both)
    letters2 = random.choice(both)
    letters3 = random.choice(both)
    letters4 = random.choice(both)
    letters5 = random.choice(both)
    letters6 = random.choice(both)
    letters7 = random.choice(both)
    letters8 = random.choice(both)
    letters9 = random.choice(both)
    letters10 = random.choice(both)
    letters11 = random.choice(both)
    letters12 = random.choice(both)
    night = letters1 + letters2 + letters3 + letters4 + "-" + letters5 + letters6 + letters7 + letters8 + "-" + letters9 + letters10 + letters11 + letters12
    print(night)
def choice():
    os.system(f'Title CdeInjctr (Premium V={VERSION})')
    os.system('cls')
    print("         _      _       _      _                        ")
    print("        | |    (_)     (_)    | |                       ")
    print("  ___ __| | ___ _ _ __  _  ___| |_ _ __ __ _  ___ _ __  ")
    print(" / __/ _` |/ _ \ | '_ \| |/ __| __| '__/ _` |/ _ \ '_ \ ")
    print("| (_| (_| |  __/ | | | | | (__| |_| | | (_| |  __/ | | |")
    print(" \___\__,_|\___|_|_| |_| |\___|\__|_|  \__, |\___|_| |_|")
    print("                      _/ |              __/ |           ")
    print("                     |__/              |___/            ")
    print('premium=1.0.0     Made by maybe h3xa#6855')
    print("checker=False")
    print("=" * 50)
    print("PLAYSTATION[1]              AMAZON[2]")
    print("PAYSAFE[3]                  XBOX[4]")
    print("ITUNES[5]                   VISA[6]")
    print("DISCORD NITRO[7]            STEAM[8]")
    print("ROCKSTAR(1) [9]             ROCKSTAR (2) [10]")
    print("ENABLE CHECKER[11]          COLOR MENU[12]")
    print("CHANGE PATH[13]")
    user_input = input("Choice: ")
    if "1" or "2" or "3" or "4" or "5" or "6" in user_input:
        threds = int(input("How many cards you want(for colors and Checker 0)?~ "))
        print(f"Generating {threds} giftcard codes...")
        print("=" * 50)
    else:
        return color_menu()
    time.sleep(2)
    if user_input == "1":
        for o in range(threds):
            playstation()
    if user_input == "2":
        for i in range(threds):
            amazon()
    if user_input == "3":
        for p in range(threds):
            paysafe()
    if user_input == "4":
        for x in range(threds):
            xbox()
    if user_input == "5":
        for cock in range(threds):
            itunes()
    if user_input == "6":
        for lol in range(threds):
            visa()
    if user_input == "7":
        for pas in range(threds):
            discord()
    if user_input == "8":
        for stema in range(threds):
            steam()
    if user_input == "9":
        for rockstar in range(threds):
            rockstar1()
    if user_input == "10":
        for mom in range(threds):
            rockstar2()
    if user_input == "11":
        print("With the checker enabled the codes will be generatesd a lot slower. Still want to continue?(Y/N)")
        u = input("(Y/N): ")
        if u == "y" or "Y":
            return checkertrue()
        elif u == "n" or "N":
            return choice()
        else:
            return choice()
    if user_input == "12":
        print("Starting color menu...")
        time.sleep(2)
        return color_menu()
    if user_input == "13":
        return pathchoose()

def color_menu():
    getos = os.name
    if getos == "nt":
        print("Blue [1]         Green[2]")
        print("Turquoise[3]     Red[4]")
        print("Purple[5]        Yellow[6]")
        print("Light-Grey(default)    [7]")
        print("=" * 50)
        color = input("?> ")
        if color == "1":
            os.system('color 1')
            return choice()
        if color == "2":
            os.system('color 2')
            return choice()
        if color == "3":
            os.system('color 3')
            return choice()
        if color == "4":
            os.system('color 4')
            return choice()
        if color == "5":
            os.system('color 5')
            return choice()
        if color == "6":
            os.system('color 6')
            return choice()
        if color == "7":
            os.system('color 7')
            return choice()
        else:
            os.system('color 7')
            return choice()

def rockstar1():
    a = random.choice(letters)
    b = random.choice(letters)
    c = random.choice(letters)
    d = random.choice(letters)
    e = random.choice(letters)
    f = random.choice(letters)
    g = random.choice(letters)
    h = random.choice(letters)
    i = random.choice(letters)
    j = random.choice(letters)
    k = random.choice(letters)
    l = random.choice(letters)
    print(a + b + c + d + "-" + e + f + g + h + "-" + i + j + k + l)
def rockstar2():
    a = random.choice(both)
    b = random.choice(both)
    c = random.choice(both)
    d = random.choice(both)
    e = random.choice(both)
    # -
    f = random.choice(both)
    g = random.choice(both)
    h = random.choice(both)
    i = random.choice(both)
    j = random.choice(both)
    # -
    k = random.choice(both)
    l = random.choice(both)
    m = random.choice(both)
    n = random.choice(both)
    o = random.choice(both)
    # -
    p = random.choice(both)
    q = random.choice(both)
    r = random.choice(both)
    s = random.choice(both)
    t = random.choice(both)
    # -
    u = random.choice(both)
    v = random.choice(both)
    w = random.choice(both)
    x = random.choice(both)
    y = random.choice(both)
    print(a + b + c + d + e + "-" + f + g + h + i + j + "-" + k + l + m + n + o + "-" + p + q + r + s + t + "-" + u + v + w + x + y)
def steam():
    hara = string.ascii_letters + numbers
    a = random.choice(hara)
    b = random.choice(hara)
    c = random.choice(hara)
    d = random.choice(hara)
    e = random.choice(hara)
    f = random.choice(hara)
    g = random.choice(hara)
    h = random.choice(hara)
    i = random.choice(hara)
    j = random.choice(hara)
    k = random.choice(hara)
    l = random.choice(hara)
    m = random.choice(hara)
    n = random.choice(hara)
    o = random.choice(hara)
    code = a + b + c + d + e + "-" + f + g + h + i + j + "-" + k + l + m + n + o
    print(code)
def discord():
    url = "https://discord.com/gifts/"
    hara = string.ascii_letters + numbers
    a = random.choice(hara)
    b = random.choice(hara)
    c = random.choice(hara)
    d = random.choice(hara)
    e = random.choice(hara)
    f = random.choice(hara)
    g = random.choice(hara)
    h = random.choice(hara)
    i = random.choice(hara)
    j = random.choice(hara)
    k = random.choice(hara)
    l = random.choice(hara)
    m = random.choice(hara)
    n = random.choice(hara)
    o = random.choice(hara)
    p = random.choice(hara)
    url = url + a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p
    print(url)


def playstation():
    letter1 = random.choice(both)
    letter2 = random.choice(both)
    letter3 = random.choice(both)
    letter4 = random.choice(both)
    letter5 = random.choice(both)
    letter6 = random.choice(both)
    letter7 = random.choice(both)
    letter8 = random.choice(both)
    letter9 = random.choice(both)
    letter10 = random.choice(both)
    letter11 = random.choice(both)
    letter12 = random.choice(both)
    print(letter1 + letter2 + letter3 + letter4 + "-" + letter5 + letter6 + letter7 + letter8 + "-" + letter9 + letter10 + letter11 + letter12)


def amazon():
    a = random.choice(both)
    b = random.choice(both)
    c = random.choice(both)
    d = random.choice(both)
    # - einbauen
    e = random.choice(both)
    f = random.choice(both)
    g = random.choice(both)
    h = random.choice(both)
    i = random.choice(both)
    j = random.choice(both)
    # - einbauen
    k = random.choice(both)
    l = random.choice(both)
    m = random.choice(both)
    n = random.choice(both)
    o = random.choice(both)
    p = random.choice(both)
    print(str(a) + b + c + d + "-" + e + f + str(g) + h + i + j + "-" + k + l + m + n + o + p)


def paysafe():
    a = random.choice(numbers)
    b = random.choice(numbers)
    c = random.choice(numbers)
    d = random.choice(numbers)
    # space
    e = random.choice(numbers)
    f = random.choice(numbers)
    g = random.choice(numbers)
    h = random.choice(numbers)
    # space
    i = random.choice(numbers)
    j = random.choice(numbers)
    j = random.choice(numbers)
    k = random.choice(numbers)
    l = random.choice(numbers)
    # space
    m = random.choice(numbers)
    n = random.choice(numbers)
    o = random.choice(numbers)
    p = random.choice(numbers)
    print("0" + b + c + d + " " + e + f + g + h + " " + i + j + k + l + " " + m + n + o + p)


def xbox():
    a = random.choice(both)
    b = random.choice(both)
    c = random.choice(both)
    d = random.choice(both)
    e = random.choice(both)
    # -
    f = random.choice(both)
    g = random.choice(both)
    h = random.choice(both)
    i = random.choice(both)
    j = random.choice(both)
    # -
    k = random.choice(both)
    l = random.choice(both)
    m = random.choice(both)
    n = random.choice(both)
    o = random.choice(both)
    # -
    p = random.choice(both)
    q = random.choice(both)
    r = random.choice(both)
    s = random.choice(both)
    t = random.choice(both)
    # -
    u = random.choice(both)
    v = random.choice(both)
    w = random.choice(both)
    x = random.choice(both)
    y = random.choice(both)
    print(
        a + b + c + d + e + "-" + f + g + h + i + j + "-" + k + l + m + n + o + "-" + p + q + r + s + t + "-" + u + v + w + x + "Z")


def itunes():
    a = random.choice(numbers)
    b = random.choice(numbers)
    c = random.choice(numbers)
    d = random.choice(numbers)
    # space
    e = random.choice(both)
    f = random.choice(both)
    g = random.choice(both)
    h = random.choice(both)
    # space
    i = random.choice(both)
    j = random.choice(both)
    k = random.choice(both)
    l = random.choice(both)
    # space
    m = random.choice(both)
    n = random.choice(both)
    o = random.choice(both)
    p = random.choice(both)
    print(a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p)


def visa():
    a = random.choice(numbers)
    b = random.choice(numbers)
    c = random.choice(numbers)
    d = random.choice(numbers)
    e = random.choice(numbers)
    #
    f = random.choice(numbers)
    g = random.choice(numbers)
    h = random.choice(numbers)
    i = random.choice(numbers)
    j = random.choice(numbers)
    #
    k = random.choice(numbers)
    l = random.choice(numbers)
    m = random.choice(numbers)
    n = random.choice(numbers)
    o = random.choice(numbers)
    #
    p = random.choice(numbers)
    q = random.choice(numbers)
    r = random.choice(numbers)
    s = random.choice(numbers)
    t = random.choice(numbers)
    #
    u = random.choice(numbers)
    v = random.choice(numbers)
    w = random.choice(numbers)
    x = random.choice(numbers)
    y = random.choice(numbers)
    #
    print(b + c + d + e + "-" + g + h + i + j + "-" + l + m + n + o + "-" + q + r + s + t + ":" + str(
        random.randint(0, 12)) + "/" + str(random.randint(1, 31)) + " " + str(random.randint(0, 999)))

def checkertrue():
    alles = ""
   
    def discord_nitro():
        global alles
        igel = '{"message": "Unknown Gift Code", "code": 10038}'
        hara = string.ascii_letters + numbers
        url = "https://discord.com/gifts/"
        vor_url = "https://discord.com/api/v8/entitlements/gift-codes/"
        after_url = "?with_application=true&with_subscription_plan=true"
        wait = '''{
  "global": false, 
  "message": "You are being rate limited.",'''
        running = False
        a = random.choice(hara)
        b = random.choice(hara)
        c = random.choice(hara)
        d = random.choice(hara)
        e = random.choice(hara)
        f = random.choice(hara)
        g = random.choice(hara)
        h = random.choice(hara)
        i = random.choice(hara)
        j = random.choice(hara)
        k = random.choice(hara)
        l = random.choice(hara)
        m = random.choice(hara)
        n = random.choice(hara)
        o = random.choice(hara)
        p = random.choice(hara)
        url = url + a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p
        url_letter = vor_url + a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + after_url
        pi = requests.get(url_letter)
        if igel in pi.text[:47]:
            alles = url + " [-]INVALID"
        else:
            alles = url + " [*]MAYBE VALID (DON`T CHECK IF OVER THE TIMEOUT MESSAGE) " + f"({time.asctime()})" + "\n"
            if " [*]MAYBE VALID (DON`T CHECK IF OVER THE TIMEOUT MESSAGE)" in alles:
                op = open(path, 'a')
                op.write(str(alles))
                op.close()
        if wait in pi.text[:65]:
            running = True
        if running == True:
            alles = url + " [-]INVALID"
            dick = pi.text.split(".")
            piml = dick[1]
            cuck = piml.split(":")
            print(f"Well, looks like we have a timeout . We will have to wait {cuck[1]} seconds, after that i will continue checking the codes for you")
            if " [*]MAYBE VALID (DON`T CHECK IF OVER THE TIMEOUT MESSAGE)" in alles:
                op = open(r'C:\Users\Bruno\Desktop\TXT\VALID CODES.txt', 'a')
                op.write(alles + ", " + "\n")
                op.close()
            time.sleep(int(cuck[1]))
        print(alles)
        #check if [*] Maybe valid in code and write it in txt file
    #greeting 2
    os.system(f'Title CdeInjctr (Premium V={VERSION})')
    os.system('cls')
    print("         _      _       _      _                        ")
    print("        | |    (_)     (_)    | |                       ")
    print("  ___ __| | ___ _ _ __  _  ___| |_ _ __ __ _  ___ _ __  ")
    print(" / __/ _` |/ _ \ | '_ \| |/ __| __| '__/ _` |/ _ \ '_ \ ")
    print("| (_| (_| |  __/ | | | | | (__| |_| | | (_| |  __/ | | |")
    print(" \___\__,_|\___|_|_| |_| |\___|\__|_|  \__, |\___|_| |_|")
    print("                      _/ |              __/ |           ")
    print("                     |__/              |___/            ")
    print('premium=1.0.0     Made by print("H3XA")#6855')
    print("checker=True")
    print("=" * 50)
    print("DISCORD[1]")
    user_input = input("Choice: ")
    if "1" or "2" or "3" or "4" or "5" or "6" in user_input:
        threds2 = int(input("How many cards you want?~ "))
        print(f"Generating {threds2} giftcard codes...")
        print("=" * 50)
    if user_input == "1":
        for dis in range(threds2):
            discord_nitro()
    else:
        quit("No thing given")
    time.sleep(2)
    
pathchoose()