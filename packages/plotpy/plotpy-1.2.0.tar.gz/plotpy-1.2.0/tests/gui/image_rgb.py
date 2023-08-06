# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see plotpy/__init__.py for details)

"""RGB Image test, creating the RGBImageItem object via make.rgbimage"""

import os.path as osp

import plotpy
from plotpy.gui.widgets.baseplot import PlotType
from plotpy.gui.widgets.plot import PlotDialog
from plotpy.gui.widgets.builder import make

SHOW = True  # Show test in GUI-based test launcher

PLOTPYDIR = osp.abspath(osp.dirname(plotpy.__file__))
IMGFILE = osp.join(PLOTPYDIR, "images", "items", "image.png")


def imshow(filename):
    win = PlotDialog(
        edit=False,
        toolbar=True,
        wintitle="RGB image item test",
        options={"type": PlotType.IMAGE},
    )
    item = make.rgbimage(filename=filename, xdata=[-1, 1], ydata=[-1, 1])
    plot = win.get_plot()
    plot.add_item(item)
    win.show()
    win.exec_()


def test():
    """Test"""
    # -- Create QApplication
    import plotpy.gui

    _app = plotpy.gui.qapplication()
    # --
    imshow(IMGFILE)


if __name__ == "__main__":
    test()
