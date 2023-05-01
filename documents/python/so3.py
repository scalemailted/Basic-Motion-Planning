from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from quaternion import from_float_array, rotate_vectors

def plot_vertices(ax, quivers, delta=0.6):
    xaxis, yaxis, zaxis = 0, 1, 2
    iLine, iEnd, iStart = 0, 0, 1
    # Apex Point of pyramid is origin point x,y,z axis
    apex = np.array([0, 0, 0])
    # Three Base Points of pyramid (XY, XZ, YZ)
    basex = quivers[xaxis]._segments3d[iLine][iEnd] * delta
    basey = quivers[yaxis]._segments3d[iLine][iEnd] * delta
    basez = quivers[zaxis]._segments3d[iLine][iEnd] * delta
    # Define the vertices and faces of the pyramid 
    vertices = np.array([basex, basey, basez, apex])
    x = vertices[:, xaxis]
    y = vertices[:, yaxis]
    z = vertices[:, zaxis]
    # Define the colors of each vertex
    colors_list = [quivers[i].get_color() for i in range(3)]
    colors_list.append([0, 0, 0, 1])  # apex is black
    ax.scatter(x, y, z, c=colors_list)

def plot_quaternion(ax, x, y, z, label):
    x_quiver = ax.quiver(0, 0, 0, *x, color='r')
    y_quiver = ax.quiver(0, 0, 0, *y, color='g')
    z_quiver = ax.quiver(0, 0, 0, *z, color='b')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(label)
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.set_zticks([-1, 0, 1])
    return np.array([x_quiver, y_quiver, z_quiver])

def plot_quaternion_rotation(a, b, c, d, delta=0.5, filename=None):
    # Create quaternion from input values
    q = from_float_array([a, b, c, d])
    # Define vectors for original and transformed coordinate systems
    x = np.array([1, 0, 0])
    y = np.array([0, 1, 0])
    z = np.array([0, 0, 1])
    # Create pyramid using center points of quivers
    fig = plt.figure(figsize=plt.figaspect(0.5))
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    quivers = plot_quaternion(ax1, x, y, z, 'Original Vector')
    print(f'quivers: {quivers}')
    plot_pyramid(ax1, quivers)
    plot_vertices(ax1, quivers)
    rotated_x = rotate_vectors(q, x)
    rotated_y = rotate_vectors(q, y)
    rotated_z = rotate_vectors(q, z)
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    quivers = plot_quaternion(ax2, rotated_x, rotated_y, rotated_z, 'Transformed Vector')
    print(f'quivers: {quivers}')
    plot_pyramid(ax2, quivers)
    plot_vertices(ax2, quivers)
    if filename:
        plt.savefig(f'./{filename}.svg', format='svg')
    plt.show()


def plot_pyramid(ax, quivers, delta=0.6):
    xaxis, yaxis, zaxis = 0, 1, 2
    iLine, iEnd, iStart = 0, 0, 1
    # Apex Point of pyramid is origin point x,y,z axis
    apex = np.array([0, 0, 0])
    # Three Base Points of pyramid (XY, XZ, YZ)
    basex = quivers[xaxis]._segments3d[iLine][iEnd] * delta
    basey = quivers[yaxis]._segments3d[iLine][iEnd] * delta
    basez = quivers[zaxis]._segments3d[iLine][iEnd] * delta
    # Define the vertices and faces of the pyramid 
    vertices = np.array([basex, basey, basez, apex])
    faces = [(0, 1, 3), (1, 2, 3), (2, 0, 3), (0, 1, 2)]
    # Define the vertex colors based on the quiver colors
    vertex_colors = [(1,1,0,1),(0,1,1,1), (1,0,1,1), (0.5, 0.5, 0.5, 1)]
    # Create a Poly3DCollection object with the vertices and faces
    poly = Poly3DCollection([vertices[face,:] for face in faces], facecolors=vertex_colors, alpha=1.0)
    # Add the Poly3DCollection to the plot
    ax.add_collection3d(poly)









