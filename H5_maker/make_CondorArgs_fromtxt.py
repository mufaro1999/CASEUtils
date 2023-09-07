import subprocess
import glob
import os
from collections import OrderedDict
import sys




with open('DataC_16APV.txt') as f:
    lines = f.readlines()
print(lines)
# loop over dataset dictionary


# create arg file
#argFile = open('DataC2016APV_arg_{}.txt'.format(year),'w')
for line in lines:	
    nuline = line.strip('\n')
    print(nuline)
    #argFile.write(' -i {} -o {} -y {} -f {}\n'.format(iFile, oFile, iYear, f))
# close file
#argFile.close()
