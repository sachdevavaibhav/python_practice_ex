# Exercise 4(ASTROLOGER'S STAR)
print()
i = 1
num1 = int(input("PLEASE ENTER A NUMBER: "))
num2 = int(input("ENTER 0 or 1: "))


while(i<=num1):
    if num2 == 0:
     print(i*"*")
     i = i + 1
     continue

    elif num2 == 1:
        print(num1*"*")
        num1 = num1 - 1
        continue

    else:
        print("INVALID INPUT")
        break








