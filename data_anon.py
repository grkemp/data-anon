#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    File name: data_anon.py
    Author: Grant Rodgers Kemp
    Date created: 09112019
    Date last modified: 09112019
    Python version: 3.6.9
'''

import pandas as pd
import numpy as np

def read_data():
    df = pd.read_excel('/Users/grantrodgerskemp/Box/corpus_paper/data/data_coding/inter-rater_reliability/nullovert123-OMJ-Reliability-grk.xlsx', sheet_name='data')
    df = df.loc[:, ['environment','tier']]
    df[df.tier != '%%svd:']

    print(df.head())

    return

read_data()