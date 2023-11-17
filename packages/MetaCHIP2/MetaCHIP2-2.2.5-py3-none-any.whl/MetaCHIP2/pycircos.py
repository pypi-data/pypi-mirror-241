from pycirclize import Circos
import pandas as pd

def pycircos(data_matrix):

    matrix_df = pd.read_csv('/Users/songweizhi/Desktop/demo.txt', sep='\t', header=0, index_col=0)

    # Initialize from matrix (Can also directly load tsv matrix file)
    circos = Circos.initialize_from_matrix(
        matrix_df,
        start=-265,
        end=95,
        space=5,
        r_lim=(93, 100),
        cmap="tab10",
        label_kws=dict(r=94, size=12, color="white"),
        link_kws=dict(ec="black", lw=0.5),
    )

    fig = circos.plotfig()
    fig.savefig("/Users/songweizhi/Desktop/result.png", dpi=100)



data_matrix =  '/Users/songweizhi/Desktop/test.csv'
plot_out    = '/Users/songweizhi/Desktop/result.png'
sep_symbol  = '\t'    # ',' or '\t'
column_name_pos = 0  # set first row as column name
row_name_pos = 0     # set first column as row name
transpose_csv(file_in, file_out, sep_symbol, column_name_pos, row_name_pos)