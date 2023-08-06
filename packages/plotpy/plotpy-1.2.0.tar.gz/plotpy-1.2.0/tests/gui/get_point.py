# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see plotpy/__init__.py for details)

"""
SelectPointTool test

This plotpy tool provide a MATLAB-like "ginput" feature.
"""

SHOW = True  # Show test in GUI-based test launcher

from plotpy.gui.widgets.baseplot import PlotType
from plotpy.gui.widgets.plot import PlotDialog
from plotpy.gui.widgets.tools import SelectPointTool
from plotpy.gui.widgets.builder import make
from plotpy.gui.widgets.config import _


def test_function(tool):
    print("Current coordinates:", tool.get_coordinates())


def get_point(*args):
    """
    Plot curves and return selected point(s) coordinates
    """
    win = PlotDialog(
        _("Select one point then press OK to accept"),
        edit=True,
        options={"type": PlotType.CURVE},
    )
    default = win.add_tool(
        SelectPointTool,
        title="Test",
        on_active_item=True,
        mode="create",
        end_callback=test_function,
    )
    default.activate()
    plot = win.get_plot()
    for cx, cy in args:
        item = make.mcurve(cx, cy)
        plot.add_item(item)
    plot.set_active_item(item)
    win.show()
    if win.exec_():
        return default.get_coordinates()


def test():
    """Test"""
    # -- Create QApplication
    import plotpy.gui

    _app = plotpy.gui.qapplication()
    # --
    from numpy import linspace, sin

    x = linspace(-10, 10, 1000)
    y = sin(sin(sin(x)))
    x2 = linspace(-10, 10, 20)
    y2 = sin(sin(sin(x2)))
    print(get_point((x, y), (x2, y2), (x, sin(2 * y))))


if __name__ == "__main__":
    test()
