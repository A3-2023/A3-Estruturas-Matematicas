# ⚪ Explorando Gráficos 3D com Pygame e OpenGL
<details>
 <summary> <h2>  📜 Documentação do código representacao_grafica.py</h2> </summary>

## 🌺 Aplicação da Álgebra Linear no Código:

A álgebra linear é frequentemente utilizada em gráficos 3D para realizar transformações em objetos, como rotações, translações e escalas. No código em questão, a função glTranslatef é usada para realizar uma translação ao longo do eixo Z, movendo o objeto para mais perto ou mais longe do observador. Além disso, a função glRotatef é usada para aplicar uma rotação contínua ao objeto.

A representação das formas tridimensionais (cubo, pirâmide, retângulo) é feita através de vértices (pontos no espaço tridimensional) e arestas (conexões entre esses pontos). Essa representação é uma aplicação direta de conceitos geométricos e, portanto, também pode ser associada a conceitos de álgebra linear, especialmente quando se lida com transformações e projeções.

No contexto gráfico 3D, a álgebra linear é fundamental para entender e manipular as matrizes de transformação que são aplicadas aos vértices dos objetos para movê-los e rotacioná-los no espaço tridimensional. Embora o código em questão não aborde diretamente a manipulação manual de matrizes, a utilização das funções de OpenGL incorpora esses conceitos por trás dos panos, facilitando a exibição de objetos 3D na tela.



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
O código em questão é uma aplicação simples que utiliza Pygame e OpenGL para renderizar diferentes formas tridimensionais (cubo, pirâmide, retângulo) em uma janela. O usuário pode alternar entre essas formas pressionando as teclas 'C', 'P' e 'Y'. A rotação contínua da forma renderizada é controlada por um pequeno loop na função principal.

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
<summary> <h2> </h2></summary>

<details>
 
</details>

No geral, o código cria uma aplicação simples que exibe um cubo 3D rotacionando em uma janela gráfica. A rotação é realizada continuamente dentro de um loop principal.

---
</details>










# 🔵Explorando Gráficos 3D com Matplotlib

<details> 
 <summary> <h2> 📜 Documentação do código cube.py</h2></summary>
 
## 📚 Depedências:
 
É necessário rodar o código no Python, com as bibliotecas Numpy e Matplotlib.

Instale o Numpy com

```bash
pip install numpy
```
    
Instale o Matplotlib com

```bash
pip install matplotlib

```


----

# ⌨ Resumo do Código:

O código utiliza a biblioteca matplotlib para criar uma visualização gráfica tridimensional de um cubo. A função draw_cube é definida para desenhar as faces do cubo, e a função principal main configura a figura, adiciona o cubo ao eixo 3D e ajusta os limites dos eixos. Ao ser executado, o código exibe uma representação visual do cubo 3D em uma janela usando a matplotlib.


## Importação de Bibliotecas 

O código utiliza as bibliotecas numpy e matplotlib para visualização 3D. A biblioteca numpy é empregada para manipulação de arrays, enquanto a matplotlib é utilizada para criar gráficos.
<details>
<summary> <h4> Expandir </h4> </summary>
 
  ``` python 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


```
</details>



## Função para Desenhar um Cubo 3D:

O código define uma função draw_cube que desenha um cubo tridimensional no espaço. Os vértices e as faces do cubo são especificados, e a função utiliza a Poly3DCollection para criar a representação visual.



<details>
<summary> <h4> Expandir </h4> </summary>
 
``` python
def draw_cube(ax):
    # Define os vértices do cubo
    vertices = np.array([[0, 0, 0],
                         [1, 0, 0],
                         [1, 1, 0],
                         [0, 1, 0],
                         [0, 0, 1],
                         [1, 0, 1],
                         [1, 1, 1],
                         [0, 1, 1]])

    # Define as faces do cubo
    faces = [[vertices[j] for j in [0, 1, 5, 4]],
             [vertices[j] for j in [1, 2, 6, 5]],
             [vertices[j] for j in [2, 3, 7, 6]],
             [vertices[j] for j in [3, 0, 4, 7]],
             [vertices[j] for j in [0, 1, 2, 3]],
             [vertices[j] for j in [4, 5, 6, 7]]]

    # Desenha o cubo
    ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

```
</details>



## Função principal
A função main cria uma figura e um eixo tridimensional usando a matplotlib. Em seguida, chama a função draw_cube para desenhar um cubo 3D. Os limites dos eixos são ajustados e a figura é exibida.

<details>
<summary> <h4> Expandir </h4> </summary>
 
``` python
def main():
    # Cria a figura e o eixo 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Chama as funções para desenhar as formas
    draw_cube(ax)

    # Ajusta o limite dos eixos
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])

    # Exibe a figura
    plt.show()

if __name__ == "__main__":
    main()

```
</details>

Este código utiliza a matplotlib para criar uma representação visual de um cubo tridimensional, fornecendo uma alternativa interessante para exploração gráfica em 3D.


