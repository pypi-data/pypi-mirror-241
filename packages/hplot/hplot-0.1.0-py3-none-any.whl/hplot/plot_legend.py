from typing import List, Optional, Tuple, Union
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors as mcolors
from hplot.config import hConfig


def plot_legend(
    legends: List[str],
    fname: Optional[str] = None,
    *,
    linestyles: Optional[List[str]] = None,
    linecolors: Optional[List[str]] = None,
    linewidths: Optional[List[float]] = None,
    ncol: Optional[int] = 1,
    figure_width: Optional[float] = 10,
    figure_height: Optional[float] = 0.32,
    display: Optional[bool] = False,
):
    plt.cla()
    plt.clf()
    plt.close()
    handles = []
    if linestyles is not None:
        assert len(legends) == len(linestyles)
    if linecolors is not None:
        assert len(legends) == len(linecolors)
    else:
        tableau_colors = cycle(mcolors.TABLEAU_COLORS)
        linecolors = [next(tableau_colors) for _ in range(len(legends))]

    if linewidths is not None:
        assert len(legends) == len(linewidths)

    for i, ele in enumerate(legends):
        lw = linewidths[i] if linewidths is not None else 2
        ls = linestyles[i] if linestyles is not None else "-"
        lc = linecolors[i]
        (line,) = plt.plot(range(10), label="line{}".format(i), lw=lw, ls=ls, color=lc)
        handles.append(line)
    fig, ax = plt.subplots(figsize=(figure_width, figure_height))
    lgd = ax.legend(
        handles=handles,
        labels=legends,
        mode="expand",
        ncol=ncol,
        borderaxespad=0,
        prop=hConfig.legend_font,
    )
    ax.axis("off")  # 去掉坐标的刻度

    lgd_fig = lgd.figure
    lgd_fig.canvas.draw()
    bbox = lgd.get_window_extent().transformed(lgd_fig.dpi_scale_trans.inverted())

    if fname is not None:
        lgd_fig.savefig(fname, bbox_inches=bbox, pad_inches=0)
    if display:
        plt.show()
    plt.close()
