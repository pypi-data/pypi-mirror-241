import matplotlib.patches
import numpy
import del_cad
import matplotlib.pyplot as plt

if __name__ == "__main__":
    vtx2xy_in = numpy.array([
        [0, 0],
        [1,0],
        [1,0.6],
        [0.6,0.6],
        [0.6,1.0],
        [0,1]],dtype=numpy.float32)
    print(vtx2xy_in)
    _, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.add_patch(matplotlib.patches.Polygon(xy=vtx2xy_in, closed=True))
    plt.show()
    ##
    tri2vtx, vtx2xy = del_cad.tesselation2d(vtx2xy_in)
    _, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.triplot(vtx2xy[:, 0], vtx2xy[:, 1], tri2vtx)
    plt.show()
