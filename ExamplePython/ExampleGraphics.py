# -*- coding: utf-8 -*-
import graphics
from graphics import *

if __name__ == '__main__':
    win = GraphWin("My Circle", 100, 100)
    c = Circle(Point(50 , 50), 20)
    c.draw(win)
    win.getMouse()
    win.close()                 # 지정된 창 "win" 에 원을 그리는 프로그램

    win = GraphWin("My Point", 300, 300)
    win.plot(50, 70, "blue")
    win.getMouse()
    win.close()                 # 지정된 창 "win" 에 점을 찍는 프로그램

    win = GraphWin("Set Background", 300, 300)
    win.setBackground("blue")
    win.getMouse()
    win.close()                 # 지정된 창 "win" 의 배경색을 파랑색으로 바꾸는 프로그램

    win = GraphWin("Get Point", 300, 300)
    clickPoint = win.getMouse()
    print str(clickPoint)
    win.close()

    #마우스로 지정된 두개의 좌표값을 받고, 선의 기울기를 찾는 프로그램

    win = GraphWin("기울기 그래프", 300, 300)
    pointA = win.getMouse()
    pointB = win.getMouse()
    win.close()
    print "A 의 좌표는 " + str(pointA) + " 입니다"
    print "B 의 좌표는 " + str(pointB) + " 입니다"
    slope = (pointA.y - pointB.y) / (pointA.x - pointB.x)
    print "두 점을 연결시키는 선의 기울기는  " + str(slope) + " 입니다"

    win = GraphWin("텍스트 입력", 300, 300)
    character = win.getKey()
    print character             # 창을 띄운 후 키가 입력되면 키의 값을 리턴받는 class

    win = GraphWin("텍스트 출력", 300, 300)
    message = Text(Point(3,4), "Hello!")
    message.setText("Hello")

