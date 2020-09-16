# x = input("enter your name ")
# if x < 0 :
#     reise Exception("Sorry no num below Zero ")
c = input("Enter your name ")
try:
    print(a)
except Exception as e:
    if c == "jitu":
        raise ValueError("Not Allowed")
    print("Exception Handled")