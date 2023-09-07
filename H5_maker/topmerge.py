import sys
import os, subprocess
path = '../../H5_Storage/JetHT_2016FGHruns/'
files = os.listdir(path)

args = ['python','H5_merge.py','../jet_images/2016JetHT_FGHruns.h5']
mx3000my300 = []
#num = 0
for f in files:
    mx3000my300.append('../../H5_Storage/JetHT_2016FGHruns/'+f)
   # num =num+1
    #if (num == 200):
     #   break     
args.extend(mx3000my300)
subprocess.call(args)
