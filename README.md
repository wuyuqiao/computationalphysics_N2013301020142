# **Hello World !!**
------

## Introduction
This is the repository for computational physics course in the spring term of 2016 in Wuhan University. 
I will publish the homework here as well as some interesting programmes I wrote via Python 2.7.
If you want to give some suggestions or point out errors in my programmes, please contact me at chenfengwhu@gmail.com 

##Homework list
- [x] [1.Exercise_3 with all levels](https://raw.githubusercontent.com/chenfeng2013301020145/computational-physics_N2013301020145/master/Exercise/1st%20assignment.md)
- [ ] 2.
- [ ] 3.
- [ ] 4.
- [ ] 5.

##Todo list 
- [x] install linux 
- [x] Python compilers: Anaconda!
- [x] update vim: k-vim
- [ ] update the repository

##Code
```python
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 16:52:21 2016
@author: AF
"""

import turtle

def drawcircle(point,color,radius):
    turtle.pensize(15)
    turtle.penup()
    turtle.goto(point)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(radius)
    
def pointup(point):
    return (point[0],point[1]+10)
    
def rainbow(point,degree,radius):
    colormap = ['red','orange','yellow','green','blue','cyan','purple']
    if degree > 6:
           degree = 0
    drawcircle(point,colormap[degree],radius)
    if radius > 0:
       rainbow(pointup(point),degree+1,radius-20)
          

def main():
    degrees = 0
    myPoint = [0,-200]
    myRadius = 200
    myWin = turtle.Screen()
    rainbow(myPoint,degrees,myRadius)
    myWin.exitonclick()
    
main()

```

##Figure
![file-list](https://raw.githubusercontent.com/chenfeng2013301020145/computational-physics_N2013301020145/master/circle.png)

##Formula
$$E = mc^2$$

##Table
|something|items|another things|
|---------|----:|:------------:|
|   ABC   |\$   | 12345        |


