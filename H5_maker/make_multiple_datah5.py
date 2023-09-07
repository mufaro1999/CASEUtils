import os, subprocess


redirector = 'root://cmseos.fnal.gov/'
#eos_path = '//store/group/lpcpfnano/cmantill/v2_3/2018/JetHT2018/JetHT/JetHT_Run2018D/220801_141548/0000'
#eos_path = '//store/group/lpcpfnano/cmantill/v2_3/2018/JetHT2018/JetHT/JetHT_Run2018D/220801_141548/0001'
#eos_path = '//store/group/lpcpfnano/cmantill/v2_3/2018/JetHT2018/JetHT/JetHT_Run2018D/220801_141548/0002'
#eos_path = '//store/group/lpcpfnano/cmantill/v2_3/2018/JetHT2018/JetHT/JetHT_Run2018A/220701_194145/0000'
#eos_path = '//store/group/lpcpfnano/cmantill/v2_3/2018/JetHT2018/JetHT/JetHT_Run2018B/220701_194212/0000'
eos_path = '//store/group/lpcpfnano/cmantill/v2_3/2018/JetHT2018/JetHT/JetHT_Run2018C/220701_194237/0000'
eosls = 'eos root://cmseos.fnal.gov ls'

files = subprocess.check_output('{} {}'.format(eosls, eos_path), shell=True)




for f in files.split('\n')[1:]:
    #print(f)
    name = f.split('.')[0]
    oFile  = 'h5_with_systematics/2018/data/runC2018_'+name+'.h5'
    iFile = redirector+eos_path+'/'+f
    iYear =  2018
    if(not os.path.exists(oFile)):
        os.system('python make_h5_local.py -i {} -o {} -y {} -f {} '.format(iFile, oFile, iYear, 0))
		#print('python make_h5_local.py -i {} -o {} -y {} -f {} --sys'.format(iFile, oFile, iYear, 0))
    else:
        print("Skipping, %s already exists" % oFile)
