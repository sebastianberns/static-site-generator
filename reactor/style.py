#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path
from shutil import copy, rmtree

class CSS(object):
    def __init__(self, src, file, build):
        self.src = src
        self.file = file
        self.build = build
    
    def read(self):
        with open(self.src/self.file, "r") as f:
            content = f.read()
        return content
    
    def __format__(self, format_spec):
        src = self.src/self.file
        dst = self.build/self.file
        dir = dst.parent
        if dir.exists():
            rmtree(dir)
        
        if not src.exists():
            return ""
        
        if format_spec == 'inline':
            return '<style>\n{}\n</style>'.format(self.read())
        
        elif format_spec == 'external':
            os.makedirs(dir)
            copy(src, dst)
            return '<link href="{}" rel="stylesheet" type="text/css">'.format(self.file)
        
        return self.file
    
    def __repr__(self):
        return "<CSS: {}>".format(self.src/self.file)
