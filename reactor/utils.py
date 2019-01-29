#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def filefilter(PATH, extensions=None):
    if type(extensions) != list:
        extensions = [extensions]
    
    def criterion(F):
        if F.is_file(): # Is file?
            if extensions == None: # Admit any extension
                return True
            if F.suffix[1:] in extensions: # Extension allowed?
                return True
        return False
    
    return list(filter(criterion, Path(PATH).glob('*')))
