import os, subprocess

redirector = 'root://cmseos.fnal.gov/'
eos_path = '/store/user/mchitoto/H5_input'
eosls = 'eos root://cmseos.fnal.gov ls'


import os, subprocess

bkgpath = 'actual_merged_BkgH5data/'
sigpath = 'actual_merged_signalData/'

bkgfiles = os.listdir(bkgpath)
sigfiles = os.listdir(sigpath)


#for f in bkgfiles:
#    subprocess.call('xrdcp {} {}{}/{}'.format(bkgpath+f,redirector, eos_path, f), shell=True)
for f in sigfiles:
    subprocess.call('xrdcp {} {}{}/{}'.format(sigpath+f,redirector, eos_path, f), shell=True)