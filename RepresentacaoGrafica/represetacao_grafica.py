import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = {
    'cube': (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, 1, 1),
        (-1, -1, 1),
    ),
    'pyramid': (
        (1, -1, -1),
        (1, -1, 1),
        (-1, -1, 1),
        (-1, -1, -1),
        (0, 1, 0),
    ),
    'retangle': (
        (0.5, -1, -1),
        (0.5, 1, -1),
        (-0.5, 1, -1),
        (-0.5, -1, -1),
        (0.5, -1, 1),
        (0.5, 1, 1),
        (-0.5, 1, 1),
        (-0.5, -1, 1),
    ),
}

edges = {
    'cube': (
        (0, 1), (0, 3), (0, 4),
        (1, 2), (1, 5),
        (2, 3), (2, 6),
        (3, 7),
        (4, 5), (4, 7),
        (5, 6),
        (6, 7),
    ),
    'pyramid': (
        (0, 1), (1, 2), (2, 3), (3, 0),
        (0, 4), (1, 4), (2, 4), (3, 4),
    ),
    'retangle': (
        (0, 1), (1, 2), (2, 3), (3, 0),
        (0, 4), (1, 5), (2, 6), (3, 7),
        (4, 5), (5, 6), (6, 7), (7, 4),
    ),
}

current_shape = 'cube'

def draw_shape():
    glBegin(GL_LINES)
    for edge in edges[current_shape]:
        for vertex in edge:
            glVertex3fv(vertices[current_shape][vertex])
            # Aqui, vertices[current_shape][vertex] representa um vetor tridimensional que especifica a posição de um vértice no espaço 3D. 
            # Esses vetores são usados para definir as coordenadas dos vértices dos objetos (cubo, pirâmide, retângulo).
    glEnd()

def change_shape(new_shape):
    global current_shape
    if new_shape in vertices:
        current_shape = new_shape

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("C - Cubo | P - Pirâmide | Y - Retangle")

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)   
    # A função glTranslatef é usada para realizar uma translação no sistema de coordenadas.
    # Neste caso, ela move a cena para trás ao longo do eixo Z, criando a impressão de que o observador está "afastando-se" dos objetos.

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    change_shape('cube')
                elif event.key == pygame.K_p:
                    change_shape('pyramid')
                elif event.key == pygame.K_y:
                    change_shape('retangle')

        glRotatef(1, 3, 1, 1)
        # A função glRotatef é usada para aplicar uma rotação à cena. 
        # Neste caso, ela realiza uma rotação de 1 grau em torno do eixo (3, 1, 1). Isso cria um efeito de rotação contínua dos objetos na cena.
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_shape()
        pygame.display.flip()
        pygame.time.wait(10)

main()
