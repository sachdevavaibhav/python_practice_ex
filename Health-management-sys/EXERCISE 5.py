print("WELCOME TO FITNESS FREAK GYM!!")
ask1=input("PRESS 0 TO LOG IN OR PRESS 1 TO RETRIEVE FILE: ")
def getdate():
    import datetime
    return datetime.datetime.now()

def main1():
    ask2= input("PRESS a FOR YASH \nb FOR VAIBHAV \nc FOR AMAN ")
    date ="    " + str(getdate())
    #write= "\t" + input("ENTER DAY: ") + date + "\n"
    if(ask2=="a"):
        y = input("PRESS y TO CONTINUE: ")
        print("\nPRESS q TO EXIT!!")
        while(y=="y"):
         f1=open("YASH EXERCISE.txt","a")
         write= input() + date + "\n"
         if write== "q" + date + "\n":
             break
         else:
          f1.write(write)
          f1.close()
         continue

    elif ask2=="b":
        y = input("PRESS y TO CONTINUE: ")
        print("\nPRESS q TO EXIT!!")
        while(y=="y"):
         f2=open("VAIBHAV EXERCISE.txt","a")
         write = input() + date + "\n"
         if write == "q" + date + "\n":
             break
         else:
             f2.write(write)
             f2.close()
         continue
         f2.write(write)
         f2.close()
         continue
    elif ask2=="c":
        y = input("PRESS y TO CONTINUE: ")
        print("\nPRESS q TO EXIT!!")
        while(y=="y"):
         f3=open("AMAN EXERCISE.txt", "a")
         write = input() + date + "\n"
         if write == "q" + date + "\n":
             break
         else:
             f3.write(write)
             f3.close()
         continue
         # f3.write(write)
         # f3.close()
         # continue

def main2():
    ask2 = input("PRESS a FOR YASH \nb FOR VAIBHAV \nc FOR AMAN ")
    date = "    " + str(getdate())
    # write= "\t" + input("ENTER DAY: ") + date + "\n"
    if (ask2 == "a"):
        y = input("PRESS y TO CONTINUE: ")
        print("\nPRESS q TO EXIT!!")
        while (y == "y"):
            f1 = open("YASH DIET.txt", "a")
            write = input() + date + "\n"
            if write == "q" + date + "\n":
                break
            else:
                f1.write(write)
                f1.close()
            continue

    elif ask2 == "b":
        y = input("PRESS y TO CONTINUE: ")
        print("\nPRESS q TO EXIT!!")
        while (y == "y"):
            f2 = open("VAIBHAV DIET.txt", "a")
            write = input() + date + "\n"
            if write == "q" + date + "\n":
                break
            else:
                f2.write(write)
                f2.close()
            continue
            f2.write(write)
            f2.close()
            continue
    elif ask2 == "c":
        y = input("PRESS y TO CONTINUE: ")
        print("\nPRESS q TO EXIT!!")
        while (y == "y"):
            f3 = open("AMAN DIET.txt", "a")
            write = input() + date + "\n"
            if write == "q" + date + "\n":
                break
            else:
                f3.write(write)
                f3.close()
            continue
            f3.write(write)
            f3.close()
            continue
            
def main3():
    ask2 = input("PRESS a FOR YASH \nb FOR VAIBHAV \nc FOR AMAN ")

    if (ask2 == "a"):
        y = input("PRESS y TO CONTINUE: ")
        f1 = open("YASH EXERCISE.txt", "r")
        read1 = f1.read()
        print(read1, end=" ")
        f1.close()
    elif ask2 == "b":
        y = input("PRESS y TO CONTINUE: ")
        f2 = open("VAIBHAV EXERCISE.txt", "r")
        read2 = f2.read()
        print(read2, end=" ")
        f2.close()
    elif ask2 == "c":
        y = input("PRESS y TO CONTINUE: ")
        f3 = open("AMAN EXERCISE.txt", "r")
        read3 = f3.read()
        print(read3, end=" ")
        f3.close()

def main4():
    ask2 = input("PRESS a FOR YASH \nb FOR VAIBHAV \nc FOR AMAN ")

    if (ask2 == "a"):
        y = input("PRESS y TO CONTINUE: ")
        f1 = open("YASH DIET.txt", "r")
        read1 = f1.read()
        print(read1, end=" ")
        f1.close()
    elif ask2 == "b":
        y = input("PRESS y TO CONTINUE: ")
        f2 = open("VAIBHAV DIET.txt", "r")
        read2 = f2.read()
        print(read2, end=" ")
        f2.close()
    elif ask2 == "c":
        y = input("PRESS y TO CONTINUE: ")
        f3 = open("AMAN DIET.txt", "r")
        read3 = f3.read()
        print(read3, end=" ")
        f3.close()

def chooseLog():
    ask3 = input("PRESS 0 FOR EXERCISE OR 1 FOR DIET: ")
    if ask3=="0":
        main1()
    else:
        main2()

def chooseRetrieve():
    ask3 = input("PRESS 0 FOR EXERCISE OR 1 FOR DIET: ")
    if ask3 == "0":
        main3()
    else:
        main4()


if ask1 == "0":
    chooseLog()
elif ask1 == "1":
    chooseRetrieve()
else:
    print("INVALID INPUT!!")

