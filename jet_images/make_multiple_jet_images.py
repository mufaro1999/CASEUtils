import os, subprocess
import glob
from collections import OrderedDict
import sys
f = '-2'
years = ['2016','2016APV','2017','2018']
process = 'data'
for year in years:
	fNames = subprocess.check_output(['ls ../H5_maker/h5_with_systematics/{}/{}/'.format(year,process)],shell=True).split('\n')
	fNames.remove('')
	
	for fName in fNames:
		
		iFile = '/uscms/home/mchitoto/nobackup/XtoHY/CMSSW_11_1_4/src/CASEUtils/H5_maker/h5_with_systematics/{}/{}/{}'.format(year, process, fName)
		oFile = 'analysis_note_jets/{}/{}/{}'.format(year, process, fName)
	
		if(not os.path.exists(oFile)):
        					print('python make_jet_images.py -i {} -o {}'.format(iFile, oFile))
		    				os.system('python make_jet_images.py -i {} -o {}'.format(iFile, oFile))
    	else:
       	    				print("Skipping, %s already exists" % oFile)
		