#  STONE, PAPER, SCISSOR
import random
from playsound import playsound
print("WELCOME TO STONE, PAPER, SCISSOR GAME!!")
s1 = playsound("D:\Business\Twerk.wav")
S = "Scissor"
P = "Paper"
G = "Stone"
lst = [G, P, S]
# opt = random.choice(lst)
i=0
l = 10 - i
comp = 0
user = 0
res = print(F"COMPUTER: {comp} \tUSER: {user} \tTURNS LEFT: {l}")
try:
 while(i<10):
    sound = playsound("D:\gps.mp3")
    x = input("PRESS \ns for scissor \np for paper \ng for stone \nYOUR INPUT: ")
    good = "Well Done"
    bad = "Better Luck Next Time"
    draw = "Draw!"
    opt = random.choice(lst)
    i=i+1
    l=10-i

    #print("TURNS LEFT: ",l)
    if x == "g" and opt == S:
        print(good)
        user = user+1
        res = print(F"COMPUTER: {comp} \tUSER: {user} \tTURNS LEFT: {l}")
    elif x == "g" and opt == P:
        print(bad)
        comp = comp+1
        res = print(F"COMPUTER: {comp} \tUSER: {user} \tTURNS LEFT: {l}")
    elif x == "g" and opt == G:
        print(draw)
        res = print(F"COMPUTER: {comp} \tUSER: {user} \tTURNS LEFT: {l}")
    elif x == "p" and opt == G:
        print(good)
        user = user + 1
        res = print(F"COMPUTER: {comp} \tUSER: {user} \tTURNS LEFT: {l}")
    elif x == "p" and opt == S:
        print(bad)
        comp = comp + 1
        res = print(F"COMPUTER: {comp} \tUSER: {user} \tTURNS LEFT: {l}")
    elif x == "p" and opt == P:
        print(draw)
        res = print(F"COMPUTER: {comp} \tUSER: {user} \tTURNS LEFT: {l}")
    elif x == "s" and opt == P:
        print(good)
        user = user + 1
        res = print(F"COMPUTER: {comp} \tUSER: {user} \tTURNS LEFT: {l}")
    elif x == "s" and opt == G:
        print(bad)
        comp = comp + 1
        res = print(F"COMPUTER: {comp} \tUSER: {user} \tTURNS LEFT: {l}")
    elif x == "s" and opt == S:
        print(draw)
        res = print(F"COMPUTER: {comp} \tUSER: {user} \tTURNS LEFT: {l}")
    else:
        print("ERROR!!")
        continue
        l = l + 1
except:
    print("UNKNOWN ERROR OCCURED!!")

if comp > user:
    print("\nCOMPUTER WINS!!")
elif comp == user:
    print("\nMATCH DRAW!!")
else:
    print("\nCONGRATULATIONS!YOU WON.")








































