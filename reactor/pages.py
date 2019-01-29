#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

import yaml

from .utils import filefilter


class Pages:
    def __init__(self, DIR, templates, file_extensions=["htm","html"], order="ASC"):
        self.files = filefilter(DIR, file_extensions)                   # get all admissible files in top directory
        self.content = Content(DIR, templates, order)
        self.pages = {f.stem: Page(f) for f in self.files}     # dict of one instance per file
    
    def build(self, style):
        for name, page in self.pages.items():
            page.build(self.content, style)
    
    def save(self, DIR):
        for name, page in self.pages.items():
            page.save(DIR)


class Page:
    def __init__(self, F):
        self.file = Path(F)
        self.name = self.file.stem
        self.ext = self.file.suffix[1:]
        self.page = None
    
    def build(self, content, style):
        with open(self.file, "r") as f:
            page = f.read()
        self.page = page.format(css=style, content=content)

    def save(self, DIR):
        assert self.page, "Build page before saving"
        with open(DIR/"{}.{}".format(self.name, self.ext), "w") as f:
            f.write(self.page)
        return True
    
    def __repr__(self):
        return "<File: {}>".format(self.src/self.file)


class Content:
    def __init__(self, SRC, templates, order="ASC"):
        self.src = SRC
        self.templates = templates
        self.order = order
    
    def __format__(self, format_spec):
        PATH = self.src/format_spec
        if not (PATH.exists() and PATH.is_dir()):
            'Path to content not found: "{}"'.format(PATH)
            return ""
        content = []
        files = filefilter(PATH, ["yaml"])
        if self.order == "DES":
            files = reversed(files)
        files = list(files)
        for f in files:
            with open(f, "r") as f:
                blocks = yaml.safe_load_all(f)
                for block in blocks:
                    t = block["template"]
                    try:
                        c = block["content"]
                    except:
                        c = ""
                    r = self.templates.render(t, c)
                    content.append(r)
        return "".join(content)
