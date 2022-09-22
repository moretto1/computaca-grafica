from OpenGL.GL import *
from OpenGL.GLUT import *


def Desenha():
    global P1x, P1y, P2x, P2y, P3x, P3y
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin (GL_TRIANGLES)
    glVertex2f(P1x,P1y)
    glVertex2f(P2x,P2y)
    glVertex2f(P3x,P3y)
    glEnd()
    glutSwapBuffers()

def Inicializa():
    glClearColor(0.0, 0.0, 1.0, 1.0)

def InicializaObjeto():
    global P1x, P1y, P2x, P2y, P3x, P3y
    P1x = 0
    P1y = 1
    P2x =-1
    P2y = 0
    P3x = 1
    P3y = 0
    glColor3f(1.0, 0.0, 0.0)

def Teclado(tecla, x, y):
    if tecla == 'r':
        InicializaObjeto()
    glutPostRedisplay()

# Rotina para tratamento de eventos relacionados ao mouse
# botao: Botao que foi pressionado.
# GLUT_LEFT_BUTTON, GLUT_RIGHT_BUTTON, GLUT_MIDDLE_BUTTON
# estado: bot�o clicado ou solto
# GLUT_UP ou GLUT_DOWN
# x,y: posicao do mouse dentro da janela
def  Mouse(botao, estado, x, y):
    glBegin(GL_POINTS)
    glColor3f(0.0,1.0,0.0)
    glPointSize(5.0)
    glVertex2f(0.0, 0.0)
    glEnd()
    if botao == GLUT_LEFT_BUTTON:
        glColor3f(1.0, 1.0, 0.0)
    elif botao == GLUT_RIGHT_BUTTON:
        glColor3f(0.0, 1.0, 1.0)
    glutPostRedisplay()

glutInit ()
glutInitDisplayMode(GLUT_RGBA)
glutCreateWindow("OpenGl com uso do Mouse")
glutKeyboardFunc(Teclado)
glutMouseFunc(Mouse)
glutDisplayFunc(Desenha)
Inicializa()
InicializaObjeto()
glutMainLoop()