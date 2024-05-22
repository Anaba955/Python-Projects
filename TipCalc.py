# Notes
# For large numbers we usally put comma(45, 610, 288), in python we can write this as 45_610_288
# To convert the data types we can use str(), float(), int() and bool()
# PEMDASLR -> ()  **  *,/  +,-
# 8 // 3 gives 2 which is an integer
# round()
# f-Strings: f"your score is {score}"


print("Welcome to tip calculator")
total = float(input("What was the total bill? $"))
tip = int(input("How much percent would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill? "))
split = (total + (tip * total / 100)) / people
print(f"Each person should pay: ${round(split, 2)}")
