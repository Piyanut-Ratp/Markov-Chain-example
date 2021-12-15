#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 18:32:18 2021

@author: piyanut

cite: https://www.youtube.com/watch?v=B9LOMA43tPA&list=PLlCuQCjEEYuRnzjPrZh6ErsB-zfMitjTO&index=2
"""

#import library
import numpy as np 
import matplotlib.pyplot as plt 

#input parameters
all_posible_state = [0,1] # 0 Sunny | 1 Rainy
num_time_step = 10
num_sequences = 10


#----------------------------------------------------#
def true_table():
    #true transition probability table

    """
    0 Sunny | 1 Rainy
    -------------------
    row | col
    t-1 | t
    0 | 0 : P(Sunny t | Sunny t-1) = 0.9
    0 | 1 : P(Rainy t | Sunny t-1) = 0.1
    1 | 0 : P(Sunny t | Rainy t-1) = 0.1
    1 | 1 : P(Rainy t | Rainy t-1) = 0.9
    """

    true_trans_prob = np.array([[0.9, 0.1],
                                [0.1, 0.9]])

    #true initial probability table
    """
    row
    t=0
    0 : P(Sunny t=0)
    1 : P(Rainy t=0)
    """
    true_init_prob = np.array([0.5, 0.5])

    return true_init_prob, true_trans_prob

#sequence generator
def sequence_generator(true_init_prob, true_trans_prob, num_time_step, num_sequences):
    
    all_sequences = [] #list collect all sequence
    
#----------------------------------------------------#
#----------------------------------------------------#
#testing
true_init_prob, true_trans_prob = true_table()





