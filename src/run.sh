#!/bin/sh
cd /home/jdoe93410/Projects/message_passing/src
python ARRLMessage.py | espeak -v en-us -p50 -s120 -g 20
