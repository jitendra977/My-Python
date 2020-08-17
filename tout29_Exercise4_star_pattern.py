print("Enter the value of number :")
num_1 = int(input())
print("Enter the value of number :")
num = bool(int(input()))
if num == True:
    for i in range(num_1+1):
        for j in range(num_1+1):
            if j >= num_1-i:
                print("*", end=" ")
        print()
else:
    for i in range(num_1 + 1):
        for j in range(num_1 + 1):
            if j <= num_1 - i:
                print("*", end=" ")
        print()

#harry method 
def star(a,b):
    global num_1
    if num==True:
        c=1
        while c<=num_1:
            print(c*"* ")
            c+=1
    else:
        while num_1>0:
            print(num_1*"* ")
            num_1-=1
star(num_1,num)