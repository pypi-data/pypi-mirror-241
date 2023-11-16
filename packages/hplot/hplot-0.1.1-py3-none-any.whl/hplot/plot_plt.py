from itertools import cycle
from typing import Dict, List, Optional

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from matplotlib import rcParams

from hplot.base import Base
from hplot.config import hConfig
from hplot.utils import cm2inch


class plot_plt(Base):
    def __init__(
        self,
        data: List[Dict],
        fname: Optional[str] = None,
        *,
        xlabel: Optional[str] = None,
        ylabel: Optional[str] = None,
        legend: Optional[List[str]] = None,
        display: Optional[bool] = False,
        **kwargs
    ):
        """
        :param data: list[dict]:
            data used to plot figures,
            example: [dict(x=x1, y=y1), dict(x=x2, y=y2)]
        :param fname:str,
            the figure will be saved here,
            example: "./path_to_file/figure.png"
        :param xlabel: str
        :param ylabel: str
        :param legend: list[str]
        :param display: bool
        :param kwargs["color_list"]:
        :param kwargs["legend_loc"]: str
            "best", "upper right", "upper left", "lower left", "lower right", "right", "center left",
            "center right", "lower center", "upper center", "center"
        :param kwargs["legend_ncol"]: int
            number of columns in legend
        :param kwargs["xlim"]:
        :param kwargs["ylim"]:
        :param kwargs["xticks"]:
        :param kwargs["yticks"]:
        :param kwargs["xtick_labels"]:
        :param kwargs["ytick_labels"]:

        """
        super().__init__(**kwargs)
        self.data = data
        self.fname = fname
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.legend = legend
        self.display = display

        self.num_data = None
        self.fig = None
        self.ax = None
        plt.cla()
        plt.clf()
        plt.close()
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

        # color list
        cl = self._kwargs.get("color_list", None)
        if (cl is None) or len(cl) < self.num_data:
            tableau_colors = cycle(mcolors.TABLEAU_COLORS)
            self._kwargs["color_list"] = [next(tableau_colors) for _ in range(self.num_data)]

    def plot(self):
        self.fig, self.ax = plt.subplots(figsize=cm2inch(*hConfig.fig_size), dpi=hConfig.dpi)

        # plot figure
        cl = self._kwargs.get("color_list", None)
        assert cl is not None
        for i, d in enumerate(self.data):
            plt.plot(d["x"], d["y"], color=cl[i])

        # legend
        plt.tick_params(labelsize=hConfig.tick_size)
        labels = self.ax.get_xticklabels() + self.ax.get_yticklabels()
        [label.set_fontname(hConfig.tick_label_font) for label in labels]

        if self.legend is not None:
            plt.legend(
                self.legend,
                loc=self._kwargs.get("legend_loc", "best"),
                ncol=self._kwargs.get("legend_ncol", 1),
                prop=hConfig.legend_font,
            )

        #  label
        if self.xlabel is not None:
            plt.xlabel(self.xlabel, hConfig.label_font)
        if self.ylabel is not None:
            plt.ylabel(self.ylabel, hConfig.label_font)

        xlim = self._kwargs.get("xlim", None)
        if xlim is not None:
            plt.xlim(xlim)
        ylim = self._kwargs.get("ylim", None)
        if ylim is not None:
            plt.ylim(ylim)

        xticks = self._kwargs.get("xticks", None)
        yticks = self._kwargs.get("yticks", None)
        xtick_labels = self._kwargs.get("xtick_labels", None)
        ytick_labels = self._kwargs.get("ytick_labels", None)

        if xticks is not None and xtick_labels is not None:
            plt.xticks(xticks, xtick_labels)
        if yticks is not None and ytick_labels is not None:
            plt.yticks(yticks, ytick_labels)
