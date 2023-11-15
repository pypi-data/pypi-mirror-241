import os
from abc import ABCMeta, abstractmethod

import matplotlib.pyplot as plt

from hplot.config import hConfig


class Base(metaclass=ABCMeta):
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self.fname = None
        self.fig = None
        self.ax = None
        self.pad = None
        self.display = None

    @abstractmethod
    def plot(self):
        pass

    def save(self):
        self.fig.set_tight_layout(True)
        plt.tight_layout(pad=hConfig.pad)
        if self.fname is None:
            pass
        else:
            dir_path = os.path.dirname(self.fname)
            os.makedirs(dir_path, exist_ok=True)
            plt.savefig(self.fname)

    def show(self):
        self.fig.set_tight_layout(True)
        plt.tight_layout(pad=hConfig.pad)
        plt.show()

    def close(self):
        plt.close()

    def run(self):
        self.plot()
        if self.fname is not None:
            self.save()
        if self.display:
            self.show()
        self.close()
