from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import OpenGL.GLUT as glut

texto = "OPENGL"
xis = 0.0
yps = 0.0
larguraJan = 800
alturaJan = 600

def escreveTela(xPos, yPos, string):
	glRasterPos2f(xPos,yPos)
	for i in range(len(string)):
 		glut.glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(string[i]))

def inicializa():
	glClearColor(0.9, 0.9, 0.9, 1.0) 

def desenha():
	global texto, xis, yps
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0, 0.0, 0.0)
	escreveTela(xis, yps, texto)
	glutSwapBuffers()

# Funcao callback chamada quando o tamanho da janela eh alterado 
def controlaTamanhoJanela(w, h):
	global larguraJan, alturaJan
	larguraJan = w
	alturaJan = h
##	print(larguraJan,alturaJan)

def mouse(botao, estado, x, y):
	global xis, yps, larguraJan, alturaJan
	if botao == GLUT_LEFT_BUTTON:
		xis = (2*x)/larguraJan - 1  ##converte x do SRD em x do SRU 
		yps = (2*-y)/alturaJan + 1  ##converte y do SRD em y do SRU
	glutPostRedisplay()

def main():
	glutInit ()
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(800,600)
	glutCreateWindow("Exemplo uso de texto")
	glutReshapeFunc(controlaTamanhoJanela)
	glutMouseFunc(mouse)
	inicializa()
	glutDisplayFunc(desenha)
	glutMainLoop()

main()
