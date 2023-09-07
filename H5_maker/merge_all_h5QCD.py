import os, subprocess
from itertools import compress

path = '../../H5_Storage/QCD/'
files = os.listdir(path)
arr_2016_all = []
arr_2017 = []
arr_2018 = []
arr_2016 = []
arr_2016APV = []

low2016 = []
mid2016 = []
high2016 = []

for f in files:
    arr_2016.append("2016post" in f)
    arr_2016APV.append("2016pre" in f)
    arr_2017.append("2017" in f)
    arr_2018.append("2018" in f)


data2016 = list(compress(files, arr_2016))
data2016APV = list(compress(files, arr_2016APV))
data2017 = list(compress(files, arr_2017))
data2018 =  list(compress(files, arr_2018))

for f in data2016APV:
    low2016.append("HT1000to1500" in f)  
for f in data2016APV:
    mid2016.append('HT1500to2000' in f)
for f in data2016APV:
    high2016.append('HT2000toInf' in f)
  
low2016 = list(compress(data2016APV, low2016))
mid2016 = list(compress(data2016APV, mid2016))
high2016 = list(compress(data2016APV, high2016))


#strings to use as input for merge

string2016 = 'H5_merge.py QCD2016APV.h5 '
for i in range(2):
    string2016 = string2016 + ' ' + path+low2016[i]+ ' ' + path+mid2016[i]  + ' ' + path+high2016[i]
print(string2016)


'''
string2016APV = 'H5_merge.py QCD2016APV.h5 '
for f in data2016APV[:20]:
    string2016APV = string2016APV + ' ' + path+f



string2017 = 'H5_merge.py QCD2017.h5 '
for f in data2017[:20]:
    string2017 = string2017 + ' ' + path+f   
    

string2018 = 'H5_merge.py QCD2018.h5 '
for f in data2018[:20]:
    string2018 = string2018 + ' ' + path+f

print(string2018)


#subprocess.call("python H5_merge.py test.h5 ../../H5_Storage/QCD/QCD-HT2000toInf_nano-mc2016post-9_2016.h5 ../../H5_Storage/QCD/QCD-HT2000toInf_nano-mc2016post-3_2016.h5"  )
#Now actually running the script to merge all the QCD files by year

subprocess.call("python " + string2016)
subprocess.call("python " + string2016APV)
subprocess.call("python " + string2017)
subprocess.call("python " + string2018)



H5_merge.py QCD2016.h5  ../../H5_Storage/QCD/QCD-HT1000to1500_nano-mc2016post-1-10_2016.h5 ../../H5_Storage/QCD/QCD-HT1500to2000_nano-mc2016post-1-10_2016.h5 ../../H5_Storage/QCD/QCD-HT2000toInf_nano-mc2016post-1-10_2016.h5 ../../H5_Storage/QCD/QCD-HT1000to1500_nano-mc2016post-1-11_2016.h5 ../../H5_Storage/QCD/QCD-HT1500to2000_nano-mc2016post-1-11_2016.h5 ../../H5_Storage/QCD/QCD-HT2000toInf_nano-mc2016post-1-11_2016.h5 ../../H5_Storage/QCD/QCD-HT1000to1500_nano-mc2016post-30_2016.h5 ../../H5_Storage/QCD/QCD-HT1500to2000_nano-mc2016post-30_2016.h5 ../../H5_Storage/QCD/QCD-HT2000toInf_nano-mc2016post-31_2016.h5 ../../H5_Storage/QCD/QCD-HT1000to1500_nano-mc2016post-1-13_2016.h5 ../../H5_Storage/QCD/QCD-HT1500to2000_nano-mc2016post-1-13_2016.h5 ../../H5_Storage/QCD/QCD-HT2000toInf_nano-mc2016post-1-13_2016.h5 ../../H5_Storage/QCD/QCD-HT1000to1500_nano-mc2016post-1-14_2016.h5 ../../H5_Storage/QCD/QCD-HT1500to2000_nano-mc2016post-1-14_2016.h5 ../../H5_Storage/QCD/QCD-HT2000toInf_nano-mc2016post-1-14_2016.h5 ../../H5_Storage/QCD/QCD-HT1000to1500_nano-mc2016post-1-15_2016.h5 ../../H5_Storage/QCD/QCD-HT1500to2000_nano-mc2016post-1-15_2016.h5 ../../H5_Storage/QCD/QCD-HT2000toInf_nano-mc2016post-1-15_2016.h5 ../../H5_Storage/QCD/QCD-HT1000to1500_nano-mc2016post-1-16_2016.h5 ../../H5_Storage/QCD/QCD-HT1500to2000_nano-mc2016post-1-16_2016.h5 ../../H5_Storage/QCD/QCD-HT2000toInf_nano-mc2016post-1-16_2016.h5

'''
#print(string2016)

#files = subprocess.check_output('{} {}'.format(eosls, eos_path), shell=True)

# now you can check to see it worked
#print("Files in {}: {}".format(eos_path, files))

# If you want to do something with them, put it in this loop:
#for f in files.split('\n'):
#    print(f)



   