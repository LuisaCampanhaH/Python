print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? "))
people = int(input("How many people to split the bill?"))
bill_tip = bill +  (bill * (tip/100))
total_bilL_person = bill_tip / people
print(f"Each person should pay: {round(total_bilL_person,2)}")