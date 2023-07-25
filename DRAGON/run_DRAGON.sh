#!/usr/bin/env bash

export DRAGON_DIR=/home/yago/public/git/DRAGON2-Beta_version
export WORKING_DIR=$(pwd)
export MODEL=run_2D_DM

cd $DRAGON_DIR
cp $WORKING_DIR/output/$MODEL* $WORKING_DIR/output/bak/
./DRAGON $WORKING_DIR/input/$MODEL.xml &> $WORKING_DIR/output/$MODEL\_output.txt
cp output/$MODEL* $WORKING_DIR/output/

: <<'Bye'
                                                         ... Paranoy@ rulz! ;^D
Bye

