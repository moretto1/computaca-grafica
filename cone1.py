# Prática #6 - tem como objetivo exemplificar a visualizacao de objetos 3D.
# Programa cone.py
# OBS.: prog. baseado nos exemplos disponнveis no livro
# "OpenGL SuperBible", 2nd Edition, de Richard S. e Wright Jr.
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


obsX=0.0
obsY=0.0
obsZ=50.0
angle=0.0
fAspect=1.0

# Funзгo callback chamada para fazer o desenho
def desenha():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)          # determina a cor corrente de desenho
    glutWireCone(20.0, 50.0, 20, 10)  # Desenha cone modelado em wireframe
    glutSwapBuffers()                 # Executa os comandos OpenGL


# Inicializa parвmetros de exibiзгo
def inicializa():
    global angle
    glClearColor(0.8, 0.8, 0.8, 1.0)
    angle=45


# Funзгo usada para especificar o volume de visualizaзгo
def parametrosVis3D():
    global angle, fAspect
    glMatrixMode(GL_PROJECTION)          # Especifica sistema de coordenadas de projeзгo
    glLoadIdentity()                     # Inicializa sistema de coordenadas de projeзгo
    gluPerspective(angle,fAspect,0.5,200)# Especifica a projeзгo perspectiva
    glMatrixMode(GL_MODELVIEW)           # Especifica sistema de coordenadas do modelo
    glLoadIdentity()                     # Inicializa sistema de coordenadas do modelo
    gluLookAt(200.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0)  # Especifica posicao do observador e do ponto de foco


# Callback para gerenciar eventos do teclado para teclas especiais
def teclado (key, x, y):
    global obsX, obsY, obsZ
    if key==GLUT_KEY_LEFT :
        obsX -=10
    if key==GLUT_KEY_RIGHT :
        obsX +=10
    if key==GLUT_KEY_UP :
        obsY +=10
    if key==GLUT_KEY_DOWN :
        obsY -=10
    if key==GLUT_KEY_HOME :
        obsZ +=10
    if key==GLUT_KEY_END :
        obsZ -=10
    glLoadIdentity()
    gluLookAt(obsX,obsY,obsZ, 0.0,0.0,0.0, 0.0,1.0,0.0)
    glutPostRedisplay()


# Funзгo callback chamada quando o tamanho da janela й alterado 
def redimensiona(w, h):
    global fAspect
    if h == 0:
        h = 1               # Para previnir uma divisгo por zero
    glViewport(0, 0, w, h)  # Especifica o tamanho da viewport
    fAspect = float(w/h)    # Calcula a correзгo de aspecto
    parametrosVis3D()


# Funзгo callback chamada para gerenciar eventos do mouse
def mouse(button, state, x, y):
    global angle
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:         # Zoom-in
            if angle >= 10:
                angle -= 5
		
    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:          # Zoom-out
            if angle <= 130:
                angle += 5
		
    parametrosVis3D()
    glutPostRedisplay()


# Programa Principal
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(800,800)
    glutCreateWindow("Visualizacao 3D")
    glutDisplayFunc(desenha)
    glutReshapeFunc(redimensiona)
    glutMouseFunc(mouse)
    glutSpecialFunc(teclado)
    inicializa()
    glutMainLoop()


main()
