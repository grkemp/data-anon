#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    File name: data_anon.py
    Author: Grant Rodgers Kemp
    Date created: 09112019
    Date last modified: 09252019
    Python version: 3.6.9
'''

import pandas as pd
import numpy as np

def read_data():
    '''Function reads in hard-coded filepath, need to change to use some method 
    of os. Reduces dataframe to the target environment column and the tier 
    columns. Indexes all %svd: tier rows and drops from the dataframe. Removes 
    tier column and passes environment column to be manipulated by the following
    function.'''
    df = pd.read_excel('/Users/grantrodgerskemp/Box/corpus_paper/data/data_coding/inter-rater_reliability/nullovert123-OMJ-Reliability-grk.xlsx',
    sheet_name='data')
    
    df = df.loc[:, ['environment','tier']]

    rm_svd = df[df['tier'] == '%svd:'].index
    df.drop(rm_svd, inplace=True)
    
    df = df.loc[:, ['environment']]

    print(df.head())

    return

read_data()