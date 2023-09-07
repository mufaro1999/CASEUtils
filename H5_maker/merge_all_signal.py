import os, subprocess
from itertools import compress
processes = ['data'] #['MX2400_MY100','MX2400_MY250','MX2400_MY350','MX1600_MY150','MX2000_MY250','MX3000_MY190','MX3000_MY300','MX3000_MY400','MX2800_MY100','MX2800_MY190','MX2600_MY300']
for process in processes:
    #process = 'MX2400_MY100'
    years = ['2018']#,'2016APV','2017', '2018']
    #years = ['2017']
    args = ['python', 'H5_merge.py', '../jet_images/analysis_note_jets/merged_run2_{}_2018.h5'.format(process)]
    #args2 = ['python', 'H5_merge.py', '../jet_images/analysis_note_jets/merged_run2_{}_2017_b.h5'.format(process)]
    #args3 = ['python', 'H5_merge.py', '../jet_images/analysis_note_jets/merged_run2_{}_2017_c.h5'.format(process)]
    for year in years:
        path = '../jet_images/analysis_note_jets/{}/{}/'.format(year, process)
        files = os.listdir(path)
        
        size = len(files)

        files = [path + f for f in files]
        


        args.extend(files)
        #args2.extend(files[size/3:2*size/3])
       # args3.extend(files[86*size/100:size])

    print(args)
    #print(args2)
    subprocess.call(args)
   # subprocess.call(args2)
    #subprocess.call(args3)