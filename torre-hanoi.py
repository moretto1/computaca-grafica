from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import OpenGL.GLUT as glut

win = False
win_message = 'Você venceu!'
window_width = 640
window_height = 480
towers_number = 3
towers_width = 25
towers_height = 75
towers = {}
discs = {}

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


def tower():
    glBegin(GL_LINES)
    glVertex2f(-towers_width, 0)
    glVertex2f(towers_width, 0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0, towers_height)
    glVertex2f(0, 0)
    glEnd()


def tower_scale():
    if towers_number == 5:
        glScalef(0.5, 0.5, 1.0)


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


def draw_disc(disc_number):
    glBegin(GL_POLYGON)
    glVertex2f(discs['disc'+str(disc_number)]['x']*-1, discs['disc'+str(disc_number)]['y'])
    glVertex2f(discs['disc'+str(disc_number)]['x'], discs['disc'+str(disc_number)]['y'])
    glVertex2f(discs['disc'+str(disc_number)]['x'], 0)
    glVertex2f(discs['disc'+str(disc_number)]['x']*-1, 0)
    glEnd()


def disc_positioning(x, y):
    glTranslatef(x, 0, 0)
    glTranslatef(0, y, 0)


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


def help_text():
    text = "Aperte 't' para aumentar o número de torres e 'r' para reiniciar o jogo"
    glColor3f(0, 0, 0)
    glRasterPos2f(-85, -90)
    for i in range(len(text)):
        glut.glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(text[i]))


def won_message():
    glColor3f(0, 0.8, 0)
    glRasterPos2f(-20, 90)
    for i in range(len(win_message)):
        glut.glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(win_message[i]))


def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    draw_all_towers()
    draw_all_discs()

    if win:
        won_message()

    help_text()

    glutSwapBuffers()


def srd_to_sru(x, y):
    x = (2 * x) / (window_width / 100) - 100
    y = (2 * -y) / (window_height / 100) + 100
    return x, y


def is_in_disc_area(disc, x, y):
    return x >= disc['min_limit_x'] and x <= disc['max_limit_x'] and y >= disc['min_limit_y'] and y <= disc['max_limit_y']


def get_tower(tower_number):
    return towers[f't{tower_number}']


def can_make_the_move(actual_tower, next_tower, disc):
    if actual_tower['discs'][0] != disc['number']:
        return False
    if len(next_tower['discs']) != 0 and next_tower['discs'][0] < disc['number']:
        return False
    return True


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


def set_tower_discs(disc, origin_tower, destiny_tower, next_tower_number):
    disc['tower'] = next_tower_number
    origin_tower['discs'].pop(0)
    destiny_tower['discs'].insert(0, disc['number'])
    

def on_mouse_click(button, state, x, y):
    global win
    if state == 1 or win:
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


def set_five_towers_global_values():
    global towers_number, towers_width, towers_height, win
    win = False
    towers_number = 5
    towers_width = 30
    towers_height = 90


def adjust_towers_position(disc, tower_pos, x, min_limit_y, max_limit_y):
    discs_position = tower_pos / 2

    disc['x'] = x
    disc['min_limit_x'] = discs_position - x
    disc['max_limit_x'] = discs_position + x
    disc['min_limit_y'] = min_limit_y
    disc['max_limit_y'] = max_limit_y
    disc['pos_x'] = discs_position
    disc['pos_y'] = min_limit_y


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


def reset_game():
    global win
    win = False
    set_towers_default_values()
    set_discs_default_values()
    

def keyboard_func(key, x, y):
    if key == b't':
        add_towers()
    elif key == b'r':
        reset_game()
    else:
        return
    draw()


def init():
    glClearColor(0.8, 0.8, 0.8, 0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(-100, 100, -100, 100)


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


main()
