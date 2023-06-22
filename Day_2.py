# Data types
# string
print("Hello"[4])
# integer
print(123 + 345)
# float
3.485
# boolean
# true
# false
len(input("what is your name?"))
num_char = (True)
print(type(num_char))
# data type conversion or type casting
num_char = len(input("what is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
two_digit_number = input("Type a two digit number:")
num_1 = two_digit_number[0]
num_2 = two_digit_number[1]
result = int(num_1) + int(num_2)
print(result)
# BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight i kg: ")
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)
print(round(9 / 3.3, 3))
score = 0
score += 1
print (score)
score = 90
height = 1.8
isWinning = True
#f-String
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
# Your Life in Weeks
age = input("What is your current age? ")
age_is_int = int(age)
years_remaining = 90 - age_is_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message =(f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left")
print(message)
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?  $")) 
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
input = ( "Each person shpuld pay ('money')")
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")