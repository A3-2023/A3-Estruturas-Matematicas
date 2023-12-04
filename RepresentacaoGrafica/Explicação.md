 <h1> Cubo Giratório </h1>

## 🌺 Conceitos de Álgebra Linear e Transformações Lineares na Renderização 3D:

Para desenhar objetos em um espaço tridimensional utilizando OpenGL, é imperativo empregar conceitos essenciais da geometria euclidiana. Pontos, vetores, matrizes e transformações desempenham papéis cruciais nesse processo. As coordenadas dos objetos são especificadas em um sistema de coordenadas 3D, seguindo as regras da geometria euclidiana. A aplicação prática desses conceitos é evidenciada pelo código, que utiliza coordenadas tridimensionais para representar um cubo giratório no espaço. Essa abordagem destaca a utilização direta de álgebra linear e transformações lineares na criação e manipulação de objetos visuais tridimensionais.



## 📚 Depedências
  É necessário rodar o código no Python, com as bibliotecas Pygame e OpenGl.

Instale o Pygame com

```bash
pip install pygame
```
    
Instale o OpenGL com

```bash
pip install PyOpenGL

```


----

# ⌨ Resumo do Código:

## Importação de Bibliotecas 

O código importa as bibliotecas necessárias, `pygame` é usada para criar janelas e lidar com eventos, enquanto `OpenGL.GL` e `OpenGL.GLU` são usadas para a renderização gráfica em 3D.
<details>
<summary> <h4> Expandir </h4> </summary>
 
  ``` python 
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

```
</details>


## Definição de Vértices e Arestas

Aqui, são definidos os vértices e as arestas que compõem um cubo, uma pirâmede e um retângulo. Os vértices são coordenadas tridimensionais, e as arestas são pares de índices referentes aos vértices.

<details>
<summary>  <h4> Expandir </h4> </summary>

 
``` python
vertices = {
    'cube': (
        # Coordenadas dos vértices para o cubo
    ),
    'pyramid': (
        # Coordenadas dos vértices para a pirâmide
    ),
    'cylinder': (
        # Coordenadas dos vértices para o cilindro
    ),
}

edges = {
    'cube': (
        # Definição das arestas para o cubo
    ),
    'pyramid': (
        # Definição das arestas para a pirâmide
    ),
    'cylinder': (
        # Definição das arestas para o cilindro
    ),
}

```

</details>



## Funções para Desenhar e Mudar de Forma:

A função draw_shape desenha a forma atual especificada por current_shape usando as coordenadas de vértices e definições de arestas.

A função change_shape muda a forma atual para a forma desejada (new_shape), desde que esta forma esteja definida nos vértices.


<details>
<summary> <h4> Expandir </h4> </summary>
 
``` python
def draw_shape():
    # Função para desenhar a forma atual
    glBegin(GL_LINES)
    for edge in edges[current_shape]:
        for vertex in edge:
            glVertex3fv(vertices[current_shape][vertex])
    glEnd()

def change_shape(new_shape):
    # Função para mudar a forma atual
    global current_shape
    if new_shape in vertices:
        current_shape = new_shape
```
</details>



## Função main
A função `main()` inicializa o Pygame, configura a janela OpenGL, define a perspectiva usando `gluPerspective`, e translada a cena para trás usando `glTranslatef`.

<details>
<summary> <h4> Expandir </h4> </summary>
 
``` python
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
```
</details>





## Loop Principal: 

- O loop principal aguarda eventos do Pygame. Se o evento de fechamento da janela ocorrer, o programa é encerrado.
- A cena é rotacionada em torno do eixo `(3, 1, 1)` usando `glRotatef`.
- O buffer de cores e o buffer de profundidade são limpos, e a função `Cube()` é chamada para desenhar o cubo.
- A tela é atualizada e aguarda-se 10 milissegundos antes da próxima iteração.

<details>
<summary> <h4> Expandir </h4> </summary>
 
```
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)
```

</details>




No geral, o código cria uma aplicação simples que exibe um cubo 3D rotacionando em uma janela gráfica. A rotação é realizada continuamente dentro de um loop principal.

---

