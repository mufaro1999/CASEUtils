import subprocess
import glob
import os
from collections import OrderedDict
import sys

redirector = 'root://cmsxrootd.fnal.gov/'
eosls = 'eos root://cmseos.fnal.gov ls'

datasets = {
    "2017": {
        #"JetHT_Run2018D": "/store/group/lpcpfnano/cmantill/v2_3/2018/JetHT2018/JetHT/JetHT_Run2018D/220801_141548/0000/",
		#"JetHT_Run2018D1": "/store/group/lpcpfnano/cmantill/v2_3/2018/JetHT2018/JetHT/JetHT_Run2018D/220801_141548/0001/",
		#"JetHT_Run2018D2": "/store/group/lpcpfnano/cmantill/v2_3/2018/JetHT2018/JetHT/JetHT_Run2018D/220801_141548/0002/",
        #"JetHT_Run2018A": "/store/group/lpcpfnano/cmantill/v2_3/2018/JetHT2018/JetHT/JetHT_Run2018A/220701_194145/0000/",
        #"JetHT_Run2018B": "/store/group/lpcpfnano/cmantill/v2_3/2018/JetHT2018/JetHT/JetHT_Run2018B/220701_194212/0000/",
        #"JetHT_Run2018C": "/store/group/lpcpfnano/cmantill/v2_3/2018/JetHT2018/JetHT/JetHT_Run2018C/220701_194237/0000/",
		#"JetHT_Run2016B_ver2_HIPM": "/store/group/lpcpfnano/cmantill/v2_3/2016/JetHT2016/JetHT/JetHT_Run2016B_ver2_HIPM/220701_193532/0000/",
		#"JetHT_Run2016C_HIPM": "/store/group/lpcpfnano/cmantill/v2_3/2016/JetHT2016/JetHT/JetHT_Run2016C_HIPM/220701_193745/0000/",
		#"JetHT_Run2016D_HIPM": "/store/group/lpcpfnano/cmantill/v2_3/2016/JetHT2016/JetHT/JetHT_Run2016D_HIPM/220701_193811/0000/",
		#"JetHT_Run2016E_HIPM": "/store/group/lpcpfnano/cmantill/v2_3/2016/JetHT2016/JetHT/JetHT_Run2016E_HIPM/220701_193836/0000/",
		#"JetHT_Run2016F": "/store/group/lpcpfnano/cmantill/v2_3/2016/JetHT2016/JetHT/JetHT_Run2016F/220701_193506/0000/",
		#"JetHT_Run2016F_HIPM": "/store/group/lpcpfnano/cmantill/v2_3/2016/JetHT2016/JetHT/JetHT_Run2016F_HIPM/220701_193559/0000/",
		#"JetHT_Run2016G": "/store/group/lpcpfnano/cmantill/v2_3/2016/JetHT2016/JetHT/JetHT_Run2016G/220701_193626/0000/",
		#"JetHT_Run2016G1": "/store/group/lpcpfnano/cmantill/v2_3/2016/JetHT2016/JetHT/JetHT_Run2016G/220701_193626/0001/",
		#"JetHT_Run2016H": "/store/group/lpcpfnano/cmantill/v2_3/2016/JetHT2016/JetHT/JetHT_Run2016H/220701_193717/0000/",
		#"JetHT_Run2016H": "/store/group/lpcpfnano/cmantill/v2_3/2016/JetHT2016/JetHT/JetHT_Run2016H/220801_140806/0000/"
		"JetHT_Run2017B": "/store/group/lpcpfnano/cmantill/v2_3/2017/JetHT2017/JetHT/JetHT_Run2017B/220701_194050/0000/",
		"JetHT_Run2017C": "/store/group/lpcpfnano/cmantill/v2_3/2017/JetHT2017/JetHT/JetHT_Run2017C/220701_194023/0000/",
		"JetHT_Run2017D": "/store/group/lpcpfnano/cmantill/v2_3/2017/JetHT2017/JetHT/JetHT_Run2017D/220701_193930/0000/",
		"JetHT_Run2017E": "/store/group/lpcpfnano/cmantill/v2_3/2017/JetHT2017/JetHT/JetHT_Run2017E/220701_193905/0000/",
		"JetHT_Run2017F": "/store/group/lpcpfnano/cmantill/v2_3/2017/JetHT2017/JetHT/JetHT_Run2017F/220701_193956/0000/",
		"JetHT_Run2017F1": "/store/group/lpcpfnano/cmantill/v2_3/2017/JetHT2017/JetHT/JetHT_Run2017F/220701_193956/0001/",
     }
   

}


if __name__=='__main__':
    # loop over dataset dictionary
    for year, dataset in datasets.items():
	# create arg file
	argFile = open('JetHT_Args_{}.txt'.format(year),'w')
	for process, path in dataset.items():
	    f=0
	    # get the file names
	    fNames = subprocess.check_output(['{} {}'.format(eosls,path)],shell=True).split('\n')
	    fNames.remove('')
	    #fNames.remove('log')
	    for fName in fNames:
	        # create arguments
	        iFile = '{}{}{}'.format(redirector, path, fName)
	        oFile = '{}_{}.h5'.format(process, fName.split('.')[0])
	        iYear = 2016 if 'APV' in year else year
	        # write to file
	        argFile.write(' -i {} -o {} -y {} -f {}\n'.format(iFile, oFile, iYear, f))
	# close file
	argFile.close()