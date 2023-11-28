<p align="center">
  <img alt="banner" src="https://github.com/A3-2023/.github/blob/main/profile/A3.png?raw=true">
</p>

# Estruturas Matemáticas A3

### Objetivo do Projeto:  

A proposta A3, no âmbito da disciplina de Estruturas Matemáticas, visa aplicar conceitos da ementa de forma prática, destacando a interconexão entre matrizes e sistemas lineares na área de programação. Os alunos serão avaliados com base em critérios processuais, qualidade de apresentação e materiais utilizados.


### Nosso projeto:
O nosso projeto tem como objetivo a criação de dois módulos Python distintos, resultantes do trabalho colaborativo de dois subgrupos de quatro pessoas cada. Cada subgrupo foi encarregado de selecionar e desenvolver os temas das ementas associadas aos seus respectivos módulos.

A divisão em subgrupos proporcionou uma abordagem mais especializada na escolha dos temas, aproveitando as habilidades e interesses individuais de cada equipe. Utilizamos plataformas como WhatsApp, Discord e GitHub para facilitar a comunicação, organização e desenvolvimento eficiente dos projetos.

### Conclusão:
Ao término deste projeto, espera-se apresentar dois módulos Python independentes, desenvolvidos de maneira colaborativa por subgrupos especializados. A utilização eficiente de plataformas de comunicação e colaboração proporcionou um ambiente propício para a consecução dos objetivos, destacando a capacidade da equipe em trabalhar de forma integrada, mesmo em contextos subdivididos.












---
<details>
  
<summary> <h1>🖥 Geometria Euclidiana em Gráficos 3D com OpenGL e Pygame </h1> </summary>

## Resumo do Código:

O código em questão emprega a biblioteca Pygame em conjunto com OpenGL para criar uma interface gráfica e renderizar um cubo tridimensional em constante rotação. Vamos explorar as principais características do código:

### Definição de Vértices e Arestas:

No contexto tridimensional, o código define os vértices do cubo por meio da lista `vertices`, contendo coordenadas tridimensionais. As arestas, representadas na lista `edges`, são pares de índices conectando os vértices.

### Função Cube():

A função `Cube()` desempenha um papel fundamental ao utilizar OpenGL para desenhar as arestas do cubo. Por meio de loops, percorre as arestas e vértices, desenhando linhas que compõem a estrutura tridimensional.

### Função main():

Esta função principal conduz as operações iniciais e principais do programa:
- Inicializa o Pygame e configura a janela OpenGL.
- Define a perspectiva tridimensional usando `gluPerspective`.
- Translada a cena para trás ao aplicar `glTranslatef`.
- Entra em um loop principal, onde a rotação do cubo é aplicada continuamente.
- A função `Cube()` é chamada para renderizar o cubo.
- A janela é atualizada, e o loop continua.

## Conceitos de Álgebra Linear e Transformações Lineares na Renderização 3D:

Para desenhar objetos em um espaço tridimensional utilizando OpenGL, é imperativo empregar conceitos essenciais da geometria euclidiana. Pontos, vetores, matrizes e transformações desempenham papéis cruciais nesse processo. As coordenadas dos objetos são especificadas em um sistema de coordenadas 3D, seguindo as regras da geometria euclidiana. A aplicação prática desses conceitos é evidenciada pelo código, que utiliza coordenadas tridimensionais para representar um cubo giratório no espaço. Essa abordagem destaca a utilização direta de álgebra linear e transformações lineares na criação e manipulação de objetos visuais tridimensionais.



 <h2> 📚 Depedências</h2>
  É necessário rodar o código no Python, com as bibliotecas Pygame e OpenGl.

Instale o Pygame com

```bash
pip install pygame
```
    
Instale o OpenGL com

```bash
pip install PyOpenGL

```
</details>

##  

