import math

radius = float(input("What is the radius of your circle? ")) # I couldnt get PI from the built in library :(
pi = math.pi
area = pi*radius**2
print("Area =", round(area,2))
