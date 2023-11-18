import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


def get_boxplot(num_lol, label_list, label_rotation, extra_value_list, shape_list, color_list, output_plot):

    num_lol_arrary = [np.array(i) for i in num_lol]

    fig = plt.figure(1, figsize=(9, 6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(num_lol_arrary)
    ax.set_xticklabels(label_list, rotation=label_rotation, fontsize=8)

    # add dots, https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html
    col_index = 1
    for num_arrary in num_lol_arrary:
        plt.plot(np.random.normal(col_index, 0.02, len(num_arrary)), num_arrary, '.', alpha=0.5, color='grey',
                 markersize=6, markeredgewidth=0)
        col_index += 1

    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='+', color='black', alpha=0.7, markersize=3)

    # add extra values, https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html
    x_index = 1
    for value, shape, color in zip(extra_value_list, shape_list, color_list):
        plt.plot(x_index, value, alpha=1, marker=shape, markersize=10, markeredgewidth=0, color=color)
        x_index += 1

    # export plot
    plt.tight_layout()
    fig.savefig(output_plot, bbox_inches='tight', dpi=300)
    plt.close()


num_lol             = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
label_list          = ['Apl', 'Car', 'Cli']
extra_value_list    = [7, 2, 4]
shape_list          = ['^', 'v', 'v']
color_list          = ['coral', 'deepskyblue', 'deepskyblue']
label_rotation      = 0

output_plot = '/Users/songweizhi/Desktop/Boxplot_with_extra_values.pdf'
get_boxplot(num_lol, label_list, label_rotation, extra_value_list, shape_list, color_list, output_plot)

