# -*- coding: utf-8 -*-
#
# Copyright © 2009-2010 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see plotpy/__init__.py for details)

"""
plotpy test package
===================
"""


def run():
    """Run plotpy test launcher"""
    import plotpy.core.config.config  # Loading icons

    try:
        from tests.gui.guitest import run_testlauncher
    except ImportError:
        from plotpy.tests.gui.guitest import run_testlauncher
    import plotpy.gui

    run_testlauncher(plotpy.gui, "tests.gui")


if __name__ == "__main__":
    run()
