import os, subprocess
import glob
from collections import OrderedDict
import sys
f = '1'
year = '2017'
processes = ['MX2400_MY100','MX2400_MY250','MX2400_MY350','MX1600_MY150','MX2000_MY250','MX3000_MY190','MX3000_MY300','MX3000_MY400','MX2800_MY100','MX2800_MY190','MX2600_MY300']
for process in processes:
	os.system('mkdir h5_with_systematics/{}/{}'.format(year,process))
	fNames = subprocess.check_output(['ls ../../H5_Storage/PFNano_with_systematics/{}/{}/'.format(year,process)],shell=True).split('\n')
	fNames.remove('')
	k = 0
	for fName in fNames:
		iFile = '/uscms/home/mchitoto/nobackup/XtoHY/CMSSW_11_1_4/src/H5_Storage/PFNano_with_systematics/{}/{}/{}'.format(year,process, fName)
		oFile = 'h5_with_systematics/{}/{}/{}_{}.h5'.format(year,process,process, k)
		k = k+1
		iYear = 2017
		if(not os.path.exists(oFile)):
			print('python make_h5_local.py -i {} -o {} -y {} -f {} --sys'.format(iFile, oFile, iYear, f))
			os.system('python make_h5_local.py -i {} -o {} -y {} -f {} --sys'.format(iFile, oFile, iYear, f))
		else:
        				print("Skipping, %s already exists" % oFile)
		
		

