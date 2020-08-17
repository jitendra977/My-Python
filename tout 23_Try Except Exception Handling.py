print("enter a num1")
num1 = input()
print("enter a num2")
num2 = input()
try:
    print("The sum of two num is ", int(num1)+int(num2))
except Exception as e:
    print("Please enter valid input ",e)
