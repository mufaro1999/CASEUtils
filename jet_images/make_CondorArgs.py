import os, subprocess
from itertools import compress

bkgpath = '../H5_maker/actual_merged_BkgH5data/'
sigpath = '../H5_maker/actual_merged_signalData/'

bkgfiles = os.listdir(bkgpath)
sigfiles = os.listdir(sigpath)

argFile = open('h5_arg_bkg.txt','w')
for f in bkgfiles:
    iFile = bkgpath + f
    oFile = f 
    argFile.write(' -i {} -o {}\n'.format(iFile, oFile))
argFile.close() 

argFile = open('h5_arg_sig.txt','w')
for f in sigfiles:
    iFile = sigpath + f
    oFile = f 
    argFile.write(' -i {} -o {}\n'.format(iFile, oFile))
argFile.close() 