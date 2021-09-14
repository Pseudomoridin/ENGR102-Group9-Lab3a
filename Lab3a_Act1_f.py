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

from conversions import convertCtoR

#all functions are stored in and imported from conversions.py
degreeC = float(input("Please enter the number of degrees Celcius to be converted to degrees Rankine: "))
print((degreeC // .01) / 100, "degrees Celcius is equivalent to", convertCtoR(degreeC),"degrees Rankine")