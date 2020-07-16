#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: EEGNet.py
# Author: stubborn vegeta
# Created Time: 2020年07月08日 星期三 16时14分13秒
##########################################################################
import sys
sys.path.append('../')
from pycore.tikzeng import *

arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_input('./EEG.jpg', width=8, height=6),
    to_Conv('conv2d', 750,25,6, offset='(0,0,0)',to="(0,0,0)",width=18, height=25,depth=50, caption='conv2d'),
    to_Pool('pool1', offset='(0,0,0)', to='(conv2d-east)',width=1,height=25,depth=50),
    to_Conv('layer2_1', '','','', offset='(3,2,0)',to="(conv2d-east)",width=6, height=1,depth=50, caption=''),
    to_Conv('layer2_2', '','','', offset='(3,0,0)',to="(conv2d-east)",width=6, height=1,depth=50, caption=''),
    to_Conv('layer2_3', 750,1,2, offset='(3,-2,0)',to="(conv2d-east)",width=6, height=1,depth=50, caption='depthwise\_conv2d'),
    to_PoolRelu('pool2_1',offset='(2.6,0,0)',to="(layer2_1-east)",width=6, height=1,depth=50, caption=''),
    to_PoolRelu('pool2_2',offset='(2.6,0,0)',to="(layer2_2-east)",width=6, height=1,depth=50, caption=''),
    to_PoolRelu('pool2_3',offset='(2.6,0,0)',to="(layer2_3-east)",width=6, height=1,depth=50, caption=''),
    to_Pool('pool2_1_0',offset='(0,0,0)',to="(pool2_1-east)",width=2, height=1,depth=25, caption=''),
    to_Pool('pool2_2_0',offset='(0,0,0)',to="(pool2_2-east)",width=2, height=1,depth=25, caption=''),
    to_Pool('pool2_3_0',187,'','',offset='(0,0,0)',to="(pool2_3-east)",width=2, height=1,depth=25, caption=''),
    to_Conv('layer3_1','','','',offset='(2,0,0)',to='(pool2_1_0-east)', width=6, height=1, depth=25, caption=''),
    to_Conv('layer3_2','','','',offset='(2,0,0)',to='(pool2_2_0-east)', width=6, height=1, depth=25, caption=''),
    to_Conv('layer3_3',187,'',2,offset='(2,0,0)',to='(pool2_3_0-east)', width=6, height=1, depth=25, caption='separable\_conv2d'),
    to_PoolRelu('pool3_1',offset='(1.5,0,0)',to="(layer3_1-east)",width=6, height=1,depth=25, caption=''),
    to_PoolRelu('pool3_2',offset='(1.5,0,0)',to="(layer3_2-east)",width=6, height=1,depth=25, caption=''),
    to_PoolRelu('pool3_3',offset='(1.5,0,0)',to="(layer3_3-east)",width=6, height=1,depth=25, caption=''),
    to_Pool('pool3_1_0',offset='(0,0,0)',to="(pool3_1-east)",width=2, height=1,depth=10, caption=''),
    to_Pool('pool3_2_0',offset='(0,0,0)',to="(pool3_2-east)",width=2, height=1,depth=10, caption=''),
    to_Pool('pool3_3_0',23,'','',offset='(0,0,0)',to="(pool3_3-east)",width=2, height=1,depth=10, caption=''),

    to_Flatten('flatten_1', 'z', 276, offset='(2.5,0,0)', to='(pool3_2_0-east)', width=1,height=1,depth=30,caption='flatten'),
    to_Flatten('out_1', 'z', 4, offset='(1.5,0,0)', to='(flatten_1-east)', width=1,height=1,depth=4,caption='dense'),

    to_connection('conv2d','layer2_1'),
    to_connection('conv2d','layer2_2'),
    to_connection('conv2d','layer2_3'),

    # to_dashed_connection_half('conv2d','layer2_1','up'),
    # to_dashed_connection_half('conv2d','layer2_3','down'),

    to_connection('layer2_1','pool2_1'),
    to_connection('layer2_2','pool2_2'),
    to_connection('layer2_3','pool2_3'),

    to_connection('pool2_1_0','layer3_1'),
    to_connection('pool2_2_0','layer3_2'),
    to_connection('pool2_3_0','layer3_3'),

    to_connection('layer3_1','pool3_1'),
    to_connection('layer3_2','pool3_2'),
    to_connection('layer3_3','pool3_3'),

    to_connection('pool3_1_0','flatten_1'),
    to_connection('pool3_2_0','flatten_1'),
    to_connection('pool3_3_0','flatten_1'),

    # to_dashed_connection_half('pool3_1_0','flatten_1','up'),
    # to_dashed_connection_half('pool3_3_0','flatten_1', 'down'),

    to_connection('flatten_1','out_1'),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')

if __name__ == '__main__':
    main()

