# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Elayne Elphingstone
#               NAME OF TEAM MEMBER 2
#               NAME OF TEAM MEMBER 3
#               NAME OF TEAM MEMBER 4
# Section:      472/572
# Assignment:   Lab 2A Activity 3
# Date:         September 8, 2021

from conversions import convertKMtoMI

#all functions are stored in and imported from conversions.py
km = float(input("Please enter the number of kilometers to be converted to miles: "))
print("{_km:.2f} kilometers is equivalent to {miles:.2f} miles".format(_km=km,miles=convertKMtoMI(km)))