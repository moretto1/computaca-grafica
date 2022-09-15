from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def tower():
    glBegin(GL_LINES)
    glVertex2f(-25, 0)
    glVertex2f(25, 0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0, 75)
    glVertex2f(0, 0)
    glEnd()


def draw_disc_1():
    glBegin(GL_POLYGON)
    glVertex2f(-17, 10)
    glVertex2f(17, 10)
    glVertex2f(17, 0)
    glVertex2f(-17, 0)
    glEnd()


def draw_disc_2():
    glBegin(GL_POLYGON)
    glVertex2f(-12, 10)
    glVertex2f(12, 10)
    glVertex2f(12, 0)
    glVertex2f(-12, 0)
    glEnd()


def draw_disc_3():
    glBegin(GL_POLYGON)
    glVertex2f(-7, 10)
    glVertex2f(7, 10)
    glVertex2f(7, 0)
    glVertex2f(-7, 0)
    glEnd()


def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(6)
    glPushMatrix()
    glTranslatef(-70, 0, 0)
    tower()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0, 0, 0)
    tower()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(70, 0, 0)
    tower()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-70, 0, 0)

    glColor3f(1.0, 0.0, 0.0)
    draw_disc_1()

    glColor3f(0.0, 1.0, 0.0)
    glPushMatrix()
    glTranslatef(0, 10, 0)
    draw_disc_2()
    glPopMatrix()

    glColor3f(0.0, 0.0, 1.0)
    glPushMatrix()
    glTranslatef(0, 20, 0)
    draw_disc_3()
    glPopMatrix()

    glPopMatrix()

    glutSwapBuffers()


def init():
    glClearColor(0.8, 0.8, 0.8, 0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(-100, 100, -100, 100)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(640, 480)
    glutCreateWindow('Torre de Hanoi')
    glutDisplayFunc(draw)
    init()
    glutMainLoop()


main()
