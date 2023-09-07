import os, subprocess

redirector = 'root://cmseos.fnal.gov/'
eos_path = '/store/user/mchitoto/H5_output'
eosls = 'eos root://cmseos.fnal.gov ls'

files = subprocess.check_output('{} {}'.format(eosls, eos_path), shell=True)

# now you can check to see it worked
print("Files in {}: {}".format(eos_path, files))

# If you want to do something with them, put it in this loop:
for f in files.split('\n'):
    
    if(not os.path.exists('data/{}'.format(f))):
        subprocess.call('xrdcp {}{}/{} data'.format(redirector, eos_path, f), shell=True) 
		#print('python make_h5_local.py -i {} -o {} -y {} -f {} --sys'.format(iFile, oFile, iYear, 0))
    else:
        print("Skipping, %s already exists" % f)