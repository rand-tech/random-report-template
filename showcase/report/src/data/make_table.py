import os
import pandas as pd


class Table:
    def __init__(self, filename, caption, label):
        self.filename = filename
        self.caption = caption
        self.label = label

    def LaTeXTable(self):
        outputfilename = f'latex_{self.filename}.tex'

        df = pd.read_csv(self.filename, sep='\t', float_precision=None)
        latex_table = df.to_latex(index=False, caption=self.caption,
                                  label=f"tab:py_{self.label}", escape=False, column_format="c"*df.count(axis='columns')[0], position='H', na_rep='')
        latex_table = latex_table.replace('#', '')
        with open(outputfilename, 'w') as f:
            f.write(latex_table)
            print("file:", f'src/data/{outputfilename}')

os.chdir(os.path.dirname(os.path.realpath(__file__)))

Table('e_showcase.csv', "Showcase(数式$T_\mathrm{A}$)", "generals").LaTeXTable()
