import os, subprocess
from itertools import compress

bkgpath = '../H5_maker/actual_merged_BkgH5data/'
sigpath = '../H5_maker/actual_merged_signalData/'

bkgfiles = os.listdir(bkgpath)
sigfiles = os.listdir(sigpath)

'''
print(bkgfiles)
#f = bkgfiles[-2]
f = 'arrTTToSemiLeptonic2016.h5'
subprocess.call(['python','make_jet_images.py','-i', bkgpath +f, '-o', 'Bkg_JetImages/'+f])

for f in bkgfiles[1]:
    subprocess.call(['python','make_jet_images.py','-i', bkgpath +f, '-o', 'Bkg_JetImages/'+f])
'''
'''
for f in sigfiles:
    subprocess.call(['python','make_jet_images.py','-i', bkgpath +f, '-o', 'Sig_JetImages/'+f])
'''
subprocess.call(['python','make_jet_images.py','-i', bkgpath +'QCD2016APV.h5', '-o', 'Bkg_JetImages/'+ 'QCD2016APV.h5'])