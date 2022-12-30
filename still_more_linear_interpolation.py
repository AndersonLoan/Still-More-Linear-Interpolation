# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name(s):         Saylor Sherrodd
#                   Ricardo Mejia
#                   Andrew Spears
#                   Spencer Torres
#                   Anderson Loan
# Section:         574
# Assignment:   3.16
# Date:         6 9 2022
#
from math import * 
#these will take in inputed values and store them for varialbes time 1, time 2, and their respective x,y, and z values
time_1 = float(input("Enter time 1:\n"))
t1_x = float(input('Enter the x position of the object at time 1:\n'))
t1_y = float(input("Enter the y position of the object at time 1:\n"))
t1_z = float(input("Enter the z position of the object at time 1:\n"))
time_2 = float(input("Enter time 2:\n"))
t2_x = float(input("Enter the x position of the object at time 2:\n"))
t2_y = float(input("Enter the y position of the object at time 2:\n"))
t2_z = float(input("Enter the z position of the object at time 2:\n"))

#this calculates the changes in the x,y,and z between each time interval
change_in_x = (t2_x - t1_x)/4
change_in_y = (t2_y - t1_y)/4
change_in_z = (t2_z - t1_z)/4
#this will calculate the change in time per interval
change_in_time = (time_2-time_1) / 4

while time_1 <= time_2:
    print(f"At time {time_1:.2f} seconds the object is at ({t1_x:.3f}, {t1_y:.3f}, {t1_z:.3f})")
    t1_x = t1_x + change_in_x
    t1_y = t1_y + change_in_y
    t1_z = t1_z + change_in_z
    time_1 = time_1 + change_in_time
    
    

