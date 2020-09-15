#File GipKerryLab004b.py
#This will be a continuation of lab004a.py
#We will be prompting the user to draw circles
#and moving them around

import graphics
from graphics import*
import time

def main():
    #draws the window
    win=GraphWin("Lab004-GipKerry", 500,500)
    win.setBackground("Black")

    #user input of color, center and radius for circle1
    color1 = input("What color do you want circle 1 to be? ")
    x1,y1 = eval(input("What are the x,y coordinates of the center circle?\n"
                       "Use a comma inbetween x and y "))
    radius1 = eval(input("What is the radius of circle1? "))             
    

    #drawing circle 1
    center1 = Point(x1,y1)
    circ1 = Circle(center1, radius1)
    circ1.setFill(color1)
    circ1.draw(win)

    #circle 2
    print("The 2nd circle will be a green circle above the first,\n"
          "with a distance twice the radius of the first circle")
    radius2 = 0.5*radius1
    x2,y2=(x1,y1-(2*radius1))
    center2 = Point(x2,y2)
    circ2=Circle(center2, radius2)
    circ2.setFill("green")
    circ2.draw(win)

    #draw a red line between the two circles
    line=Line(center1,center2)
    line.setFill("red")
    line.draw(win)

    print("When you click, the circle should move to the right at 90 degrees")

    #add a mouseclick function
    win.getMouse()

    #move circle 90 degrees to the right and draw line to it
    line.undraw()
    circ2.move(2*radius1, 2*radius1)
    #get new center
    RightCenter = circ2.getCenter()
    #draw new line
    line=Line(RightCenter, center1)
    line.setFill("red")
    line.draw(win)

    print("When you click again, the circle should move down at 90 degrees")

    #move circle 90 degrees down and draw line to it
    win.getMouse()
    line.undraw()
    circ2.undraw()
    #circ2.move(x1-8.9*radius1, y1-5*radius1)
    x3,y3=(x1,y1+2*radius1)
    center3= Point(x3,y3)
    circ3=Circle(center3,radius2)
    circ3.setFill("green")
    circ3.draw(win)
    
    #get new center
    #DownCenter = circ2.getCenter()
    
    #draw new line
    line=Line(center3, center1)
    line.setFill("red")
    line.draw(win)

    print("When you click again, the circle should move left at 90 degrees")

    #move circle 90 degrees left and draw line to it
    win.getMouse()
    line.undraw()
    circ3.undraw()

    #draw next circle
    x4,y4=(x1-2*radius1,y1)
    center4= Point(x4,y4)
    circ4=Circle(center4,radius2)
    circ4.setFill("green")
    circ4.draw(win)

    #draw line
    line=Line(center4, center1)
    line.setFill("red")
    line.draw(win)

    #move circle back to start and draw a line to it
    win.getMouse()
    line.undraw()
    circ4.undraw()

    #draw start circle
    x2,y2=(x1,y1-(2*radius1))
    center2 = Point(x2,y2)
    circ2=Circle(center2, radius2)
    circ2.setFill("green")
    circ2.draw(win)

    #draw a red line between the two circles
    line=Line(center1,center2)
    line.setFill("red")
    line.draw(win)


    


main()
