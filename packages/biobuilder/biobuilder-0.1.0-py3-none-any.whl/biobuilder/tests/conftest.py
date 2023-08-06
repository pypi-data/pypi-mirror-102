#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
file: conftest.py
created time : 2021/04/18
last edit time : 2021/04/18
author : Zhenyu Wei 
version : 1.0
contact : zhenyuwei99@gmail.com
copyright : (C)Copyright 2021-2021, Zhenyu Wei and Southeast University
'''

test_order = [
     'judgement',
     'locate',
     'unique',
     'baseDimension',
     'unit',
     'quantity',
     'unitDefinition'
]

def pytest_collection_modifyitems(items):
     current_index = 0
     for test in test_order:
          indexes = []
          for id, item in enumerate(items):
               if 'test_'+test+'.py' in item.nodeid:
                    indexes.append(id)  
          for id, index in enumerate(indexes):
               items[current_index+id], items[index] = items[index], items[current_index+id]
          current_index += len(indexes)
