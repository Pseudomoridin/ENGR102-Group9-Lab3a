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

from conversions import convertLbstoN

#all functions are stored in and imported from conversions.py
pounds = float(input("Please enter the number of pounds to be converted to Newtons: "))
print("{_pounds:.2f} pounds is equivalent to {newtons:.2f} Newtons".format(_pounds=pounds,newtons=convertLbstoN(pounds)))