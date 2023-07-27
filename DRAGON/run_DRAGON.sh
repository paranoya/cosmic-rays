#!/usr/bin/env bash

export DRAGON_DIR=/home/yago/public/git/DRAGON2-Beta_version
export WORKING_DIR=$(pwd)

if [[ $# != 1 ]];
then
    echo "USAGE: run_DRAGON <model_name>"
    exit
fi

cd $DRAGON_DIR
for MODEL in $@
do
    [ -f "$WORKING_DIR/output/$MODEL.fits.gz" ] && cp $WORKING_DIR/output/$MODEL* $WORKING_DIR/output/bak/
    ./DRAGON $WORKING_DIR/input/$MODEL.xml &> $WORKING_DIR/output/$MODEL\_output.txt
    [ -f "output/$MODEL.fits.gz" ] && cp output/$MODEL* $WORKING_DIR/output/
done

: <<'Bye'
                                                         ... Paranoy@ rulz! ;^D
Bye

