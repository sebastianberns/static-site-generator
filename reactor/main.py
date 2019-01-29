#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import subprocess

import yaml

from .pages import Pages
from .style import CSS
from .templates import Templates
from .utils import filefilter


""" Absolute paths """
HOME = Path()


def build():
    """ Config """
    configfile = HOME/"config.yaml"
    with open(configfile, 'r') as f:
        config = yaml.safe_load(f)

    """ App paths """
    SRC   = HOME/config['source']
    BUILD = HOME/config['build']
    TEMPL = HOME/config['templates']
    
    """ Templates """
    templates = Templates(TEMPL)
    
    """ Stylesheet """
    style = CSS(SRC, config['style'], BUILD)

    """ Pages """
    pages = Pages(SRC, templates, config['extensions'], config['fileorder'])
    pages.build(style)
    pages.save(BUILD)


def refresh(browser):
    PATH = HOME/"reactor"/"browser"
    files = filefilter(PATH, ["scpt", "scptd", "applescript"])  # all script files
    browsers = {f.stem: f for f in files}  # file names w/o extension map to full file names
    if browser in browsers.keys():
        subprocess.Popen(
            ['osascript', browsers[browser],
            HOME.absolute().as_uri()],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )


if __name__ == "__main__":
    build()
