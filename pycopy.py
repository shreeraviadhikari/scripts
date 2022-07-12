#!/usr/bin/python3

import sys
import pyperclip 

pyperclip.copy(sys.stdin.read().strip())

