from graphics import *
from Arc import *

def main():
    win = GraphWin("My Circle", 1000, 1000)
    rect = Rectangle(Point(200, 300), Point(600, 200))
    rect.setFill("orange")
    rect.draw(win)
    rect = Rectangle(Point(200, 300), Point(600, 400))
    rect.setFill("white")
    rect.draw(win)
    rect = Rectangle(Point(200, 400), Point(600, 500))
    rect.setFill("green")
    rect.draw(win)
    rect = Rectangle(Point(180, 200), Point(200, 900))
    rect.setFill("black")
    rect.draw(win)
    rect = Rectangle(Point(150, 900), Point(230, 920))
    rect.setFill("brown")
    rect.draw(win)
    rect = Rectangle(Point(130, 920), Point(250, 940))
    rect.setFill("brown")
    rect.draw(win)
    rect = Rectangle(Point(110, 940), Point(270, 960))
    rect.setFill("brown")
    rect.draw(win)
    c = Circle(Point(400,350), 50)
    c.draw(win)
    c.setOutline('black')
    c.setFill('blue')
main()