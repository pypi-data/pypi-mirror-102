#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
file: builder.py
created time : 2021/04/18
last edit time : 2021/04/18
author : Zhenyu Wei 
version : 1.0
contact : zhenyuwei99@gmail.com
copyright : (C)Copyright 2021-2021, Zhenyu Wei and Southeast University
'''

from .. import System


class Builder:
    def __init__(self, system=None) -> None:
        if system == None:
            self._system = System()
        else:
            self._system = system