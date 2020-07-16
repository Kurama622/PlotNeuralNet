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
    to_input('./EEG.jpg',to="(-2,0,0)",width=8,height=6),
    # to_Conv("input", 32, 40, "", offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=32, caption="Input"),
    to_ConvRelu("conv1", 32, 12, 32, offset="(0,0,0)", to="(0,0,0)", width=10, height=12, depth=32, caption="Conv1" ),
    to_ConvRelu("conv2", 32, 4, 32, offset="(1.2,0,0)", to="(conv1-east)", width=10, height=4, depth=32 ,caption="Conv2"),
    to_ConvRelu("conv3", 1, 4, 32, offset="(1.2,0,0)", to="(conv2-east)", width=10, height=4, depth=1.5 ,caption="Conv3"),

    to_Flatten("linear1",'z', 128 ,"(1.2,0,0)", "(conv3-east)", caption="Flatten", width=1.5, height=2, depth=50),


    # to_Linear("linear2", 'z',512, "(1.2,0,0)", "(linear1-east)", width=1.5, height=3, depth=16, caption="Linear"),
    to_SoftMax("soft", 4 ,"(1.2,0,0)", "(linear1-east)", caption="LogSoftMax", depth=4  ),
    # to_dashed_connection( "input", "conv1"),
    # to_dashed_connection( "conv1", "conv2"),
    # to_dashed_connection("conv2", "linear1"),
    # to_connection( "input", "conv1"),
    to_connection( "conv1", "conv2"),
    to_connection( "conv2", "conv3"),
    to_connection("conv3", "linear1"),
    # to_connection("linear1", "linear2"),
    to_connection( "linear1","soft"),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
