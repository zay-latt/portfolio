cost = 18.07
cash = 20

change = round(cash - cost, 2)
print()
print("Change due:", change)

Dollars =   change // 1
Quarters = (change - (Dollars)) // 0.25
Dimes =    (change - (Dollars + (Quarters*0.25))) // 0.1
Nickels =  (change - (Dollars + (Quarters*0.25) + (Dimes*0.1))) // 0.05
Pennies =  (change - (Dollars + (Quarters*0.25) + (Dimes*0.1) + (Nickels*0.05))) // 0.01

print()
print("Dollars:", int(Dollars))
print("Quarters:", int(Quarters))
print("Dimes:", int(Dimes))
print("Nickels:", int(Nickels))
print("Pennies:", int(Pennies))