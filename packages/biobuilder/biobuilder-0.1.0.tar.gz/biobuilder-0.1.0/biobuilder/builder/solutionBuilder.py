#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
file: solutionBuilder.py
created time : 2021/04/18
last edit time : 2021/04/18
author : Zhenyu Wei 
version : 1.0
contact : zhenyuwei99@gmail.com
copyright : (C)Copyright 2021-2021, Zhenyu Wei and Southeast University
'''

from . import Builder


class SolutionBuilder(Builder):
    def __init__(self, system=None) -> None:
        super().__init__(system=system)