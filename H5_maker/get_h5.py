import subprocess
import glob
import os
from collections import OrderedDict
import sys

def CombineCommonSets(year):
    '''
	year (str) = 2016APV, 2016, 2017, 2018
    '''
    datasets = {
	year: {
	    'QCDHT1000to1500': None,
	    'QCDHT1500to2000': None,
	    'QCDHT2000toInf': None
        }
    }
    for HTcat in ['1000to1500','1500to2000','2000toInf']:
	argStr = ' '.join(glob.glob('H5_output/QCD-HT{}_*_{}.h5'.format(HTcat,year)))
	print('Concatenating H5 files for {}, {}'.format(HTcat, year))
	subprocess.call('python H5_merge.py {}_{}.h5 {}'.format(HTcat, year, argStr),shell=True)


redirector = 'root://cmsxrootd.fnal.gov/'
eosls = 'eos root://cmseos.fnal.gov ls'
eosdir = '/store/user/ammitra/H5_output'

if __name__=='__main__':
    print('{} {}'.format(eosls,eosdir))
    fNames = subprocess.check_output(['{} {}'.format(eosls,eosdir)],shell=True).split('\n')
    fNames.remove('')
    for fName in fNames:
	toCopy = '{}{}/{} H5_output/'.format(redirector,eosdir,fName)
	print('xrdcp {}'.format(toCopy))	
	subprocess.call('xrdcp {}'.format(toCopy),shell=True)	# add -f to force copy

    for year in ['2016','2016APV','2017','2018']:
	CombineCommonSets(year)
