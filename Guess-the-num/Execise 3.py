print("Guess A NUMBER BETWEEN 0-100")
i = 22
inp = 5
guess = 1
num = int(input("Press 0 to start: "))
while(num>=0 ):
    num = int(input("ENTER A NUMBER: "))
    print("NUMBER OF ATTEMTS LEFT: ",inp)
    inp=inp-1
    guess = guess + 1
    if num==i and inp>=(-1):
        print("KUDOS!YOU GUESSED IT RIGHT.\nAttempts used: ",guess)

        break
    elif num>i and num<=26 and inp>=0:
        print("YOU ENTERED A NUMBER GREATER THAN EXPECTED BUT YOU ARE CLOSE TO THE VALUE.")
    elif num<i and num>=20 and inp>=0:
        print("YOU ENTERED A NUMBER LESSER THAN EXPECTED BUT YOU ARE CLOSE TO THE VALUE.")
    elif num>26 and inp>=0:
        print("YOU ENTERED A NUMBER GREATER THAN EXPECTED.")
    elif num<20 and inp>=0:
        print("YOU ENTERED A NUMBER LESSER THAN EXPECTED.")

        continue
    else:
        break
        print("Try Again!")
