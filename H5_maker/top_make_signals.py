import sys
import os, subprocess

for num in range(243):
    subprocess.call('python make_h5_local.py -i root://cmsxrootd.fnal.gov//store/user/lpcpfnano/ammitra/v2_3/2017/XHYPrivate/NMSSM_XToYH_MX3000_MY300_HTo2bYTo2W_hadronicDecay/NMSSM_XToYH_MX3000_MY300_HTo2bYTo2W_hadronicDecay/221013_151454/0000/nano_mc2017_{}.root -o topsignals/MX3000_MY300_{}.h5 -y 2017 -f 1'.format(num+1,num+1), shell=True) 