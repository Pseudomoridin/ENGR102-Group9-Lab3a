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

from conversions import convertWtoBTU

#all functions are stored in and imported from conversions.py
watts = float(input("Please enter the number of watts to be converted to BTU per hour: "))
print("{_watts:.2f} watts is equivalent to {btu:.2f} BTU per hour".format(_watts=watts,btu=convertWtoBTU(watts)))