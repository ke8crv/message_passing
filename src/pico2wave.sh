#!/bin/sh

pico2wave -w tmp.wav "Testing 123" && aplay tmp.wav
