#!/bin/bash


python3 $1.py 

/usr/local/texlive/2019/bin/x86_64-linux/xelatex $1.tex

rm *.aux *.log *.vscodeLog
rm *.tex

if [[ "$OSTYPE" == "darwin"* ]]; then
    open $1.pdf
else
    xdg-open $1.pdf
fi
