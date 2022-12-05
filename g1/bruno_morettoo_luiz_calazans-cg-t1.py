from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import OpenGL.GLUT as glut

#variaveis globais necessarias para o funcionamento do programa
win = False
win_message_str = 'Você venceu!'
win_message_rotation = 0.0
window_width = 640
window_height = 480
towers_number = 3
towers_width = 25
towers_height = 75
towers = {}
discs = {}


#seta valores default para as variaveis globais envolvendo torres
def set_towers_default_values():
    global towers, towers_number, towers_width, towers_height
    towers_number = 3
    towers_width = 25
    towers_height = 75
    towers = {
        't1': {
            'pos': -70,
            'discs': [1, 2, 3] 
        },
        't2': {
            'pos': 0,
            'discs': [] 
        },
        't3': {
            'pos': 70,
            'discs': [] 
        },
    }


#seta valores default para as variaveis globais envolvendo os discos
def set_discs_default_values():
    global discs
    discs = {
        'disc1': {
            'number': 1,
            'x': 4,
            'y': 8,
            'min_limit_x': -74,
            'max_limit_x': -66,
            'min_limit_y': 20,
            'max_limit_y': 30,
            'pos_x': -70,
            'pos_y': 16,
            'tower': 1
        },
        'disc2': {
            'number': 2,
            'x': 7,
            'y': 8,
            'min_limit_x': -77,
            'max_limit_x': -63,
            'min_limit_y': 10,
            'max_limit_y': 20,
            'pos_x': -70,
            'pos_y': 8,
            'tower': 1
        },
        'disc3': {
            'number': 3,
            'x': 10,
            'y': 8,
            'min_limit_x': -80,
            'max_limit_x': -60,
            'min_limit_y': 0,
            'max_limit_y': 10,
            'pos_x': -70,
            'pos_y': 0,
            'tower': 1
        },
    }


#cria uma torre
def tower():
    glBegin(GL_LINES)
    glVertex2f(-towers_width, 0)
    glVertex2f(towers_width, 0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0, towers_height)
    glVertex2f(0, 0)
    glEnd()


#faz a função de escala da torre
def tower_scale():
    if towers_number == 5:
        glScalef(0.5, 0.5, 1.0)


#desenha todas as torres
def draw_all_towers():
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(6)

    glPushMatrix()
    tower_scale()
    glTranslatef(towers['t1']['pos'], 0, 0)
    tower()
    glPopMatrix()

    glPushMatrix()
    tower_scale()
    glTranslatef(towers['t2']['pos'], 0, 0)
    tower()
    glPopMatrix()

    glPushMatrix()
    tower_scale()
    glTranslatef(towers['t3']['pos'], 0, 0)
    tower()
    glPopMatrix()

    if towers_number == 5:
        glPushMatrix()
        tower_scale()
        glTranslatef(towers['t4']['pos'], 0, 0)
        tower()
        glPopMatrix()

        glPushMatrix()
        tower_scale()
        glTranslatef(towers['t5']['pos'], 0, 0)
        tower()
        glPopMatrix()


#desenha um disco
def draw_disc(disc_number):
    glBegin(GL_POLYGON)
    glVertex2f(discs['disc'+str(disc_number)]['x']*-1, discs['disc'+str(disc_number)]['y'])
    glVertex2f(discs['disc'+str(disc_number)]['x'], discs['disc'+str(disc_number)]['y'])
    glVertex2f(discs['disc'+str(disc_number)]['x'], 0)
    glVertex2f(discs['disc'+str(disc_number)]['x']*-1, 0)
    glEnd()


#posiciona o disco
def disc_positioning(x, y):
    glTranslatef(x, 0, 0)
    glTranslatef(0, y, 0)


#desenha todos os discos
def draw_all_discs():
    glColor3f(1.0, 0.0, 0.0)
    glPushMatrix()
    disc_positioning(discs['disc1']['pos_x'], discs['disc1']['pos_y'])
    draw_disc(1)
    glPopMatrix()


    glColor3f(0.0, 1.0, 0.0)
    glPushMatrix()
    disc_positioning(discs['disc2']['pos_x'], discs['disc2']['pos_y'])
    draw_disc(2)
    glPopMatrix()

    glColor3f(0.0, 0.0, 1.0)
    glPushMatrix()
    disc_positioning(discs['disc3']['pos_x'], discs['disc3']['pos_y'])
    draw_disc(3)
    glPopMatrix()

    if towers_number == 5:
        glColor3f(0.5, 0.5, 1.0)
        glPushMatrix()
        disc_positioning(discs['disc4']['pos_x'], discs['disc4']['pos_y'])
        draw_disc(4)
        glPopMatrix()

        glColor3f(0.5, 0.5, 0.5)
        glPushMatrix()
        disc_positioning(discs['disc5']['pos_x'], discs['disc5']['pos_y'])
        draw_disc(5)
        glPopMatrix()


#desenha o texto de ajuda
def help_text():
    text = "Aperte 't' para aumentar o número de torres e 'r' para reiniciar o jogo"
    glColor3f(0, 0, 0)
    glRasterPos2f(-85, -90)
    for i in range(len(text)):
        glut.glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(text[i]))


#desenha o texto de vitória
def win_message():
    global win_message_rotation
    glColor3f(0, 0.8, 0)
    glPushMatrix()
    glRotatef (win_message_rotation, 0.0, 0.0, 1.0)
    glRasterPos2f(-20, -20)
    for i in range(len(win_message_str)):
        glut.glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(win_message_str[i]))
    glPopMatrix()


#desenha a base do jogo
def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    draw_all_towers()
    draw_all_discs()

    if win:
        win_message()

    help_text()

    glutSwapBuffers()


#realiza a conversão do SRD para o SRU
def srd_to_sru(x, y):
    x = (2 * x) / (window_width / 100) - 100
    y = (2 * -y) / (window_height / 100) + 100
    return x, y


#valida se o clique esta na area do disco
def is_in_disc_area(disc, x, y):
    return x >= disc['min_limit_x'] and x <= disc['max_limit_x'] and y >= disc['min_limit_y'] and y <= disc['max_limit_y']


#pega uma torre
def get_tower(tower_number):
    return towers[f't{tower_number}']


#valida se o movimento é valido
def can_make_the_move(actual_tower, next_tower, disc):
    if actual_tower['discs'][0] != disc['number']:
        return False
    if len(next_tower['discs']) != 0 and next_tower['discs'][0] < disc['number']:
        return False
    return True


#seta os valores pra nova posicao do disco após o clique
def set_disc_position(disc, tower):
    if towers_number == 5:
        disc_pos_x = tower['pos'] / 2
    else:
        disc_pos_x = tower['pos']
    disc_pos_y = len(tower['discs']) * 8
    disc['pos_x'] = disc_pos_x
    disc['pos_y'] = disc_pos_y
    disc['min_limit_x'] = disc_pos_x - disc['x']
    disc['max_limit_x'] = disc_pos_x + disc['x']
    disc['min_limit_y'] = disc_pos_y
    disc['max_limit_y'] = disc_pos_y + 8


#seta os valores necessarios do disco após o clique
def set_tower_discs(disc, origin_tower, destiny_tower, next_tower_number):
    disc['tower'] = next_tower_number
    origin_tower['discs'].pop(0)
    destiny_tower['discs'].insert(0, disc['number'])
    

#função do mouse
def on_mouse_click(button, state, x, y):
    global win, win_message_rotation

    if state == 1:
        return

    if win:
        win_message_rotation += 20.0
        glutPostRedisplay()
        return

    x, y = srd_to_sru(x, y)

    for disc in discs.values():
        if is_in_disc_area(disc, x, y):
            actual_tower = get_tower(disc['tower'])
            
            next_tower_number = disc['tower'] + 1
            if next_tower_number > towers_number:
                next_tower_number = 1
            next_tower = get_tower(next_tower_number)

            if not can_make_the_move(actual_tower, next_tower, disc):
                return
            
            set_disc_position(disc, next_tower)
            set_tower_discs(disc, actual_tower, next_tower, next_tower_number)

            if towers_number == 3:
                if len(towers['t3']['discs']) == 3:
                    win = True
            else:
                if len(towers['t3']['discs']) == 5:
                    win = True

            glutPostRedisplay()


#atualiza as variaveis globais para jogar com 5 torres
def set_five_towers_global_values():
    global towers_number, towers_width, towers_height, win
    win = False
    towers_number = 5
    towers_width = 30
    towers_height = 90


#ajusta as posições das torres para 5 torres
def adjust_towers_position(disc, tower_pos, x, min_limit_y, max_limit_y):
    discs_position = tower_pos / 2

    disc['x'] = x
    disc['min_limit_x'] = discs_position - x
    disc['max_limit_x'] = discs_position + x
    disc['min_limit_y'] = min_limit_y
    disc['max_limit_y'] = max_limit_y
    disc['pos_x'] = discs_position
    disc['pos_y'] = min_limit_y


#adiciona os novos discos quando é alterado pra 5 torres
def add_new_discs(tower_pos):
    discs_position = tower_pos / 2

    discs['disc4'] = {
        'number': 4,
        'x': 10,
        'y': 8,
        'min_limit_x': -83,
        'max_limit_x': -57,
        'min_limit_y': 8,
        'max_limit_y': 16,
        'pos_x': discs_position,
        'pos_y': 8,
        'tower': 1
    }
    discs['disc5'] = {
        'number': 5,
        'x': 12,
        'y': 8,
        'min_limit_x': -87,
        'max_limit_x': -53,
        'min_limit_y': 0,
        'max_limit_y': 8,
        'pos_x': discs_position,
        'pos_y': 0,
        'tower': 1
    }


#adiciona as novas torres e discos
def add_towers():
    set_towers_default_values()
    set_discs_default_values()
    set_five_towers_global_values()

    towers['t1']['discs'] = [1, 2, 3, 4, 5]

    towers['t1']['pos'] = -150
    towers['t2']['pos'] = -75
    towers['t3']['pos'] = 0

    towers['t4'] = {
        'pos': 75,
        'discs': [] 
    }
    towers['t5'] = {
        'pos': 150,
        'discs': [] 
    }

    adjust_towers_position(discs['disc1'], towers['t1']['pos'], 4, 32, 40)
    adjust_towers_position(discs['disc2'], towers['t1']['pos'], 6, 24, 32)
    adjust_towers_position(discs['disc3'], towers['t1']['pos'], 8, 16, 24)

    add_new_discs(towers['t1']['pos'])


#reinicia o jogo
def reset_game():
    global win
    win = False
    set_towers_default_values()
    set_discs_default_values()
    

#função do teclado
def keyboard_func(key, x, y):
    if key == b't':
        add_towers()
    elif key == b'r':
        reset_game()
    else:
        return
    draw()


#inicialização
def init():
    glClearColor(0.8, 0.8, 0.8, 0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(-100, 100, -100, 100)


#funcao main
def main():
    set_towers_default_values()
    set_discs_default_values()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow('Torre de Hanoi')
    glutMouseFunc(on_mouse_click)
    glutKeyboardFunc(keyboard_func)
    glutDisplayFunc(draw)
    init()
    glutMainLoop()


#chamada da função main
main()
