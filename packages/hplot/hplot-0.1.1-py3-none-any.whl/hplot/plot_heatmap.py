from typing import List, Union, Optional

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import rcParams

from hplot.config import hConfig
from hplot.utils import cm2inch
from hplot.base import Base
from matplotlib.colors import Colormap

class plot_heatmap(Base):
    def __init__(
            self,
            x: Union[np.ndarray, List[float]],
            y: Union[np.ndarray, List[float]],
            z: Union[np.ndarray, List[List[float]]],
            fname: str,
            *,
            cmap: Union[str, Colormap] = "BrBG",
            vmin: float ,
            vmax: float,
            center:float=None,
            levels: Optional[List[float]]=None,
            level_colors: Optional[List[str]]=None,
            xlabel: str=None,
            ylabel:str=None,
            display:bool=False,
            **kwargs,
            ):
        """
        :param x: Union[np.ndarray, List[float]]
        :param y: Union[np.ndarray, List[float]]
        :param z: Union[np.ndarray, List[List[float]]]
        :param fname: str
        :param cmap: Union[str, Colormap]
        :param vmin: float
        :param vmax: float
        :param center: float
        :param levels: Optional[List[float]]
        :param level_colors: Optional[List[str]]
        :param xlabel: str
        :param ylabel: str
        :param display: bool
        :param kwargs["xtick_labels"]: List[str]
        :param kwargs["ytick_labels"]: List[str]
        """
        super().__init__(**kwargs)
        self.x = x
        self.y = y
        self.z = z
        self.fname = fname
        self.cmap = cmap
        self.vmin = vmin
        self.vmax = vmax
        self.center = center
        self.levels = levels
        self.level_colors = level_colors
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.display = display
        self.fig = None
        self.ax = None
        plt.cla()
        plt.clf()
        plt.close()
        self.__preprocess()
        self.run()

    def __preprocess(self):
        rcParams.update({"mathtext.fontset": "stix"})

        # use tex to render fonts, tex install required
        if hConfig.usetex:
            from matplotlib import rc
            rc("font", **{"family": "serif", "serif": ["Times New Roman"]})
            rc("text", usetex=True)

    def plot(self):
        self.fig, self.ax = plt.subplots(figsize=cm2inch(*hConfig.fig_size), dpi=hConfig.dpi)
        # plot figure
        if isinstance(self.cmap, str):
            cmap = plt.get_cmap(self.cmap)
        else:
            cmap = self.cmap

        self.ax = sns.heatmap(
            self.z,
            cmap=cmap,
            vmin=self.vmin,
            vmax=self.vmax,
            center=self.center,
        )

        cbar = self.ax.collections[0].colorbar
        cbar.ax.tick_params(labelsize=hConfig.tick_size)
        labels = cbar.ax.get_yticklabels()
        [label.set_fontname(hConfig.tick_label_font) for label in labels]
        if self.levels:
            plt.contour(self.z, colors=self.level_colors, levels=self.levels)

        xtick_labels = self._kwargs.get("xtick_labels", None)
        ytick_labels = self._kwargs.get("ytick_labels", None)
        if xtick_labels is not None:
            pos_list_x = self._tick2pos(xtick_labels, self.x)
            plt.xticks(pos_list_x, xtick_labels, rotation=0)
        if ytick_labels is not None:
            pos_list_y = self._tick2pos(ytick_labels, self.y)
            plt.yticks(pos_list_y, ytick_labels)

        if self.xlabel:
            plt.xlabel(self.xlabel, hConfig.label_font)
        if self.ylabel:
            plt.ylabel(self.ylabel, hConfig.label_font)

    
        plt.tick_params(labelsize=hConfig.tick_size)
        labels = self.ax.get_xticklabels() + self.ax.get_yticklabels()
        [label.set_fontname(hConfig.tick_label_font) for label in labels]
        self.ax.invert_yaxis()

    def _tick2pos(
        self,
        tick: Union[np.ndarray, List[float]],
        anchor: Union[np.ndarray, List[float]],
    ) -> List[int]:
        pos = []

        if isinstance(anchor, list):
            anchor = np.array(anchor).reshape(-1)

        for t in tick:
            t = float(t)
            dist = (anchor - t) ** 2
            label = np.argmin(dist)
            pos.append(int(label))
        return pos
