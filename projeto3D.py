#objetivo exemplificar a visualizacao de objetos 3D.
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

PI = 3.1415926535897932384626433832795
projecao = True
fogo = False
angulo = 0
angle = 0.0
fAspect = 1.0
upx = 0
upy = 1
upz = 0
eyex = 0.0
eyey = 0.0
eyez = 100.0
xis = 0.0
yps = 0.0
zhe = 0.0
Xmin = -100
Xmax = 100
Ymin = -100
Ymax = 100
Zmin = -200
Zmax= 200
def desenha():
    global xis, yps, zhe
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.5, 0.5)
    glPushMatrix()
    glTranslatef(xis,yps,zhe)
    glutWireSphere(10,20,20)
    glPopMatrix()
    glutSwapBuffers()       


def inicializa():
    global angle
    glClearColor(0.95, 0.95, 0.95, 1.0)
    angle = 55


def parametrosVis3D():
    global projecao, angle, faspect, upx, upy, upz, eyex, eyey, eyez
    global Xmin, Xmax, Ymin, Ymax, Zmin, Zmax
    glMatrixMode(GL_PROJECTION)          # Especifica sistema de coordenadas de projecao
    glLoadIdentity()                     # Inicializa sistema de coordenadas de projecao
    if projecao == True:
        gluPerspective(angle,fAspect,0.5,500)# Especifica a projecao perspectiva
    else:
        glOrtho(Xmin,Xmax,Ymin,Ymax,Zmin,Zmax)
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

def animaBola(valor):
    global xis,fogo
    if valor:
        if xis < 100:
            xis += 1
        else:
            xis = -100.0
    glutPostRedisplay()
    glutTimerFunc(20,animaBola,fogo)

# Funcao callback chamada para gerenciar eventos do mouse
def mouse(button, state, x, y):
    global angle, Xmin, Xmax, Ymin, Ymax, Zmin, Zmax
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:         # Zoom-in
            if angle >= 10:
                angle -= 5
            Xmin -= 10
            Xmax += 10
            Ymin -= 10
            Ymax += 10
            Zmin -= 10
            Zmax += 10
    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:           # Zoom-out
            if angle <= 130:
                angle += 5
            Xmin += 10
            Xmax -= 10
            Ymin += 10
            Ymax -= 10
            Zmin += 10
            Zmax -= 10
    parametrosVis3D()
    glutPostRedisplay()


def teclado(tecla, x, y):
    global projecao, fogo, eyex, eyey, eyez, angle, angulo, PI
    if tecla == b'p':
        projecao = not(projecao)
    if tecla == b't':
        fogo = not(fogo)
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
    glutCreateWindow("Movimentacao 3D")
    glutDisplayFunc(desenha)
    glutTimerFunc(100,animaBola,fogo)
    glutReshapeFunc(redimensiona)
    glutMouseFunc(mouse)
    glutKeyboardFunc(teclado)
    inicializa()
    glutMainLoop()


main()