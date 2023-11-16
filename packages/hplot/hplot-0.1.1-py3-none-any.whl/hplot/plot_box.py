import os
from typing import Dict, List, Optional
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import rcParams

from hplot.config import hConfig
from hplot.utils import cm2inch
from hplot.base import Base 

class plot_box(Base):
    def __init__(
        self,
        data: List[Dict],
        fname: Optional[str] = None,
        *,
        xlabel: Optional[str] = None,
        ylabel: Optional[str] = None,
        width: Optional[float] =0.5,
        linewidth: Optional[float] =1.0,
        display: Optional[bool] = False,
        **kwargs
    ):
        """
        :params data (list of dict): each dict with keys "label" and "y"
        :params fname (str, optional): figure save path. Defaults to None.
        :param xlabel: str
        :param ylabel: str
        :params width (float, optional): width of each box. Defaults to 0.5.
        :params linewidth (float, optional): linewidth of box boundary. Defaults to 1.0.
        :params theme (str, optional): theme of seaborn. Defaults to None. darkgrid, whitegrid, dark, white, ticks
        :param kwargs["style"]: str
        "white", "dark", "whitegrid", "darkgrid"
        """
        super().__init__(**kwargs)
        self.data = data
        self.fname = fname
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.width = width
        self.linewidth = linewidth
        self.display = display

        self.fig = None
        self.ax = None
        plt.cla()
        plt.clf()
        plt.close()
        self.ax = None
        self.fig = None
        style = kwargs.get("style", "white")
        sns.set_style(style)
        self.__preprocess()
        self.run()

    def __preprocess(self):
        rcParams.update({"mathtext.fontset": "stix"})
        assert isinstance(self.data, (dict, list, tuple))

        if isinstance(self.data, dict):
            self.data = [self.data]
        self.num_data = len(self.data)


        # use tex to render fonts, tex install required
        if hConfig.usetex:
            from matplotlib import rc
            rc("font", **{"family": "serif", "serif": ["Times New Roman"]})
            rc("text", usetex=True)

    def plot(self):
        self.fig, self.ax = plt.subplots(figsize=cm2inch(*hConfig.fig_size), dpi=hConfig.dpi)

        data_dict = dict()

        for subdata in self.data:
            data_dict[subdata["label"]] = subdata["y"]

        df = pd.DataFrame(data_dict)
        sns.boxplot(data=df, width=self.width, linewidth=self.linewidth)

        # tick
        plt.tick_params(labelsize=hConfig.tick_size)
        labels = self.ax.get_xticklabels() + self.ax.get_yticklabels()
        [label.set_fontname(hConfig.tick_label_font) for label in labels]

        # label
        if self.xlabel is not None:
            plt.xlabel(self.xlabel, fontdict=hConfig.label_font)
        if self.ylabel is not None:
            plt.ylabel(self.ylabel, fontdict=hConfig.label_font)

