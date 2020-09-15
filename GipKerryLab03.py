#
# Name: Kerry Gip
# Class: CSCI 1411-004
# Due Date: 9/8/2020
# Description: Code that demonstrates the difference between floating point division and integer division

import math

def main():
    print("You want to build a box and put trim around it ")
    print("So we're gonna need supplies")
    length = eval(input("What is the length of your box in inches? "))
    print("Your length is ", length, "in.")
    width = eval(input("What is the width of your box in inches? "))
    print("Your width is ", width, "in.")
    print()
    print()
    trim = 1.88
    perimeter = 2*length + 2*width
    print("Your perimeter is ",perimeter, "in.")
    print("The trim costs $1.88 for a 12in segment")
    trim_perim = float(perimeter/12)
    trim_perim_rounded = round(trim_perim,2)
    trim_perim_int = math.ceil(perimeter/12)
    print()
    print()
    print("It would take exactly ", trim_perim_rounded, " or roughly ", trim_perim_int,"segments to go around the box")
    print("You need to buy whole pieces so you need to buy ", trim_perim_int, "pieces")
    area = trim_perim_int*trim
    areas = round(area,2)
    print("That would cost you $", areas)
    difference = round(trim_perim_int- trim_perim, 2)
    dollars_lost = round(difference * trim,2)
    print("Becaues you have an oddly shaped box, you wasted", difference, "inches of trim", "which equates to a $",
        dollars_lost, " loss since you couldn't buy full segments")
    
    
main()    