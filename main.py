
print("Welcome to the tip calculator !!")

bill = float(input("What was the total bill ? $ "))
tip = int(input("What percent of bill you would want to give as tip ? "))
split_members = int(input("How many people to split the bill amongst ?"))

total_amount = bill + (bill * tip/100)

per_person = total_amount / split_members
print("Amount to be paid by each person is ${0:.2f}".format(per_person))