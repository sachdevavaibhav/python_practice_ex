# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

# FAULTY CALCULATOR


num1 = input("ENTER YOUR FIRST NUMBER: ")

num2 = input("ENTER YOUR SECOND NUMBER: ")

operator = input("CHOOSE YOUR OPERATOR: +, -, /, *: ")

if (num1=="56" and num2=="9") or (num1=="9" and num2=="56") and operator== '+':
    print("= 77")

elif (num1=="45" and num2=="3") or (num1=="3" and num2=="45") and operator=='*':
    print("= 555")

elif num1=="56" and num2=="6" and operator=='/':
    print("= 4")

elif operator=="+":
    print("=", int(num1)+int(num2))

elif operator=='-':
    print("=", int(num1)-int(num2))

elif operator=='*':
    print("=", int(num1)*int(num2))

elif operator=='/':
    print("=", int(num1)/int(num2))

else:
    print("INVALID INPUT")



