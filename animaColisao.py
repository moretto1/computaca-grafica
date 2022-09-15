from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

xis = 0.0
yps = 0.0
desloca = 0.1
fogo = False
move = False

def inicializacao():
    glClearColor (0.8, 0.8, 0.8, 0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(-10.0,10.0,-10.0,10.0) #manipula dim do SRU (xmim, xmax, ymin, xmax)

def trave():
    glBegin(GL_POLYGON)
    glVertex2f(-0.5,1.5)
    glVertex2f(0.5,1.5)
    glVertex2f(0.5,-1.5)
    glVertex2f(-0.5,-1.5)

def desenha():
    global xis,yps
    glClear (GL_COLOR_BUFFER_BIT)
    #TRAVE
    glColor3f(0.0,0.7,0.0)
    glPushMatrix()
    glTranslatef(0.0,yps,0.0)
    glTranslatef(10.0,0.0,0.0)
    trave()
    glEnd()
    glPopMatrix()
    #TRAVE
    glColor3f(0.0,0.7,0.0)
    glPushMatrix()
    glTranslatef(0.0,yps,0.0)
    glTranslatef(-10.0,0.0,0.0)
    trave()
    glEnd()
    glPopMatrix()
    #BOLA
    glColor3f(0.0,0.0,0.0)
    glPushMatrix()
    glTranslatef(xis,0.0,0.0)
    glTranslatef(0.0,0.0,1.0)
    glutSolidSphere(0.5,100,100)
    glPopMatrix()
    glutSwapBuffers()  #utilizada com GLUT_SINGLE

def Teclado(tecla,x,y):
    global fogo,move
    if tecla == b'q':
        exit()
    if tecla == b't':
        fogo = not(fogo)
    if tecla == b'T':
        move = not(move)
    glutPostRedisplay()

def animaBola(valor):
    global xis,fogo
    if valor:
        if xis < 10:
            xis += 0.1
        else:
            xis = -10.0
    glutPostRedisplay()
    glutTimerFunc(20,animaBola,fogo)


def animaTrave(valor):
    global yps,desloca,xis
    if(valor):
        if yps < 10 and yps > -10:
            yps += desloca
        else:
            yps -= desloca
            desloca *= -1
        if yps<2.5 and yps >-0.55 and xis>8.0:
            if desloca > 0:
                yps = -0.5
            else:
                yps = 2.5
                desloca *= -1
                #print(f"xis = {xis} e yps= {yps}\n")
    glutPostRedisplay()
    glutTimerFunc(20,animaTrave,move)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode (GLUT_RGBA)
    glutInitWindowSize (800,600)
    glutCreateWindow ("Exemplos de Animacao")
    glutTimerFunc(100,animaBola,fogo)
    glutTimerFunc(100,animaTrave,move)
    glutDisplayFunc (desenha)
    glutKeyboardFunc(Teclado)
    inicializacao()
    glutMainLoop()

main()

