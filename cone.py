from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle = 0.0
fAspect = 1.0
upx = 0
upy = 1
upz = 0
eyex = 0.0
eyey = -200.0
eyez = -200.0


def desenha():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)            # determina a cor corrente de desenho
    glutWireCone(20.0, 50.0, 20, 10)      # Desenha cone modelado em wireframe
    glutSwapBuffers()                     # Executa os comandos OpenGL


def parametrosVis3D():
    global angle, faspect, upx, upy, upz, eyex, eyey, eyez
    glMatrixMode(GL_PROJECTION)                     # Especifica sistema de coordenadas de projecao
    glLoadIdentity()                                # Inicializa sistema de coordenadas de projecao
    gluPerspective(angle,fAspect,0.5,500)           # Especifica a projecao perspectiva
    glMatrixMode(GL_MODELVIEW)                      # Especifica sistema de coordenadas do modelo
    glLoadIdentity()                                # Inicializa sistema de coordenadas do modelo
    gluLookAt(eyex,eyey,eyez,0.0,0.0,0.0, upx,upy,upz)   # Especifica posicao do observador e do ponto de foco ou alvo


def inicializa():
    global angle
    glClearColor(0.8,  0.8,  0.8, 1.0)
    angle = 70


def redimensiona(w,h):
    global fAspect
    if h == 0:
        h = 1                           # Para previnir uma divisao por zero
    glViewport(0, 0, w, h)              # Especifica o tamanho da viewport
    fAspect = float(w/h)                # Calcula a correcao de aspecto
    parametrosVis3D()


def mouse(button,state,x,y):
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

def teclado(tecla, x, y):
    global eyex, eyey, eyez, upx, upy, upz
    if tecla == b'r':
        if eyey < 200 and eyez == 200:
            eyey += 10
            print(f"1- eyex={eyex}, eyey={eyey} e eyez={eyez}")
            upx = 0
            upy = 1
            upz = 0
        if eyey == 200 and eyez > -200:
            eyez -= 10
            print(f"2- eyex={eyex}, eyey={eyey} e eyez={eyez}")
            upx = 0
            upy = 1
            upz = 0
        if eyey > -200 and eyez == -200:
            eyey -= 10
            print(f"3- eyex={eyex}, eyey={eyey} e eyez={eyez}")
            upx = 0
            upy = 1
            upz = 0
        if eyey == -200 and eyez < 200:
            eyez += 10
            print(f"3- eyex={eyex}, eyey={eyey} e eyez={eyez}")
            upx = 0
            upy = 1
            upz = 0
    parametrosVis3D()
    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(800,600)
    glutCreateWindow("Visualizacao 3D")
    glutDisplayFunc(desenha)
    glutReshapeFunc(redimensiona)
    glutMouseFunc(mouse)
    glutKeyboardFunc(teclado)
    inicializa()
    glutMainLoop()


main()