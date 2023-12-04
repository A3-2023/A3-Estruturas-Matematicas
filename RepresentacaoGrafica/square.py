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
    'cylinder': (
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
    'cylinder': (
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
    glEnd()

def change_shape(new_shape):
    global current_shape
    if new_shape in vertices:
        current_shape = new_shape

def render_text(font, text, position):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=position)
    pygame.display.get_surface().blit(text_surface, text_rect)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("C - Cubo | P - Pirâmide | Y - Cilindro")  # Modificado o título da janela

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    font = pygame.font.Font(None, 36)

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
                    change_shape('cylinder')

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_shape()

        instructions = f"Pressione 'C' para Cubo, 'P' para Pirâmide, 'Y' para Cilindro"
        render_text(font, instructions, (display[0] // 2, display[1] - 20))

        pygame.display.flip()
        pygame.time.wait(10)

main()
