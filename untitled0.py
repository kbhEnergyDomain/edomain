# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 10:53:44 2019

@author: kbhus
"""

input_list = [[1,2,3], [ 4,5,6], [7,8,9]]


output_list = [ list(x) for x in zip(*input_list) ]
print(output_list)