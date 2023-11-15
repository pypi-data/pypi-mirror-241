class Config:
    def __init__(self):
        self.fig_size = (8.5, 6.5)
        self.dpi = 600
        self.pad = 0.2

        self.tick_size = 8

        self.base_font = "Times New Roman"
        self.base_font_weight = "normal"
        self.tick_label_font = self.base_font
        self.legend_font = {"family": self.base_font, "size": "8", "weight": self.base_font_weight}
        self.label_font = {"family": self.base_font, "size": "9", "weight": self.base_font_weight}

        self.usetex = False

    def keys(self):
        return [
            "fig_size",
            "dpi",
            "pad",
            "tick_size",
            "base_font",
            "base_font_weight",
            "tick_label_font",
            "legend_font",
            "label_font",
            "usetex",
        ]


hConfig = Config()
