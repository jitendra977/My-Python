# faulty calculator
# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
a=int(input("enter a first number:"))
b=int(input("inter a second number:"))
operand=input("select operator you want calculate +,-,*,/:")
if operand=="+":
    result = a + b
    if a==56 and b==9 :
        print("Result is : 77")
    else :
        print("Result is :",result)
if operand=="-":
    result = a - b
    print("Result is :",result)
if operand=="*":
    result = a * b
    if a==45 and b==3 :
        print("Result is : 555")
    else :
        print("Result is :",result)
if operand=="/":
    result = a / b
    if a==56 and b==6 :
        print("Result is : 4")
    else :
        print("Result is :",result)