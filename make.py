#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

import sass
import yaml

import reactor


HOME = Path()

configfile = HOME/"config.yaml"
with open(configfile, 'r') as f:
    config = yaml.safe_load(f)  # Load config

SRC   = HOME/config['source']
BUILD = HOME/config['build']


# SASS = SRC / config['sass']
# CSS  = SRC / config['css']
sass.compile(
    dirname=(SRC/"scss", SRC/"css"),
    output_style='expanded')             # Compile stylesheet
reactor.main.build()                     # Build site
reactor.main.refresh(config['browser'])  # Open in/refresh browser
