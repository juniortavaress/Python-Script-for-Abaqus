import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Definindo as dimensões da barra
length = 200000  # Comprimento em mm
width = 10   # Largura em mm
height = 10  # Altura em mm

# Definindo os vértices do paralelepípedo (barra)
vertices = [[0, 0, 0],
            [length, 0, 0],
            [length, width, 0],
            [0, width, 0],
            [0, 0, height],
            [length, 0, height],
            [length, width, height],
            [0, width, height]]

# Definindo as faces do paralelepípedo usando os vértices
faces = [[vertices[0], vertices[1], vertices[5], vertices[4]],  # Face inferior
         [vertices[7], vertices[6], vertices[2], vertices[3]],  # Face superior
         [vertices[0], vertices[3], vertices[7], vertices[4]],  # Face esquerda
         [vertices[1], vertices[2], vertices[6], vertices[5]],  # Face direita
         [vertices[0], vertices[1], vertices[2], vertices[3]],  # Face frontal
         [vertices[4], vertices[5], vertices[6], vertices[7]]]  # Face traseira

# Criando a figura e o eixo 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Criando o Poly3DCollection a partir das faces
ax.add_collection3d(Poly3DCollection(faces, facecolors='black', linewidths=1, edgecolors='grey', alpha=0.8))

# Definindo os limites dos eixos para 200 mm
ax.set_xlim([-50, length +50])
ax.set_ylim([-30, 30])
ax.set_zlim([-30, 30])

# Etiquetas dos eixos
ax.set_xlabel('Comprimento (mm)')
ax.set_ylabel('Largura (mm)')
ax.set_zlabel('Altura (mm)')

ax.set_axis_off()
# Exibindo o gráfico
plt.show()
