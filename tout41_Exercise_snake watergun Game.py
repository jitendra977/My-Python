import random
run_time = int(input("enter how many Play Game"))
option1 = ["s", "w", "g"]
no_of_chance = 0
computer_point = 0
your_point = 0

def computer_win():
    global computer_point
    computer_point = computer_point + 1
    print(f"your gues {user_1} and computer guess is {rand_random}\n")
    print("Computer has 1 point")
    print(f"computer point is {computer_point} and your point is {user_1}")
def user_win():
    global your_point
    your_point=your_point+1
    print(f"your gues {user_1} and computer guess is {rand_random}\n")
    print("you has 1 point")
    print(f"computer point is {computer_point} and your point is {your_point}")

print("water snake gun game \n")
print("Enter s for snake w for water and g for gun")
for i in range(run_time) :
    if no_of_chance<run_time:
        user_1=input("Enter s for snake w for water and g for gun :")
        rand_random=random.choice(option1)
        if rand_random==user_1:
            print("Tie Both are same!")
        if user_1=="s" and rand_random=="g":
            computer_win()
        elif user_1=="s" and rand_random=="w":
            user_win()
        elif user_1=="w" and rand_random=="s":
            computer_win()
        elif user_1 == "w" and rand_random == "g":
            user_win()
        elif user_1 == "g" and rand_random == "s":
            user_win()
        elif user_1 == "g" and rand_random == "w":
            computer_win()
        else:
            print("please write input")
        no_of_chance = no_of_chance + 1
        print(f"{run_time-no_of_chance} is left out of {run_time} \n")

print("Game over")

if computer_point > your_point:
    print("Computer wins and you loose")

if computer_point < your_point:
    print("you win and computer loose")
print(f"your point is {your_point} and computer point is {computer_point}")