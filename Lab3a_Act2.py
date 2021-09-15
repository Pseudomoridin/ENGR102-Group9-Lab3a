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

# positions will be stored in lists ordered x, y, z
# points will be stored in a dictionary containing the time and position
# functions are parametric

def interpolate(point1, point2):
  timediff = (point2["time"] - point1["time"])
  timediffstep = timediff / 4.0
  xslope = (point2["position"][0] - point1["position"][0]) / timediff
  xint = - (point2["time"]*xslope) + point2["position"][0]
  yslope = (point2["position"][1] - point1["position"][1]) / timediff
  yint = - (point2["time"]*yslope) + point2["position"][1]
  zslope = (point2["position"][2] - point1["position"][2]) / timediff
  zint = - (point2["time"]*zslope) + point2["position"][2]
  pointlist = []
  print(xslope,yslope,zslope)
  for x in range (5):
    temppoint = {
      "time":point1["time"] + (x * timediffstep), # time works, this gives the correct time at the point
      "position":[
        xslope * (point1["time"] + (x * timediffstep)) + xint,
        yslope * (point1["time"] + (x * timediffstep)) + yint,
        zslope * (point1["time"] + (x * timediffstep)) + zint,
      ]
    }
    pointlist.append(temppoint)
  return pointlist


position1 = [0,0,0]
point1 = {"position":position1}
position2 = [0,0,0]
point2 = {"position":position2}

point1["time"] = float(input("Enter time 1: "))
point1["position"][0] = float(input("Enter the x position of the object at time 1: "))
point1["position"][1] = float(input("Enter the y position of the object at time 1: "))
point1["position"][2] = float(input("Enter the z position of the object at time 1: "))

point2["time"] = float(input("Enter time 2: "))
point2["position"][0] = float(input("Enter the x position of the object at time 2: "))
point2["position"][1] = float(input("Enter the y position of the object at time 2: "))
point2["position"][2] = float(input("Enter the z position of the object at time 2: "))

print(interpolate(point1, point2))
