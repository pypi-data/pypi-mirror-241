import del_cad
import matplotlib.pyplot as plt


def show_mesh(cad):
    tri2vtx, vtx2xy = cad.triangulation(0.13)
    fig2, ax2 = plt.subplots()
    ax2.set_aspect('equal')
    ax2.triplot(vtx2xy[:, 0], vtx2xy[:, 1], tri2vtx)
    plt.show()


if __name__ == "__main__":
    cad = del_cad.MyClass()
    i0_face = cad.add_polygon(
        [0.0, 0.0,
         1.0, 0.0,
         1.0, 1.0])
    assert (abs(cad.area_of_face(i0_face) - 0.5) < 1.0e-5)
    show_mesh(cad)
    ##
    i1_face = cad.add_polygon(
        [0.1, 0.2,
         1.1, 0.2,
         1.1, 1.2,
         0.1, 1.2])
    assert (abs(cad.area_of_face(i1_face) - 1.0) < 1.0e-5)
    show_mesh(cad)
