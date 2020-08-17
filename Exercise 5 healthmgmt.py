# Health management system
def getdate():
    import datetime
    return datetime.datetime.now()


def log(k):
    if k == 1:
        opt = int(input("Select 1 For Food 2 For exercise"))
        if opt == 1:
            value = input("Enter What you eat ? :")
            with open("ram_food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print(value, "is added in to database")
        elif opt == 2:
            value = input("Enter What you Play this day ? :")
            with open("ram_exercise.txt", "w") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print(value, "is added in to database")
        else:
            print("enter a valid input")
    elif k == 2:
        opt = int(input("Select 1 For Food 2 For exercise"))
        if opt == 1:
            value = input("Enter What you eat ? :")
            with open("rabin_food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print(value, "is added in to database")
        elif opt == 2:
            value = input("Enter What you Play this day ? :")
            with open("rabin_exercise.txt", "w") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print(value, "is added in to database")
        else:
            print("enter a valid input")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            with open("ram_exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("ram_food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 2:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            with open("ram_exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("ram_food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("enter a valid input")


print("Health management system ")
a = int(input('Enter 1 For Log & 2 For Retrieve'))
if a == 1:
    b = int(input("Enter 1 For Ram & 2 For Rabin"))
    log(b)
else:
    b = int(input("Enter 1 For Ram & 2 For Rabin"))
    retrieve(b)
    pass
