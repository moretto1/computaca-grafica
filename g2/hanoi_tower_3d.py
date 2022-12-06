from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import OpenGL.GLUT as glut


TAM = 60
D = 2 

angle = 0
fAspect = 0
rotX = 0
rotY = 0
rotX_ini = 0
rotY_ini = 0
obsX = 0
obsY = 0
obsZ = 0
obsX_ini = 0
obsY_ini = 0
obsZ_ini = 0
x_ini = 0
y_ini = 0
bot = 0

luz = 0 # Luz selecionada
posLuz = [[-30, 50, 0, 1], [0, 50, 0, 1], [30, 50, 0, 1]] # Posicao de cada luz
dirLuz = [[0, -1, 0], [0, -1, 0], [0, -1, 0]]    # Direcao de cada luz
luzDifusa = [[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]]  # Cor difusa de cada luz #RGB
luzEspecular= [[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]]     # Cor especular de cada luz #RGB

SENS_ROT = 5.0
SENS_OBS = 10.0
SENS_TRANSL = 10.0

towers = {}
discs = {}

difference_disc_height = 3

tower_first_disc_height = 2
tower_next_disc_height = 3

win = False
win_message_str = 'Você venceu!'


#seta valores default para as variaveis globais envolvendo torres
def set_towers_default_values():
    global towers
    towers = {
        't1': {
            'pos': -30,
            'discs': [1, 2, 3]
        },
        't2': {
            'pos': 0,
            'discs': []
        },
        't3': {
            'pos': 30,
            'discs': []
        },
    }


#seta valores default para as variaveis globais envolvendo os discos
def set_discs_default_values():
    global discs
    discs = {
        'disc1': {
            'number': 1,
            'tower': 1
        },
        'disc2': {
            'number': 2,
            'tower': 1
        },
        'disc3': {
            'number': 3,
            'tower': 1
        },
    }


# Funcao responsavel pela especificacao dos parametros de iluminacao
def sets_lighting():
	global posLuz, dirLuz, luzDifusa, luzEspecular
	luzAmbiente= [0.1, 0.1, 0.1, 1.0]
	especularidade = [0.7, 0.7, 0.7, 1.0] # Capacidade de brilho do material
	especMaterial = 90
	glMaterialfv(GL_FRONT, GL_SPECULAR, especularidade) # Define a refletancia do material
	glMateriali(GL_FRONT, GL_SHININESS, especMaterial) # Define a concentracao do brilho
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente) # Ativa o uso da lutowers['t' + strz ambiente
	cont = 0
	while cont < 3: # Define os parametros das fontes de luz
		glLightfv(GL_LIGHT0 + cont, GL_AMBIENT, luzAmbiente)
		glLightfv(GL_LIGHT0 + cont, GL_DIFFUSE, luzDifusa[cont] )
		glLightfv(GL_LIGHT0 + cont, GL_SPECULAR, luzEspecular[cont] )
		glLightfv(GL_LIGHT0 + cont, GL_POSITION, posLuz[cont] )
		glLightfv(GL_LIGHT0 + cont, GL_SPOT_DIRECTION,dirLuz[cont])
		glLightf(GL_LIGHT0  + cont, GL_SPOT_CUTOFF,40.0)
		glLightf(GL_LIGHT0  + cont, GL_SPOT_EXPONENT,10.0)
		cont = cont + 1


# Funcao para desenhar um "chao" no ambiente
def floor():
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


def tower():
	glBegin(GL_QUADS)

	glVertex3f(-2.5, 40, -2.5)
	glVertex3f(2.5, 40, -2.5)
	glVertex3f(2.5, 0, -2.5)
	glVertex3f(-2.5, 0, -2.5)

	glVertex3f(-2.5, 40, 2.5)
	glVertex3f(2.5, 40, 2.5)
	glVertex3f(2.5, 0, 2.5)
	glVertex3f(-2.5, 0, 2.5)

	glVertex3f(-2.5, 40, -2.5)
	glVertex3f(-2.5, 40, 2.5)
	glVertex3f(-2.5, 0, 2.5)
	glVertex3f(-2.5, 0, -2.5)

	glVertex3f(2.5, 40, -2.5)
	glVertex3f(2.5, 40, 2.5)
	glVertex3f(2.5, 0, 2.5)
	glVertex3f(2.5, 0, -2.5)

	glVertex3f(-2.5, 40, -2.5)
	glVertex3f(2.5, 40, -2.5)
	glVertex3f(2.5, 40, 2.5)
	glVertex3f(-2.5, 40, 2.5)

	glEnd()


def draw_all_towers():
	glColor3f(0.6, 0.6, 0.1)

	glPushMatrix()
	glTranslatef(-30, 0, 0)
	tower()
	glPopMatrix()

	tower()

	glPushMatrix()
	glTranslatef(30, 0, 0)
	tower()
	glPopMatrix()


def draw_all_discs():
	disc3_tower_height = tower_first_disc_height

	disc2_tower_height = 2
	if len(towers['t' + str(discs['disc2']['tower'])]['discs']) == 2:
		if (1 in towers['t' + str(discs['disc2']['tower'])]['discs']):
			disc2_tower_height = tower_first_disc_height
		else:
			disc2_tower_height = 5
	elif len(towers['t' + str(discs['disc2']['tower'])]['discs']) == 3:
		disc2_tower_height = 5
	elif len(towers['t' + str(discs['disc2']['tower'])]['discs']) == 1:
		disc2_tower_height = 2

	disc1_tower_height = 2
	if len(towers['t' + str(discs['disc1']['tower'])]['discs']) == 2:
		disc1_tower_height = 5
	if len(towers['t' + str(discs['disc1']['tower'])]['discs']) == 3:
		disc1_tower_height = 8

	glColor3f(1.0, 0.0, 0.0)
	glPushMatrix()
	glTranslatef(towers['t' + str(discs['disc1']['tower'])]['pos'], 0, 0)
	glTranslatef(0, disc1_tower_height, 0)
	glRotatef(-90,1,0,0)
	glutSolidTorus(2, 6, 7, 7)
	glPopMatrix()

	glColor3f(0.0, 1.0, 0.0)
	glPushMatrix()
	glTranslatef(towers['t'+ str(discs['disc2']['tower'])]['pos'], 0, 0)
	glTranslatef(0, disc2_tower_height, 0)
	glRotatef(-90,1,0,0)
	glutSolidTorus(2, 8, 12, 12)
	glPopMatrix()

	glColor3f(0.0, 0.0, 1.0)
	glPushMatrix()
	glTranslatef(towers['t' + str(discs['disc3']['tower'])]['pos'], 0, 0)
	glTranslatef(0, disc3_tower_height, 0)
	glRotatef(-90,1,0,0)

	glutSolidTorus(2, 10, 16, 16)
	glPopMatrix()


def draw():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	sets_lighting()
	glDisable(GL_LIGHTING)
	glEnable(GL_LIGHTING)

	draw_all_towers()
	draw_all_discs()

	if win:
		win_message()

	help_text()
	floor()
	glutSwapBuffers()


def win_message():
    global win_message_rotation
    glColor3f(0, 0.8, 0)
    glPushMatrix()
    glRasterPos2f(-10, 50)
    for i in range(len(win_message_str)):
        glut.glutBitmapCharacter(glut.GLUT_BITMAP_HELVETICA_18, ord(win_message_str[i]))
    glPopMatrix()


def observer():
	global rotX, rotY, obsX, obsY, obsZ
	glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
	glLoadIdentity() # Inicializa sistema de coordenadas do modelo
	glTranslatef(-obsX,-obsY,-obsZ) # Posiciona e orienta o observador
	glRotatef(rotX,1.0,0.0,0.0)
	glRotatef(rotY,0.0,1.0,0.0)


# Funcao usada para especificar o volume de visualizacao
def visualization_params():
	global fAspect, angle
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()	# Inicializa sistema de coordenadas de projecao
	gluPerspective(angle,fAspect,0.5,1500) # Especifica a projecao perspectiva(angulo,aspecto,zMin,zMax)
	observer()


def game(disc_number):
	global win

	if win:
		return

	actual_tower = discs['disc'+str(disc_number)]['tower']
	next_tower = actual_tower + 1
	if next_tower > 3:
		next_tower = 1

	if not can_make_the_move(actual_tower, next_tower, disc_number):
		return

	towers['t' + str(actual_tower)]['discs'].pop(0)
	towers['t' + str(next_tower)]['discs'].insert(0, disc_number)

	discs['disc'+str(disc_number)]['tower'] = next_tower

	if len(towers['t3']['discs']) == 3:
		win = True


def can_make_the_move(actual_tower, next_tower, disc):
    if towers['t' + str(actual_tower)]['discs'][0] != discs['disc' + str(disc)]['number']:
        return False
    if len(towers['t' + str(next_tower)]['discs']) != 0 and towers['t' + str(next_tower)]['discs'][0] < discs['disc' + str(disc)]['number']:
        return False
    return True


def reset_game():
    global win
    win = False
    set_towers_default_values()
    set_discs_default_values()
	

def keyboard(tecla, x, y):
	if tecla == b'1':
		game(1)
	elif tecla == b'2':
		game(2)
	elif tecla == b'3':
		game(3)
	elif tecla == b'r':
		reset_game()

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
	elif tecla == b'1':
		pass
	observer()
	glutPostRedisplay()


def help_text():
	text = "Aperte 'r' para reiniciar o jogo"
	glColor3f(1, 1, 1)
	glRasterPos2f(0, 50)
	for i in range(len(text)):
		glut.glutBitmapCharacter(glut.GLUT_BITMAP_HELVETICA_18, ord(text[i]))


# Funcao callback para eventos de botoes do mouse
def mouse(button, state, x, y):
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


def movement(x, y):
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
	observer()
	glutPostRedisplay()


# Funcao callback chamada quando o tamanho da janela eh alterado
def change_window_size(w, h):
	global fAspect
	if h == 0:
		h = 1	# Para previnir uma divisao por zero
	glViewport(0, 0, w, h)	# Especifica as dimensoes da viewport
	fAspect = float(w/h)	# Calcula a correcao de aspecto
	visualization_params()


def init():
	global angle, rotX, rotY, obsX, obsY, obsZ
	glClearColor(0.0, 0.0, 0.0, 1.0)
	glEnable(GL_COLOR_MATERIAL)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_LIGHT1)
	glEnable(GL_LIGHT2)
	glEnable(GL_DEPTH_TEST)
	glShadeModel(GL_SMOOTH)
	angle=70
	rotY = 0
	obsX = 0
	obsY = 0
	obsZ = 100


def main():
	set_towers_default_values()
	set_discs_default_values()

	glutInit()
	glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
	glutInitWindowPosition(5,5)
	glutInitWindowSize(800,800)
	glutCreateWindow("Tower of Hanoi - 3D")
	glutDisplayFunc(draw)
	glutReshapeFunc(change_window_size)
	glutKeyboardFunc(keyboard)
	glutSpecialFunc (teclasEspeciais)
	glutMouseFunc(mouse)
	glutMotionFunc(movement)
	init()
	glutMainLoop()


main()
