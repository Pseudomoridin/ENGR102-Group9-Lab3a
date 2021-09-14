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

#pounds to newtons
def convertLbstoN(pounds):
  newtons = pounds * 4.448
  return (newtons // .01) / 100

#kilometers to miles
def convertKMtoMI(km):
  miles = km * .621371
  return (miles // .01) / 100

#atm to mmHg
def convertATMtoMMHG(atm):
  torr = atm * 760
  return (torr // .01) / 100

#Watts to BTU per hour
def convertWtoBTU(watts):
  btu = watts * 3.41
  return (btu // .01) / 100

#Liters per second to Gallons per minute
def convertLPStoGPM(lps):
  gpm = lps * 15.850323141489
  return (gpm // .01) / 100

#Degrees Celcius to Degrees Rankine
def convertCtoR(degreesC):
  degreesR = degreesC * (9/5) + 491.67
  return (degreesR // .01) / 100