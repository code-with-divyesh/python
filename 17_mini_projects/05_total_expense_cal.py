rent=int(input("Enter Your Total Rent for hostal/flat:"))
food=int(input("Enter The amount for snacking:"))
units_used = int(input("Enter total electricity units used: "))
rate_per_unit = float(input("Enter the rate per unit: "))

persons=int(input("Enter the total person per flat/Room:"))

total_elec_bill = units_used * rate_per_unit
total_bill=rent+food+total_elec_bill
print("Total Bill is:",total_bill)
print("Each person will pay:",(total_bill)/persons)

