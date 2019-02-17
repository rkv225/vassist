#!/usr/bin/env python

import os

def operation(text):
    text = text.strip()
    print(text)
    text = text.replace(' ','\ ')
    text = text.replace("'", "")
    os.system("pico2wave -w audio_out.wav " + text + "&& aplay -D sysdefault:CARD=Device audio_out.wav")