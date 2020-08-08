#
i=0
n=18
for i in range(9):
    print("enter number ",9-i," times Remember only:-")
    user=int(input())
    if user<18:
        print("Enter the number over the current number")
    elif user>18:
        print("Enter the number under the current number")
    else:
        print("You own Great")
        print("You can find guss on",i+1, "times")
        break
    print(9-i,"Times left")
    print("GAME OVER")
    