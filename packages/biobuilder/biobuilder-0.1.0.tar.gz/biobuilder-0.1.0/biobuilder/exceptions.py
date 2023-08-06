#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
file: exceptions.py
created time : 2021/04/18
last edit time : 2021/04/18
author : Zhenyu Wei 
version : 1.0
contact : zhenyuwei99@gmail.com
copyright : (C)Copyright 2021-2021, Zhenyu Wei and Southeast University
'''

class PeptideTypeError(Exception):
    """
    PeptideTypeError related to the peptide type error
    Used in
    - biobuilder.utils.judgement 
    """ 
    pass

class UnitDimensionDismatchError(Exception):
    '''
    UnitDimensionDismatchError raises when the base dimension of unit does not matched
    Used in:
    - biobuilder.unit.unit.Unit
    - biobuilder.unit.quantity.Quantity
    '''
    pass

class DividingZeroError(Exception):
    '''
    DividingZeroError raises when value is divided by a zero 
    Used in:
    - biobuilder.unit.quantity.Quantity
    '''
    pass