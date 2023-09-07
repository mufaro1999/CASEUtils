import os, subprocess
from itertools import compress

path = '../../H5_Storage/Bkg/'
files = os.listdir(path)
arr_2016_all = []
arr_2017 = []
arr_2018 = []
arr_2016 = []
arr_2016APV = []

for f in files:
    arr_2016.append("2016post" in f)
    arr_2016APV.append("2016pre" in f)
    arr_2017.append("2017" in f)
    arr_2018.append("2018" in f)

#data from each year before separating the different backgrounds
data2016 = list(compress(files, arr_2016))
data2016APV = list(compress(files, arr_2016APV))
#data2017 = list(compress(files, arr_2017))
data2018 =  list(compress(files, arr_2018))

#TTJets 2016
TTjets2016 = []
for f in data2016:
    TTjets2016.append('TTJets' in f) 
arrTTJets2016 = list(compress(data2016, TTjets2016))

#TTJets 2016APV
TTjets2016APV = []
for f in data2016APV:
    TTjets2016APV.append('TTJets' in f) 
arrTTJets2016APV = list(compress(data2016APV, TTjets2016APV))

#TTJets 2018
TTjets2018 = []
for f in data2018:
    TTjets2018.append('TTJets' in f) 
arrTTJets2018 = list(compress(data2018, TTjets2018))

#TTJets Done! Now on to TTTo2L2Nu


#TTTo2L2Nu 2016
TTTo2L2Nu2016 = []
for f in data2016:
    TTTo2L2Nu2016.append('TTTo2L2Nu' in f) 
arrTTTo2L2Nu2016 = list(compress(data2016, TTTo2L2Nu2016))

#TTTo2L2Nu 2016APV
TTTo2L2Nu2016APV = []
for f in data2016APV:
    TTTo2L2Nu2016APV.append('TTTo2L2Nu' in f) 
arrTTTo2L2Nu2016APV = list(compress(data2016APV, TTTo2L2Nu2016APV))

#TTTo2L2Nu 2016
TTTo2L2Nu2018 = []
for f in data2018:
    TTTo2L2Nu2018.append('TTTo2L2Nu' in f) 
arrTTTo2L2Nu2018 = list(compress(data2018, TTTo2L2Nu2018))

#TTTo2LNu are done now! on to TTToHadronic

#TTToHadronic 2016
TTToHadronic2016 = []
for f in data2016:
    TTToHadronic2016.append('TTToHadronic' in f) 
arrTTToHadronic2016 = list(compress(data2016, TTToHadronic2016))

#TTToHadronicAPV 2016
TTToHadronic2016APV = []
for f in data2016APV:
    TTToHadronic2016APV.append('TTToHadronic' in f) 
arrTTToHadronic2016APV = list(compress(data2016APV, TTToHadronic2016APV))

#TTToHadronic 2018
TTToHadronic2018 = []
for f in data2018:
    TTToHadronic2018.append('TTToHadronic' in f) 
arrTTToHadronic2018 = list(compress(data2018, TTToHadronic2018))

#TTToHadronic are done now, on to SemiLeptonic

#TTToSemiLeptonic 2016
TTToSemiLeptonic2016 = []
for f in data2016:
    TTToSemiLeptonic2016.append('TTToSemiLeptonic' in f) 
arrTTToSemiLeptonic2016 = list(compress(data2016, TTToSemiLeptonic2016))

#TTToSemiLeptonicAPV 2016
TTToSemiLeptonic2016APV = []
for f in data2016APV:
    TTToSemiLeptonic2016APV.append('TTToSemiLeptonic' in f) 
arrTTToSemiLeptonic2016APV = list(compress(data2016APV, TTToSemiLeptonic2016APV))

#TTToHadronic 2018
TTToSemiLeptonic2018 = []
for f in data2018:
    TTToSemiLeptonic2018.append('TTToSemiLeptonic' in f) 
arrTTToSemiLeptonic2018 = list(compress(data2018, TTToSemiLeptonic2018))

#TTToSemiLeptonic are done now, on to WJetsToQQ!

#WJetsToQQ 2016
WJetsToQQ2016 = []
for f in data2016:
    WJetsToQQ2016.append('WJetsToQQ' in f) 
arrWJetsToQQ2016 = list(compress(data2016, WJetsToQQ2016))

#WJetsToQQ 2016APV
WJetsToQQ2016APV = []
for f in data2016APV:
    WJetsToQQ2016APV.append('WJetsToQQ' in f) 
arrWJetsToQQ2016APV = list(compress(data2016APV, WJetsToQQ2016APV))

#WJetsToQQ 2018
WJetsToQQ2018 = []
for f in data2018:
    WJetsToQQ2018.append('WJetsToQQ' in f) 
arrWJetsToQQ2018 = list(compress(data2018, WJetsToQQ2018))


#ZJetsToQQ 2016
ZJetsToQQ2016 = []
for f in data2016:
    ZJetsToQQ2016.append('ZJetsToQQ' in f) 
arrZJetsToQQ2016 = list(compress(data2016, ZJetsToQQ2016))

#ZJetsToQQ 2016APV
ZJetsToQQ2016APV = []
for f in data2016APV:
    ZJetsToQQ2016APV.append('ZJetsToQQ' in f) 
arrZJetsToQQ2016APV = list(compress(data2016APV, ZJetsToQQ2016APV))

#ZJetsToQQ 2016
ZJetsToQQ2018 = []
for f in data2018:
    ZJetsToQQ2018.append('ZJetsToQQ' in f) 
arrZJetsToQQ2018 = list(compress(data2018, ZJetsToQQ2018))



#Arrays of Data we have at this point are:
#arrTTJets2016 (EMPTY), arrTTJets2016AP (EMPTY), arrTTJets2018, arrTTTo2L2Nu2016, arrTTTo2L2Nu2016APV, arrTTTo2L2Nu2018, arrTTToHadronic2016 
#arrTTToHadronic2016APV, arrTTToHadronic2018, arrTTToSemiLeptonic2016, arrTTToSemiLeptonic2016APV, arrTTToSemiLeptonic2018 
#arrWJetsToQQ2016, arrWJetsToQQ2016APV, arrWJetsToQQ2018, arrZJetsToQQ2016, arrZJetsToQQ2016APV, arrZJetsToQQ2018
#UPON EXAMINATION ALL THE ARRAYS ARE FULL EXCEPT THE FIRST 2


#making arrays into paths by appending the path to their location
arrTTJets2018 = [path + f for f in arrTTJets2018]

arrTTTo2L2Nu2016 = [path + f for f in arrTTTo2L2Nu2016]
arrTTTo2L2Nu2016APV = [path + f for f in arrTTTo2L2Nu2016APV]
arrTTTo2L2Nu2018 = [path + f for f in arrTTTo2L2Nu2018]

arrTTToHadronic2016 = [path + f for f in arrTTToHadronic2016]
arrTTToHadronic2016APV = [path + f for f in arrTTToHadronic2016APV]
arrTTToHadronic2018 = [path + f for f in arrTTToHadronic2018]

arrTTToSemiLeptonic2016 = [path + f for f in arrTTToSemiLeptonic2016]
arrTTToSemiLeptonic2016APV = [path + f for f in arrTTToSemiLeptonic2016APV]
arrTTToSemiLeptonic2018 = [path + f for f in arrTTToSemiLeptonic2018]

arrWJetsToQQ2016 = [path + f for f in arrWJetsToQQ2016]
arrWJetsToQQ2016APV = [path + f for f in arrWJetsToQQ2016APV]
arrWJetsToQQ2018 = [path + f for f in arrWJetsToQQ2018]

arrZJetsToQQ2016 = [path + f for f in arrZJetsToQQ2016]
arrZJetsToQQ2016APV = [path + f for f in arrZJetsToQQ2016APV]
arrZJetsToQQ2018 = [path + f for f in arrZJetsToQQ2018]




#Now We Merge all these 16 arrays

#arrTTJets2018
args = ['python','H5_merge.py','arrTTJets2018.h5']
args.extend(arrTTJets2018)
subprocess.call(args)

#arrTTTo2L2Nu2016
args = ['python','H5_merge.py','arrTTTo2L2Nu2016.h5']
args.extend(arrTTTo2L2Nu2016)
subprocess.call(args)

#arrTTTo2L2Nu2016APV
args = ['python','H5_merge.py','arrTTTo2L2Nu2016APV.h5']
args.extend(arrTTTo2L2Nu2016APV)
subprocess.call(args)

#arrTTTo2L2Nu2018
args = ['python','H5_merge.py','arrTTTo2L2Nu2018.h5']
args.extend(arrTTTo2L2Nu2018)
subprocess.call(args)

#arrTTToHadronic2016
args = ['python','H5_merge.py','arrTTToHadronic2016.h5']
args.extend(arrTTToHadronic2016)
subprocess.call(args)

#arrTTToHadronic2016APV
args = ['python','H5_merge.py','arrTTToHadronic2016APV.h5']
args.extend(arrTTToHadronic2016APV)
subprocess.call(args)

#arrTTToHadronic2018
args = ['python','H5_merge.py','arrTTToHadronic2018.h5']
args.extend(arrTTToHadronic2018)
subprocess.call(args)

#arrTTToSemiLeptonic2016
args = ['python','H5_merge.py','arrTTToSemiLeptonic2016.h5']
args.extend(arrTTToSemiLeptonic2016)
subprocess.call(args)

#arrTTToSemiLeptonic2016APV
args = ['python','H5_merge.py','arrTTToSemiLeptonic2016APV.h5']
args.extend(arrTTToSemiLeptonic2016APV)
subprocess.call(args)

#arrTTToSemiLeptonic2018
args = ['python','H5_merge.py','arrTTToSemiLeptonic2018.h5']
args.extend(arrTTToSemiLeptonic2018)
subprocess.call(args)

#arrWJetsToQQ2016
args = ['python','H5_merge.py','arrWJetsToQQ2016.h5']
args.extend(arrWJetsToQQ2016)
subprocess.call(args)

#arrWJetsToQQ2016APV
args = ['python','H5_merge.py','arrWJetsToQQ2016APV.h5']
args.extend(arrWJetsToQQ2016APV)
subprocess.call(args)

#arrWJetsToQQ2018
args = ['python','H5_merge.py','arrWJetsToQQ2018.h5']
args.extend(arrWJetsToQQ2018)
subprocess.call(args)

#arrZJetsToQQ2016
args = ['python','H5_merge.py','arrZJetsToQQ2016.h5']
args.extend(arrZJetsToQQ2016)
subprocess.call(args)

#arrZJetsToQQ2016APV
args = ['python','H5_merge.py','arrZJetsToQQ2016APV.h5']
args.extend(arrZJetsToQQ2016APV)
subprocess.call(args)

#arrZJetsToQQ2018
args = ['python','H5_merge.py','arrZJetsToQQ2018.h5']
args.extend(arrZJetsToQQ2018)
subprocess.call(args)












