"""
 Um programa OpenGL simples que abre uma janela GLUT 
 e desenha dois objetos iluminados por 3 fontes de luz spot.
 Além dos objetos há um tabuleiro que não permite que a luz passe.
 Navegacao via botoes do mouse + movimento:
 - botao esquerdo: rotaciona objeto
 - botao direito:  aproxima/afasta
 - botao do meio:  translada objeto

 Teclas Home e End fazem zoom in/zoom out
 Teclas 0, 1 e 2 devem ser usadas para escolher a fonte de luz desejada (verde, vermelha ou azul)
 Setas movem fonte de luz em x e y
 PageUp/PageDown movem fonte de luz em z

 Marcelo Cohen e Isabel H. Manssour
 Este codigo acompanha o livro
 "OpenGL - Uma Abordagem Pratica e Objetiva"

"""
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Variaveis para controles de navegacao

TAM = 40  # define TAM 40
D = 2  # define D 2
angle = 0.0
fAspect = 0.0
rotX = 0.0
rotY = 0.0
rotX_ini = 0.0
rotY_ini = 0.0
obsX = 0.0
obsY = 0.0
obsZ = 0.0
obsX_ini = 0.0
obsY_ini = 0.0
obsZ_ini = 0.0
x_ini = 0
y_ini = 0
bot = 0
luz = 0 # Luz selecionada
posLuz = [[-10.0, 30.0, 10.0, 1.0],[0.0, 30.0, 10.0, 1.0],[10.0, 30.0, 10.0, 1.0 ]] # Posicao de cada luz
dirLuz = [[0.0,-1.0,0.0],[0.0,-1.0,0.0],[ 0.0,-1.0,0.0]]    # Direcao de cada luz
luzDifusa = [[1.0,0.0,0.0,1.0 ],[ 0.0,1.0,0.0,1.0 ],[ 0.0,0.0,1.0,1.0 ]]  # Cor difusa de cada luz #RGB
luzEspecular= [[1.0,0.0,0.0,1.0],[0.0,1.0,0.0,1.0],[0.0,0.0,1.0,1.0]]     # Cor especular de cada luz #RGB
SENS_ROT = 5.0
SENS_OBS = 10.0
SENS_TRANSL = 10.0


# Funcao responsavel pela especificacao dos parametros de iluminacao
def defineIluminacao():
	global posLuz, dirLuz, luzDifusa, luzEspecular
	luzAmbiente= [0.2,0.2,0.2,1.0]
	especularidade = [0.5,0.5,0.5,1.0] # Capacidade de brilho do material
	especMaterial = 90
	glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade) # Define a refletancia do material
	glMateriali(GL_FRONT,GL_SHININESS,especMaterial) # Define a concentracao do brilho
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente) # Ativa o uso da luz ambiente
	cont = 0
	while cont < 3: # Define os parametros das fontes de luz
		glLightfv(GL_LIGHT0 + cont, GL_AMBIENT, luzAmbiente)
		glLightfv(GL_LIGHT0 + cont, GL_DIFFUSE, luzDifusa[cont] )
		glLightfv(GL_LIGHT0 + cont, GL_SPECULAR, luzEspecular[cont] )
		glLightfv(GL_LIGHT0 + cont, GL_POSITION, posLuz[cont] )
		glLightfv(GL_LIGHT0 + cont, GL_SPOT_DIRECTION,dirLuz[cont])
		glLightf(GL_LIGHT0  + cont, GL_SPOT_CUTOFF,40.0)
		glLightf(GL_LIGHT0  + cont, GL_SPOT_EXPONENT,10.0)
		#print(GL_LIGHT0 + cont)
		cont = cont + 1



# Funcao para desenhar um "chao" no ambiente
def desenhaChao():
	global D, TAM
	flagx = True  # Flags para determinar a cor de cada quadrado
	flagz = True
	x = 0.0
	z = 0.0
	glNormal3f(0.0,1.0,0.0)# Define a normal apontando para cima
	glBegin(GL_QUADS)
	flagx = False
	x = -TAM
	while x < TAM: # X varia de -TAM a TAM, de D em D
		if flagx == True:   # Flagx determina a cor inicial
			flagz = False
		else:
			flagz = True
		z = -TAM
		while z < TAM: # Z varia de -TAM a TAM, de D em D
			if flagz == True:			# Escolhe cor
				glColor3f(0.4,0.4,0.4)
			else:
				glColor3f(1.0,1.0,1.0)
			# E desenha o quadrado
			glVertex3f(x,0.0,z)
			glVertex3f(x+D,0.0,z)
			glVertex3f(x+D,0.0,z+D)
			glVertex3f(x,0.0,z+D)
			flagz = not(flagz) # Alterna cor
			z += D
		flagx = not(flagx)		# A cada coluna, alterna cor inicial
		x += D
	glEnd()



def desenha():
	cont = 0
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)# Limpa a janela de visualizacao com a cor de fundo definida previamente
	defineIluminacao()	# Chama a funcao que especifica os parametros de iluminacao
	glDisable(GL_LIGHTING)	# Desabilita a iluminacao para desenhar as esferas
	while cont < 3:   # Desenha "esferas" nas posicoes das fontes de luz
		glPushMatrix()
		glTranslatef(posLuz[cont][0],posLuz[cont][1],posLuz[cont][2])
		glColor3f(luzDifusa[cont][0],luzDifusa[cont][1],luzDifusa[cont][2])
		glutSolidSphere(1.5,20,10)
		glPopMatrix()
		cont = cont + 1
	glEnable(GL_LIGHTING) # Habilita iluminacao novamente
	glColor3f(1.0,1.0,1.0)	# Altera a cor do desenho para branco
	glPushMatrix() # Desenha o teapot e o chao
	#glTranslatef(-20.0,7.5,0.0)
	glRotatef(-90,1,0,0)
	glTranslatef(-30.0,7.5,0.0)
	glutSolidCone(2,40,20,20)
	glPopMatrix()
	
	glPushMatrix()
	glRotatef(-90,1,0,0)
	glTranslatef(-30.0,7.5,0.5)
	glutSolidTorus(2, 16, 16, 16)
	glPopMatrix()

	glPushMatrix()
	glRotatef(-90,1,0,0)
	glTranslatef(-30.0,7.5,7.0)
	glutSolidTorus(2, 12, 12, 12)
	glPopMatrix()

	glPushMatrix()
	glRotatef(-90,1,0,0)
	glTranslatef(-30.0,12.0,12.0)
	glutSolidTorus(2, 7, 7, 7)
	glPopMatrix()

	glPushMatrix()
	glRotatef(-90,1,0,0)
	glTranslatef(0.0,7.5,0.0)
	glutSolidCone(2,40,20,20)
	glPopMatrix()


	glPushMatrix()
	glRotatef(-90,1,0,0)
	glTranslatef(30.0,7.5,0.0)
	glutSolidCone(2,40,20,20)
	glPopMatrix()

	# glPushMatrix()
	# glTranslatef(30.0,7.5,0.0)
	# glutSolidCone(2,70,20,20)

	#glutSolidTorus(2,20, 20, 20)
	#glPopMatrix()
	desenhaChao()
	glutSwapBuffers() # Executa os comandos OpenGL


def posicionaObservador():
	global rotX, rotY, obsX, obsY, obsZ
	glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
	glLoadIdentity() # Inicializa sistema de coordenadas do modelo
	glTranslatef(-obsX,-obsY,-obsZ) # Posiciona e orienta o observador
	glRotatef(rotX,1.0,0.0,0.0)
	glRotatef(rotY,0.0,1.0,0.0)


# Funcao usada para especificar o volume de visualizacao
def especificaParametrosVisualizacao():
	global fAspect, angle
	glMatrixMode(GL_PROJECTION) # Especifica sistema de coordenadas de projecao
	glLoadIdentity()	# Inicializa sistema de coordenadas de projecao
	gluPerspective(angle,fAspect,0.5,1500) # Especifica a projecao perspectiva(angulo,aspecto,zMin,zMax)
	posicionaObservador()


# Funcao callback chamada para gerenciar eventos de teclas normais (ESC)
def teclado(tecla, x, y):
	global luz
	if tecla == b'q': # ESC ?
		exit()
	if tecla == b'1':
		luz = 0  #luz vermelha
	elif tecla == b'2':
		luz = 1 #luz verde
	elif tecla == b'3':
		luz = 2 #luz azul
	else:
		luz = 0
	glutPostRedisplay()


# Funcao callback para tratar eventos de teclas especiais
def teclasEspeciais (tecla, x, y):
	global luz, angle
	if tecla == GLUT_KEY_LEFT:
		posLuz[luz][0] -=2
	elif tecla == GLUT_KEY_RIGHT:
		posLuz[luz][0] +=2
	elif tecla == GLUT_KEY_UP:
		posLuz[luz][1] +=2
	elif tecla == GLUT_KEY_DOWN:
		posLuz[luz][1] -=2
	elif tecla == GLUT_KEY_PAGE_UP:
		posLuz[luz][2] -=2
	elif tecla == GLUT_KEY_PAGE_DOWN:
		posLuz[luz][2] +=2
	elif tecla == GLUT_KEY_HOME:
		if angle >= 10:
			angle -= 5
	elif tecla == GLUT_KEY_END:
		if angle <= 150:
			angle +=5
	posicionaObservador()
	glutPostRedisplay()


# Funcao callback para eventos de botoes do mouse
def gerenciaMouse(button, state, x, y):
	global x_ini, y_ini, obsX_ini, obsY_ini, obsZ_ini, rotX_ini, rotY_ini, bot
	if state == GLUT_DOWN:
		x_ini = x  # Salva os parametros atuais
		y_ini = y
		obsX_ini = obsX
		obsY_ini = obsY
		obsZ_ini = obsZ
		rotX_ini = rotX
		rotY_ini = rotY
		bot = button
	else:
		bot = -1


# Funcao callback para eventos de movimento do mouse
def gerenciaMovim(x, y):
	global x_ini, y_ini, rotY, rotX, rotY_ini, rotX_ini, obsZ, obsY, obsX
	global deltax, deltay, deltaz, SENS_OBS, SENS_ROT, SENS_TRANSL
	if bot == GLUT_LEFT_BUTTON:	# Botao esquerdo ?
		deltax = x_ini - x      # Calcula diferencas
		deltay = y_ini - y
		rotY = rotY_ini - deltax/SENS_ROT # E modifica angulos
		rotX = rotX_ini - deltay/SENS_ROT
	# Botao direito ?
	elif bot == GLUT_RIGHT_BUTTON:
		deltaz = y_ini - y   # Calcula diferenca
		obsZ = obsZ_ini + deltaz/SENS_OBS  # E modifica distancia do observador
	# Botao do meio ?
	elif bot==GLUT_MIDDLE_BUTTON:
		# Calcula diferencas
		deltax = x_ini - x
		deltay = y_ini - y
		# E modifica posicoes
		obsX = obsX_ini + deltax/SENS_TRANSL
		obsY = obsY_ini - deltay/SENS_TRANSL
	posicionaObservador()
	glutPostRedisplay()



# Funcao callback chamada quando o tamanho da janela eh alterado
def alteraTamanhoJanela(w, h):
	global fAspect
	if h == 0:
		h = 1	# Para previnir uma divisao por zero
	glViewport(0, 0, w, h)	# Especifica as dimensoes da viewport
	fAspect = float(w/h)	# Calcula a correcao de aspecto
	especificaParametrosVisualizacao()


def inicializa():
	global angle, rotX, rotY, obsX, obsY, obsZ
	glClearColor(0.0, 0.0, 0.0, 1.0) 	# Define a cor de fundo da janela de visualizacao como branca
	glEnable(GL_COLOR_MATERIAL) 	# Habilita a definicao da cor do material a partir da cor corrente
	glEnable(GL_LIGHTING) 	#Habilita o uso de iluminacao
	glEnable(GL_LIGHT0)     # Habilita as fontes de luz
	glEnable(GL_LIGHT1)
	glEnable(GL_LIGHT2)
	glEnable(GL_DEPTH_TEST) # Habilita o depth-buffering
	glShadeModel(GL_SMOOTH) # Habilita o modelo de colorizacao de Gouraud
	angle=70  # Inicializa a variavel que especifica o angulo da projecao perspectiva
	# Inicializa as variaveis usadas para alterar a posicao do
	# observador virtual
	rotX = 30
	rotY = 0
	obsX = 0
	obsY = 0
	obsZ = 100


def main():
	glutInit ()
	glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
	glutInitWindowPosition(5,5)
	glutInitWindowSize(800,800)
	glutCreateWindow("Desenho iluminado por spots")
	glutDisplayFunc(desenha)
	glutReshapeFunc(alteraTamanhoJanela)
	glutKeyboardFunc (teclado)
	glutSpecialFunc (teclasEspeciais)
	glutMouseFunc(gerenciaMouse)
	glutMotionFunc(gerenciaMovim)
	inicializa()
	glutMainLoop()


main()
