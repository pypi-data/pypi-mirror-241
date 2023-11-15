import os
from typing import Dict, List, Optional
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import rcParams

from hplot.config import hConfig
from hplot.utils import cm2inch
from hplot.base import Base

class plot_sns(Base):
    def __init__(self,         
        data: List[Dict],
        fname: Optional[str] = None,
        *,
        xlabel: Optional[str] = None,
        ylabel: Optional[str] = None,
        legend: Optional[List[str]] = None,
        display: Optional[bool] = False,
        **kwargs):
        """
        :param data: list[dict]:
            data used to plot figures,
            example: [dict(x=x1_list, y=y1_list, label=label1), dict(x=x2_list, y=y2_list, label=label2)]
            when there is no repeat experiment data, xi_list=x, shape of x is [d,],
                                                    yi_list=y, shape of y is [d,],
                                                    lableli str,
            when there is repeat experiment data, xi_list=[x1, x2, ..., xd], shape of xi is [d,],
                                                yi_list=[y1, y2, ..., yd], shape of y is [d,],
                                                lableli str,
        :param fname: fname: str,
            the figure will be saved here,
            example: "./path_to_file/figure.png"
        :param xlabel:  str
        :param ylabel:  str
        :param legend: list[str]
        :param display: bool
        :param kwargs["style"]: str
            "white", "dark", "whitegrid", "darkgrid"
        :param kwargs["linewidths"]: List[str]
        :param kwargs["linestyles"]: List[str]
        :param kwargs["legend_loc"]: str
            "best", "upper right", "upper left", "lower left", "lower right", "right", "center left",
            "center right", "lower center", "upper center", "center"
        :param kwargs["legend_frameon"]: bool
        :param kwargs["legend_ncol"]: int
            number of columns in legend
        :param kwargs["show_legend"]: bool
        :param kwargs["xlim"]:
        :param kwargs["ylim"]:
        :param kwargs["xticks"]:
        :param kwargs["yticks"]:
        :param kwargs["xtick_labels"]:
        :param kwargs["ytick_labels"]:
        :param kwargs["log_yaxis"]: bool
        :param kwargs["ticklabel_style"]: "sci" or "plain"
        :param kwargs["ticklabel_style_axis"]: "x" or "y" or "both"
        :param kwargs["log_yaxis"]: bool

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

    def _ppc_data(self, d):
        x = d["x"]
        y = d["y"]
        label = d["label"]
        if isinstance(x, np.ndarray):
            x = [x]
        if isinstance(y, np.ndarray):
            y = [y]

        assert len(x) == len(y)

        for i in range(len(x)):
            x[i] = x[i].reshape(-1)
            y[i] = y[i].reshape(-1)
            assert x[i].shape == y[i].shape
        x = np.stack(x)
        y = np.stack(y)

        x = x.reshape(-1)
        y = y.reshape(-1)
        return x, y, label
    
    def plot(self):
        self.fig, self.ax = plt.subplots(figsize=cm2inch(*hConfig.fig_size), dpi=hConfig.dpi)
        # plot figure
        lws = self._kwargs.get("linewidths", None)
        if lws is not None:
            assert len(self.data) == len(lws)
        
        lss = self._kwargs.get("linestyles", None)
        if lss is not None:
            assert len(self.data) == len(lss)

        for i, d in enumerate(self.data):
            x, y, label = self._ppc_data(d)
            lw = lws[i] if lws is not None else 2
            ls = lss[i] if lss is not None else "-"
            sns.lineplot(x=x, y=y, label=label, linewidth=lw, ls=ls)

        # tick
        plt.tick_params(labelsize=hConfig.tick_size)
        labels = self.ax.get_xticklabels() + self.ax.get_yticklabels()
        [label.set_fontname(hConfig.tick_label_font) for label in labels]

        # set legend
        legend_handles, legend_labels = self.ax.get_legend_handles_labels()
        legend_dict = dict()
        legend_dict["handles"] = legend_handles
        legend_dict["labels"] = self.legend if self.legend is not None else legend_labels
        legend_dict["columnspacing"] = 0.3
        legend_loc = self._kwargs.get("legend_loc", "best")
        legend_dict["loc"] = "best" if legend_loc is None else legend_loc
        legend_dict["frameon"] = self._kwargs.get("legend_frameon", True)
        legend_dict["prop"] = hConfig.legend_font

        ncol = self._kwargs.get("legend_ncol", 1)
        if ncol is not None:
            legend_dict["ncol"] = ncol

        if self._kwargs.get("show_legend", True):
            self.ax.legend(**legend_dict)
        else:
            plt.legend([], [], frameon=False)

        #  label
        if self.xlabel is not None:
            plt.xlabel(self.xlabel, hConfig.label_font)
        if self.xlabel is not None:
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

        ticklabel_style = self._kwargs.get("ticklabel_style", None)
        ticklabel_style_axis = self._kwargs.get("ticklabel_style_axis", "x")
        if ticklabel_style:
            plt.ticklabel_format(style=ticklabel_style, axis=ticklabel_style_axis, scilimits=(0, 0))

        log_yaxis = self._kwargs.get("log_yaxis", None)
        if log_yaxis is not None:
            plt.yscale("log")
