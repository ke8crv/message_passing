#!/bin/sh

if [ -t 0 ]
then
	DATA=$1
else
	DATA=$(cat)
fi


#https://github.com/DougGore/picopi
#speed 100 is normal

pico2wave -w tmp.wav "<speed level='100'>$DATA</speed>" && aplay tmp.wav
