print("Welcome to the tip calculator")
total_bill = float(input("What is the total bill? "))
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int (input("How many poeple to split the bill? "))
bill_with_tip = (total_bill + (total_bill * percent_tip)/100)/people
final_amount = round(bill_with_tip,2)
print(f"Each person should pay: {final_amount}")
