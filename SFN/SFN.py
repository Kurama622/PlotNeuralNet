#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: SFN.py
# Author: stubborn vegeta
# Created Time: 2020年07月08日 星期三 13时11分54秒
##########################################################################
import sys
sys.path.append('../')
from pycore.tikzeng import *
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_Conv('input', 750,25,'', offset='(0,0,0)',to="(0,0,0)",width=1, height=25,depth=50, caption='input'),
    to_Conv('layer1', 750,12,'', offset='(1.8,0,0)',to="(input-east)",width=1, height=12,depth=50, caption='layer1'),
    to_Linear('log-var', pos='y', n_unit='', offset='(1,0,0)',to="(layer1-east)",width=1, height=12,depth=2, caption='log-var'),
    to_LinearRelu('layer2', pos='y', n_unit=4, offset='(1,0,0)',to="(log-var-east)",width=1, height=4,depth=2, caption='layer2'),
    to_connection('input','layer1'),
    to_connection('layer1','log-var'),
    to_connection('log-var','layer2'),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')

if __name__ == '__main__':
    main()
