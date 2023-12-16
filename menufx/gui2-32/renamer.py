import os
import glob
import re
import time
color = 'yellow'

for infilename in glob.iglob('**/*.png', recursive=True):
    if "yellow" in infilename or "green" in infilename or "blue" in infilename or "white" in infilename:
        print(infilename)

time.sleep(100)