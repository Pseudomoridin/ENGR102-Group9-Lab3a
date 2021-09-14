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

from conversions import convertLPStoGPM
  
#all functions are stored in and imported from conversions.py
lps = float(input("Please enter the number of liters per second to be converted to gallons per minute: "))
print("{_lps:.2f} liters per second is equivalent to {gpm:.2f} gallons per minute".format(_lps=lps,gpm=convertLPStoGPM(lps)))