import socket
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

sys.setrecursionlimit(999999)


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPointSize(1.0)
    gluOrtho2D(0, 500.0, 500.0, 0)

def drawDDA(x1,y1,x2,y2):
    glColor3f(0.0, 1.0, 0.0)
    dx = x2-x1
    dy = y2-y1
    x,y = x1,y1

    length = dx if abs(dx)>abs(dy) else dy
    length = abs(length)
    if dx == dy == 0:
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(x, y)
        return
    xinc = dx/float(length)
    yinc = dy/float(length)
    glVertex2f(x,y)

    for i in range(int(length)):
        x += xinc
        y += yinc
        glVertex2f(x,y)
    glColor3f(1.0, 0.0, 0.0)

class point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def subdivide(a,b,t):
    c = point(0,0)
    c.x = a.x +(b.x-a.x)*t
    c.y = a.y +(b.y-a.y)*t
    return c

def bezier(points,t):

    subpoint = []
    for i in range(len(points)-1):
        subpoint.append(subdivide(points[i],points[i+1],t))

    if len(subpoint)==1:
        return subpoint[0]

    return bezier(subpoint,t)

def write_text(point):
    glColor3f(0, 1, 1)
    glWindowPos2d(point.x,500-point.y)
    string = [point.x,point.y]
    string = str(string)
    for ch in string:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ctypes.c_int(ord(ch)))
    glColor3f(1.0, 0.0, 0.0)


def Display():
    global points1,p,drawn1,points2,drawn2
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)

    for i in range(len(points1)):
        write_text(points1[i])
    glBegin(GL_POINTS)

    for  i in range(0,1000+50*len(points1)):
        t = i/(999.0+50*len(points1))
        p = bezier(points1,t)
        glVertex2f(p.x,p.y)


    for i in range(len(points1)-1):
        drawDDA(points1[i].x,points1[i].y,points1[i+1].x,points1[i+1].y)



    glEnd()
    glFlush()
    glutPostRedisplay()



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)

    global points1, p ,drawn1,points2,drawn2

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(("localhost", 12345))

    msg = b"graphics"

    print(b"client sending: " + msg)
    clientsocket.send(msg)

    msg = clientsocket.recv(1024)
    print(msg.decode("utf-8"))
    points1= []
    lst = eval(msg.decode("utf-8"))
    for i in lst:
        points1.append(point(i[0],i[1]))
    drawn1=3
    p = point(0,0)
    drawn1 = 0
    drawn2 = 0
    glutCreateWindow(b'bezier curve')
    glutDisplayFunc(Display)
    init()
    glutMainLoop()


main()
#socket.SOCK_STREAM indicates TCP
