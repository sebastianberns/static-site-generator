#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

import pystache

from .utils import filefilter


class Templates:
    def __init__(self, DIR):
        self.files = filefilter(DIR, ["mustache"])
        self.templates = {f.stem: Template(f) for f in self.files}
        self.renderer = pystache.Renderer(search_dirs=DIR)
    
    def render(self, name, data):
        template = self.templates[name].parse()
        return self.renderer.render(template, data)


class Template:
    def __init__(self, F):
        self.file = Path(F)
        self.name = self.file.stem
        self.name = self.file.suffix[1:]
        self.parsed = None
    
    def read(self):
        with open(self.file, "r") as f:
            content = f.read()
        return content
    
    def parse(self):
        if not self.parsed:
            template = self.read()
            self.parsed = pystache.parse(template)
        return self.parsed
    
    def __repr__(self):
        return "<Template: {}>".format(self.src/self.file)
