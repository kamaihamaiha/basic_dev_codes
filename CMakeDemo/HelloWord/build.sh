#!/bin/zsh

rm -rf output # clear temp dir
mkdir output
cd output

cmake .. # 在临时目录中创建工程
make
./hello-world
./cmd-dir .