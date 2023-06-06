#Create a calculator to calculate the tip
print("Welcome to the tip calculator!")

bill = float(input("What is i the total of the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 0r 15?"))
people_num = int(input("How many people to split the bill?"))

tip_as_percent = tip_percentage / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people_num

#Format the result to 2 decimal places = 33.60
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay {final_amount}")
