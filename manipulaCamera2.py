#objetivo exemplificar a visualizacao de objetos 3D.
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

PI = 3.1415926535897932384626433832795
angulo = 0
angle = 0.0
fAspect = 1.0
upx = 0
upy = 1
upz = 0
eyex = 0.0
eyey = 0.0
eyez = 100.0


def desenha():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0)      
    glutWireTorus(2,6,10,10)
    glColor3f(1.0, 0.0, 0.0)   

    glPushMatrix()
    glTranslatef(-25, 0.0,0.0)
    glutWireTeapot(5)
    glPopMatrix()
    
    glColor3f(1.0, 0.0, 1.0)   
    glPushMatrix()
    glTranslatef(25.0, 0.0,0.0)
    glutWireSphere(5,10,10)
    glPopMatrix()
    glutSwapBuffers()       


def inicializa():
    global angle
    glClearColor(0.8, 0.8, 0.8, 1.0)
    angle = 45


def parametrosVis3D():
    global angle, faspect, upx, upy, upz, eyex, eyey, eyez
    glMatrixMode(GL_PROJECTION)          # Especifica sistema de coordenadas de projecao
    glLoadIdentity()                     # Inicializa sistema de coordenadas de projecao
    gluPerspective(angle,fAspect,0.5,500)# Especifica a projecao perspectiva
    #glFrustum(-1,1 ,-1 ,1 , 0.5, 200)
    #glOrtho(-40,40,-40,40,-60,60)
    glMatrixMode(GL_MODELVIEW)           # Especifica sistema de coordenadas do modelo
    glLoadIdentity()                     # Inicializa sistema de coordenadas do modelo
    gluLookAt(eyex,eyey,eyez, 0,0,0, upx,upy,upz)    # Especifica posicao do observador e do ponto de foco ou alvo


# Funcao callback chamada quando o tamanho da janela eh alterado
def redimensiona(w, h):
    global fAspect
    if h == 0:
        h = 1                       # Para previnir uma divisao por zero
    glViewport(0, 0, w, h)          # Especifica o tamanho da viewport
    fAspect = float(w/h)            # Calcula a correcao de aspecto
    parametrosVis3D()


# Funcao callback chamada para gerenciar eventos do mouse
def mouse(button, state, x, y):
    global angle
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:         # Zoom-in
            if angle >= 10:
                angle -= 5

    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:           # Zoom-out
            if angle <= 130:
                angle += 5
    parametrosVis3D()
    glutPostRedisplay()


def teclado(tecla, x, y):
    global eyex, eyey, eyez, angle, angulo
    if tecla == b'q':
        eyex = 0.0
        eyey = 0.0
        eyez = 100.0
        angle = 45
        angulo = 0.0
    if tecla == b'e':
        eyez = 0
        if angulo <= (2*PI):
            angulo += PI/6
        else:
            angulo = 0
        eyex = 100 * cos(angulo)
        eyey = 100 * sin(angulo)
    if tecla == b'r':
        eyex = 0
        if angulo <= (2*PI):
            angulo += PI/6
        else:
            angulo = 0
        eyez= 100 * cos(angulo)
        eyey= 100 * sin(angulo)
    if tecla == b'a':
        eyey = 0
        if angulo <= (2*PI):
            angulo += PI/6
        else:
            angulo = 0.0
        eyex= 200 * cos(angulo)
        eyez= 200 * sin(angulo)
    parametrosVis3D()
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600,600)
    glutCreateWindow("Visualizacao 3D")
    glutDisplayFunc(desenha)
    glutReshapeFunc(redimensiona)
    glutMouseFunc(mouse)
    glutKeyboardFunc(teclado)
    inicializa()
    glutMainLoop()


main()