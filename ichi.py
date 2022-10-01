#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from oneblue import oneb1ue
from matplotlib import pyplot as plt
plt.style.use("solarized-light")
np.random.seed(39)
lmap = np.log(np.load("./assets/yozora-lmap.npz")["lmap"]).T
d_01 = pd.read_excel("./assets/D01.xlsx").values[ 1 : , 2 : ].astype(np.float64)
hcwm = np.load("./assets/hcwm-sst-20061224150039.npz")
for lab, cmap in [
  ("o", plt.matplotlib.cm.get_cmap("Greys")),
  ("r", plt.matplotlib.cm.get_cmap("Greys_r")),
  ("s", plt.matplotlib.cm.get_cmap("seismic")),
  ("x", oneb1ue.cmap),
  ("y", oneb1ue.dmap),
  ]:
  with plt.rc_context({"image.cmap": cmap }):
    with plt.rc_context({"figure.figsize": [ 16.4, 3.9 ]}):
      plt.grid(False)
      plt.pcolormesh(
        np.arange(lmap.shape[1]) * .005,
        np.logspace(np.log10(40), 3., lmap.shape[0], endpoint=True, base=10.),
        lmap,
        cmap = cmap
        )
      plt.xlabel("Time [s]")
      plt.ylabel("Frequency [Hz]")
      plt.ylim(None, 560)
      plt.title("(Nebula yielded) $F_0$ $\\log$-likelihood map of yozora by Hoshino-Ichika")
      plt.tight_layout()
      plt.savefig("./assets/yozora-lmap-%s.jpeg" % lab)
      plt.close()
    with plt.rc_context({"figure.figsize": [ 6., 5.6 ]}):
      plt.grid(False)
      plt.pcolormesh(d_01)
      plt.contour(d_01)
      plt.title("$IM^2C$ 2019 Prob-D-01")
      plt.tight_layout()
      plt.savefig("./assets/im2c2019d01-%s.jpeg" % lab)
      plt.close()
    with plt.rc_context({"figure.figsize": [ 7.6, 5.6 ]}):
      plt.grid(False)
      plt.pcolormesh(hcwm["long"], hcwm["lati"], hcwm["arr"], shading="gouraud")
      plt.contour(hcwm["long"], hcwm["lati"], hcwm["arr"])
      plt.xlabel("Longitude [deg]")
      plt.ylabel("Latitude  [deg]")
      plt.title("SST of Yellow Sea Cold Water Mass Area at 15:00, Dec 24$^{{th}}$, 2006")
      plt.colorbar().set_label("Temperature [K]")
      plt.tight_layout()
      plt.savefig("./assets/hcwm-sst-20061224150039-%s.jpeg" % lab)
      plt.close()