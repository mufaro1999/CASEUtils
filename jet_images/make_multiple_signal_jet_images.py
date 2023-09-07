processes = ['MX2400_MY100','MX2400_MY250','MX2400_MY350','MX1600_MY150','MX2000_MY250','MX3000_MY190','MX3000_MY300','MX3000_MY400','MX2800_MY100','MX2800_MY190','MX2600_MY300']

import os, subprocess
import glob
from collections import OrderedDict
import sys
f = '-2'
for process in processes:
    years = ['2017']
    for year in years:
        fNames = subprocess.check_output(['ls ../H5_maker/h5_with_systematics/{}/{}/'.format(year,process)],shell=True).split('\n')
        fNames.remove('')
        if(not os.path.exists('analysis_note_jets/{}/{}'.format(year, process))):
                os.system('mkdir analysis_note_jets/{}/{}'.format(year, process))
        for fName in fNames:

            
            iFile = '/uscms/home/mchitoto/nobackup/XtoHY/CMSSW_11_1_4/src/CASEUtils/H5_maker/h5_with_systematics/{}/{}/{}'.format(year, process, fName)
            oFile = 'analysis_note_jets/{}/{}/{}'.format(year, process, fName)
        
            if(not os.path.exists(oFile)):
                                print('python make_jet_images.py -i {} -o {}'.format(iFile, oFile))
                                os.system('python make_jet_images.py -i {} -o {}'.format(iFile, oFile))
            else:
                                print("Skipping, %s already exists" % oFile)
            