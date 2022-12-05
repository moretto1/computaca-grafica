from math import * 
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *   
posx, posy = 0,0    
sides = 32    
radius = 1    
glBegin(GL_POLYGON)    
for i in range(100):    
    cosine= radius * cos(i*2*pi/sides) + posx    
    sine  = radius * sin(i*2*pi/sides) + posy    
    glVertex2f(cosine,sine)