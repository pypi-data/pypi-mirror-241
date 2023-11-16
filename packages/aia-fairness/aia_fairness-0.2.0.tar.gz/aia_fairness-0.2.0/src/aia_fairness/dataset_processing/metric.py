import numpy as np

from .__init__ import load_format

def dp_lvl(dset, attrib):
    data = load_format(dset, attrib)
    a0 = np.mean(data["y"][data["z"]==0]==0)
    a1 = np.mean(data["y"][data["z"]==1]==1)
    return np.abs(a0-a1)


