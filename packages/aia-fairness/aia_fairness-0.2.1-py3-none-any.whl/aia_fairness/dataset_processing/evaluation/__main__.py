import pickle

from .. import metric
from .. import config

dp_lvl = {}

for dset in config.config.dsets:
    dp_lvl[dset] = {}
    for attrib in config.config.attribs:
        dp_lvl[dset][attrib] = metric.dp_lvl(dset, attrib)

with open("data_eval.pickle", "wb") as f:
    pickle.dump(dp_lvl,f)

tex = """
\\documentclass{article}
\\begin{document}
\\begin{tabular}"""
length = len(dp_lvl.keys())
col = "{c|"
for i in range(length):
    col += "c"
col += "}\n"
tex += col
tex += "&"
for dset in dp_lvl.keys():
    tex += f"{dset}&"
tex = tex[:-1]
tex += "\\\\"
tex += "\n"
tex += "\\hline\n"

for attrib in config.config.attribs:
    tex += f"{attrib}&"
    for dset in config.config.dsets:
        tex += f"{round(dp_lvl[dset][attrib],3)}&"
    tex = tex[:-1]
    tex += "\\\\"
    tex += "\n"

tex +="""
\\end{tabular}
\\end{document}
"""
with open("data_eval.tex", 'w') as f:
    f.write(tex)
