import subprocess
import glob
import os
import sys

redirector = 'root://cmsxrootd.fnal.gov/'
eosls = 'eos root://cmseos.fnal.gov ls'

# open the txt file containing the location of all the signal files
locFile = open('PFNano_signals_2017.txt','r')

# get each line of the file in a list
locs = locFile.readlines()

# open new file to write to
fOut = open('SignalArgs.txt','w')

# loop over the list
for loc in locs:
    # get rid of the carriage return at the end of the directory name
    loc = loc.strip('\n')
    # run "eosls" on the directory name
    # the output fNames will be a list of the file names in each directory
    fNames = subprocess.check_output(['{} {}'.format(eosls,loc)],shell=True).split('\n')
    fNames.remove('') # get rid of random empty entry
    fNames.remove('log')
    # loop over all the file names
    for fName in fNames:
        # create arguments
        iFile = '{}{}{}'.format(redirector, loc, fName)
        procName = loc.split('/')[8].split('_')
        mX = procName[2]
        mY = procName[3]
        year = loc.split('/')[6]
        oFile = '{}-{}_{}_{}.h5'.format(mX,mY,fName.split('.')[0].replace('_','-'),year)

        # write to file
        fOut.write(' -i {} -o {} -y {} -f 0\n'.format(iFile, oFile, year))

fOut.close()