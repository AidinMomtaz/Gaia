import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import numpy as np

data=pd.read_csv("../data/Gaia_Data.csv")
mg=data["mg"]
bp_rp=data["bp_rp"]
cmap = plt.get_cmap("hot")
xy = np.vstack([bp_rp,mg])
z = gaussian_kde(xy)(xy)
# Create the plot with plt.scatter
plot = plt.scatter(bp_rp,mg, c=z, cmap=cmap, s=1)

cb = plt.colorbar(plot)

plt.xlim(0,6)
plt.ylim(15,-5)
plt.xlabel("Gbp-Grp")
plt.ylabel("mg")
plt.savefig("color-magnitude diagram", dpi=1200)
plt.show()
