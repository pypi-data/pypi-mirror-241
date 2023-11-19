import pickle
import matplotlib.pyplot as plt
from pathlib import Path
import os


def boxplot(dset, attrib, evaltype, metric):

    targets  = os.listdir(Path("result"))
    m = []
    l = []
    for target in targets:
        try:
            with open(Path("result",target,evaltype,dset,attrib,f"{metric}.pickle"), 'rb') as f:
                m += [pickle.load(f)]
                l += [target]
        except:
            pass

    try:
        plt.boxplot(m,labels=l)
    except:
        print(f"{dset} {attrib} {evaltype} {metric}")
        quit()
    plt.ylabel(metric)
    plt.xticks(rotation=30, ha="right")
    path = Path("plot",dset,attrib,evaltype)
    os.makedirs(path,exist_ok=True)
    plt.savefig(Path(path,f"{metric}.pdf"), bbox_inches="tight")
    plt.clf()


def latex():
    size = 0.49
    tex = """\\documentclass{article}
\\usepackage{graphicx}
\\begin{document}
"""
    dsets = os.listdir(Path("plot"))
    for dset in dsets:
        tex += f"\\section{{ {dset} }}\n"
        attribs = os.listdir(Path("plot",dset))
        for attrib in attribs:
            tex += f"\\subsection{{ {attrib} }}\n"
            evaltypes = os.listdir(Path("plot",dset,attrib))
            for evaltype in evaltypes:
                tex += f"\\subsubsection{{ {evaltype} }}\n"
                if evaltype=="attack":
                    atypes = os.listdir(Path("plot",dset,attrib,evaltype,))
                    tex += "\\begin{tabular}{c}\n"
                    for atype in atypes:
                        tex += f"{atype}\\\\ \n"
                        metrics = os.listdir(Path("plot",dset,attrib,evaltype,atype))
                        for metric in metrics:
                            tex += f"\\includegraphics[width={size}\\linewidth]{{ plot/{dset}/{attrib}/{evaltype}/{atype}/{metric} }}\n"
                        tex += "\\\\"
                    tex += "\\end{tabular}\n"

                else:
                    metrics = os.listdir(Path("plot",dset,attrib,evaltype))
                    for metric in metrics:
                        tex += f"\\includegraphics[width={size}\\linewidth]{{ plot/{dset}/{attrib}/{evaltype}/{metric} }}\n"

    tex += "\\end{document}\n"

    with open("main.tex", 'w') as f:
        f.write(tex)






