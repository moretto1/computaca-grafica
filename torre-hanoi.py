from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window_height = 480
window_width = 640
towers_number = 3

towers = {
    't1': {
        'pos': -70,
        'discs_number': 3,
        'discs': [1, 2, 3] 
    },
    't2': {
        'pos': 0,
        'discs_number': 0,
        'discs': [] 
    },
    't3': {
        'pos': 70,
        'discs_number': 0,
        'discs': [] 
    },
}


discs = {
    'disc1': {
        'number': 1,
        'x': 7,
        'y': 10,
        'min_limit_x': -77,
        'max_limit_x': -63,
        'min_limit_y': 20,
        'max_limit_y': 30,
        'pos_x': -70,
        'pos_y': 20,
        'tower': 1
    },
    'disc2': {
        'number': 2,
        'x': 12,
        'y': 10,
        'min_limit_x': -82,
        'max_limit_x': -58,
        'min_limit_y': 10,
        'max_limit_y': 20,
        'pos_x': -70,
        'pos_y': 10,
        'tower': 1
    },
    'disc3': {
        'number': 3,
        'x': 17,
        'y': 10,
        'min_limit_x': -87,
        'max_limit_x': -53,
        'min_limit_y': 0,
        'max_limit_y': 10,
        'pos_x': -70,
        'pos_y': 0,
        'tower': 1
    },
}


def tower():
    glBegin(GL_LINES)
    glVertex2f(-25, 0)
    glVertex2f(25, 0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0, 75)
    glVertex2f(0, 0)
    glEnd()


def draw_disc_1():
    glBegin(GL_POLYGON)
    glVertex2f(discs['disc1']['x']*-1, discs['disc1']['y'])
    glVertex2f(discs['disc1']['x'], discs['disc1']['y'])
    glVertex2f(discs['disc1']['x'], 0)
    glVertex2f(discs['disc1']['x']*-1, 0)
    glEnd()


def draw_disc_2():
    glBegin(GL_POLYGON)
    glVertex2f(discs['disc2']['x']*-1, discs['disc2']['y'])
    glVertex2f(discs['disc2']['x'], discs['disc2']['y'])
    glVertex2f(discs['disc2']['x'], 0)
    glVertex2f(discs['disc2']['x']*-1, 0)
    glEnd()


def draw_disc_3():
    glBegin(GL_POLYGON)
    glVertex2f(discs['disc3']['x']*-1, discs['disc3']['y'])
    glVertex2f(discs['disc3']['x'], discs['disc3']['y'])
    glVertex2f(discs['disc3']['x'], 0)
    glVertex2f(discs['disc3']['x']*-1, 0)
    glEnd()


def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(6)
    glPushMatrix()
    glTranslatef(towers['t1']['pos'], 0, 0)
    tower()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(towers['t2']['pos'], 0, 0)
    tower()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(towers['t3']['pos'], 0, 0)
    tower()
    glPopMatrix()

    glColor3f(1.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(discs['disc1']['pos_x'], 0, 0)
    glTranslatef(0, discs['disc1']['pos_y'], 0)
    draw_disc_1()
    glPopMatrix()


    glColor3f(0.0, 1.0, 0.0)
    glPushMatrix()
    glTranslatef(discs['disc2']['pos_x'], 0, 0)
    glTranslatef(0, discs['disc2']['pos_y'], 0)
    draw_disc_2()
    glPopMatrix()

    glColor3f(0.0, 0.0, 1.0)
    glPushMatrix()
    glTranslatef(discs['disc3']['pos_x'], 0, 0)
    glTranslatef(0, discs['disc3']['pos_y'], 0)
    draw_disc_3()
    glPopMatrix()

    glutSwapBuffers()


def on_mouse_click(button, state, x, y):
    if state == 1:
        return
    x = (2 * x) / (window_width / 100) - 100
    y = (2 * -y) / (window_height / 100) + 100
    for disc_name, disc in discs.items():
        if x >= disc['min_limit_x'] and x <= disc['max_limit_x']:
            if y >= disc['min_limit_y'] and y <= disc['max_limit_y']:
                actual_tower_number = disc['tower']
                actual_tower_key = f't{actual_tower_number}'
                actual_tower = towers[actual_tower_key]
                
                next_tower_number = actual_tower_number + 1
                if next_tower_number > towers_number:
                    next_tower_number = 1
                next_tower_key = f't{next_tower_number}'
                next_tower = towers[next_tower_key]

                next_tower_discs_number = len(next_tower['discs'])
                if actual_tower['discs'][0] != disc['number']:
                    return
                if next_tower_discs_number != 0 and next_tower['discs'][0] < disc['number']:
                    return

                disc['tower'] = next_tower_number
                actual_tower['discs'].pop(0)
                next_tower['discs'].insert(0, disc['number'])

                disc_pos_x = next_tower['pos']
                disc_pos_y = next_tower_discs_number * 10
                disc['pos_x'] = disc_pos_x
                disc['pos_y'] = disc_pos_y
                disc['min_limit_x'] = disc_pos_x - disc['x']
                disc['max_limit_x'] = disc_pos_x + disc['x']
                disc['min_limit_y'] = disc_pos_y
                disc['max_limit_y'] = disc_pos_y + 10

                glutPostRedisplay()


def init():
    glClearColor(0.8, 0.8, 0.8, 0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(-100, 100, -100, 100)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow('Torre de Hanoi')
    glutMouseFunc(on_mouse_click)
    glutDisplayFunc(draw)
    init()
    glutMainLoop()


main()
