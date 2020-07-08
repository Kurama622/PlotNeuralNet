#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: my_NN.py
# Author: stubborn vegeta
# Created Time: 2020年07月01日 星期三 00时08分25秒
##########################################################################
import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_Conv("input", 32, 40, "", offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=32, caption="Input"),
    to_ConvRelu("conv1", 32, 12, 32, offset="(3,0,0)", to="(input-east)", width=5, height=32, depth=32, caption="Conv1" ),
    to_ConvRelu("conv2", 32, 4, 32, offset="(3,0,0)", to="(conv1-east)", width=5, height=12, depth=32 ,caption="Conv2"),

    to_LinearRelu("linear1",'z', 4096 ,"(2,0,0)", "(conv2-east)", caption="Flattening"  ),

    to_LinearRelu("linear2", 'z',512, "(2,0,0)", "(linear1-east)", width=1.5, height=3, depth=16, caption="Linear"),
    to_SoftMax("soft", 4 ,"(2,0,0)", "(linear2-east)", caption="LogSoftMax", depth=4  ),
    to_dashed_connection( "input", "conv1"),
    # to_dashed_connection( "conv1", "conv2"),
    # to_dashed_connection("conv2", "linear1"),
    to_connection( "input", "conv1"),
    to_connection( "conv1", "conv2"),
    to_connection("conv2", "linear1"),
    to_connection("linear1", "linear2"),
    to_connection( "linear2","soft"),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
