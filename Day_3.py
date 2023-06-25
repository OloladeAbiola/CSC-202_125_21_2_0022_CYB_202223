# print("Welcome to the rollercoaster !")
bill = 0
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickes are $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
        print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller befre you ca ride.")
# Odd or Even
number = int(input("Which number do you want to check? "))
if number%2 == 1:
    print("It is an odd number")
else:
    print("It is a even number")
    # BMI Calculator
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / height ** 2)
print(bmi)
if bmi < 18.5:
    print("you are underweight")
elif bmi > 18.5 < 25:
    print("you have a nurnal weight")
elif bmi > 25 < 30:
    print("you are overweight")
elif bmi > 30 < 35:
    print("you are obese")
else:
    print("you are clinically obese")
# Leap year
year = int(input("Which year do you want to check? "))
print(year)
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 15
    if size == "M":
        bill += 20
else:
    bill += 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
# print(f"Your final bill is ${bill}")
print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_string = name1 + name2
lower_case_string = combined_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l + o + v + e
love_score = str(true) + str(love)
print(f"Your love score is {love_score}%")
if (love_score) < 10 or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
#Treasure Land Game
print("Welcome to Treasure Land Game!\nYour mission is to find the treasure!")
path = input("Choose a path between left and right. Type 'left' or 'right' to choose a path \n").lower()
if path == "left":
    main_choice = input("You are at a lake. There is an island at the middle of the lake.\nType 'swim' to swim across or type 'wait' to wait for a boat \n").lower()
    if main_choice == "wait":
        choice2 = input("The boat has arrived and it has three doors colored red, blue and yellow.\nType 'red' to enter through the red door or 'blue' to enter through the blue door \nor type 'yellow' to go through the yellow door  \n").lower()
        if choice2 == "red":
            print("Oops! Game over")
        elif choice2 == "blue":
            print("Oops! Wrong choice. Game over")
        else:
            print("Congratulations! You found the treasure")
    else:
        print("Oops, Game Over! The lake is too vast. You'll die if you choose to swim across")
else:
    print("Game over! You fell into a hole")
