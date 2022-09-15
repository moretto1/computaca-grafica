from OpenGL.GL import *
from OpenGL.GLUT import *

yps = 0.0

def desenho():
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_TRIANGLES)
	glVertex2f(-0.2,0.2)
	glVertex2f(0.0,yps)
	glVertex2f(0.2,0.2)
	glEnd()
	glutSwapBuffers()

def inicializa():
	glClearColor( 0.0, 0.0, 1.0, 1.0 )

def teclado(key,x,y):
	global yps
	if key == b'q':
		quit()
	if key == b'r':
		yps += -0.1
	glutPostRedisplay()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA)
	glutInitWindowSize(640,480)
	glutCreateWindow('Primeira Aplicacao OpenGL')
	glutKeyboardFunc(teclado)
	glutDisplayFunc(desenho)
	inicializa()
	glutMainLoop()
 
main()
