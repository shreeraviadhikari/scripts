#!/usr/local/bin/python

import sys
import pyperclip

pyperclip.copy(sys.stdin.read().strip())
