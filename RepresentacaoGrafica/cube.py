import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

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
