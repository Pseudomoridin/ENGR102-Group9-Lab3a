# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Elayne Elphingstone
#               Reagan Wall
#               Logan Winship
#               Tyler Mayou & Zack Abbott
# Section:      472/572
# Assignment:   Lab 2A Activity 3
# Date:         September 8, 2021

from conversions import convertATMtoMMHG

#all functions are stored in and imported from conversions.py
atm = float(input("Please enter the number of atmospheres to be converted to millimeters of mercury: "))
print("{_atm:.2f} atmospheres is equivalent to {mmhg:.2f} millimeters of mercury".format(_atm=atm,mmhg=convertATMtoMMHG(atm)))