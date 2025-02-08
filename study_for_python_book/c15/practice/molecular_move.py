import matplotlib.pyplot as plt
from molecular_walk import MolecularWalk


def start_move():
    mw = MolecularWalk()
    mw.fill_point()

    plt.figure(dpi=128, figsize=(10, 6))
    point_colors = list(range(mw.x_values))

    plt.plot(mw.x_values, mw.y_values, linewidth=1)
    cur_axis = plt.gca()
    cur_axis.get_xaxis().set_visible(False)
    cur_axis.get_yaxis().set_visible(False)

    plt.show()


start_move()