import subprocess
import glob
import os
from collections import OrderedDict
import sys

redirector = 'root://cmsxrootd.fnal.gov/'
eosls = 'eos root://cmseos.fnal.gov ls'

datasets = {
    "2016": {
        "QCD_HT1000to1500": "/store/group/lpcpfnano/cmantill/v2_3/2016/QCD/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT1000to1500/220808_181242/0000/",
        "QCD_HT100to200": "/store/group/lpcpfnano/cmantill/v2_3/2016/QCD/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT100to200/220808_181126/0000/",
        "QCD_HT1500to2000": "/store/group/lpcpfnano/cmantill/v2_3/2016/QCD/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT1500to2000/220808_181307/0000/",
        "QCD_HT2000toInf": "/store/group/lpcpfnano/cmantill/v2_3/2016/QCD/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT2000toInf/220808_181358/0000/",
        "QCD_HT200to300": "/store/group/lpcpfnano/cmantill/v2_3/2016/QCD/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT200to300/220808_181332/0000/",
        "QCD_HT300to500": "/store/group/lpcpfnano/cmantill/v2_3/2016/QCD/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT300to500/220808_181423/0000/",
        "QCD_HT500to700": "/store/group/lpcpfnano/cmantill/v2_3/2016/QCD/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT500to700/220808_181100/0000/",
        "QCD_HT50to100": "/store/group/lpcpfnano/cmantill/v2_3/2016/QCD/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT50to100/220808_181151/0000/",
        "QCD_HT700to1000": "/store/group/lpcpfnano/cmantill/v2_3/2016/QCD/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT700to1000/220808_181216/0000/",
        "TTTo2L2Nu": "/store/group/lpcpfnano/cmantill/v2_3/2016/TTbar/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/TTTo2L2Nu/220808_181933/0000/",
        "TTToHadronic": "/store/group/lpcpfnano/cmantill/v2_3/2016/TTbar/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/TTToHadronic/220808_181812/0000/",
        "TTToSemiLeptonic": "/store/group/lpcpfnano/cmantill/v2_3/2016/TTbar/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/TTToSemiLeptonic/220808_181840/0000/",
        "WJetsToQQ_HT-400to600": "/store/group/lpcpfnano/cmantill/v2_3/2016/WJetsToQQ/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/WJetsToQQ_HT-400to600/220808_182049/0000/",
        "WJetsToQQ_HT-600to800": "/store/group/lpcpfnano/cmantill/v2_3/2016/WJetsToQQ/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/WJetsToQQ_HT-600to800/220808_181958/0000/",
        "WJetsToQQ_HT-800toInf": "/store/group/lpcpfnano/cmantill/v2_3/2016/WJetsToQQ/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/WJetsToQQ_HT-800toInf/220808_182024/0000/",
        "ZJetsToQQ_HT-400to600": "/store/group/lpcpfnano/cmantill/v2_3/2016/ZJetsToQQ/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/ZJetsToQQ_HT-400to600/220808_182140/0000/",
        "ZJetsToQQ_HT-600to800": "/store/group/lpcpfnano/cmantill/v2_3/2016/ZJetsToQQ/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/ZJetsToQQ_HT-600to800/220808_182229/0000/",
        "ZJetsToQQ_HT-800toInf": "/store/group/lpcpfnano/cmantill/v2_3/2016/ZJetsToQQ/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/ZJetsToQQ_HT-800toInf/220808_182204/0000/"
    },
    "2016APV": {
        "QCD_HT1000to1500": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/QCD/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT1000to1500/220808_173028/0000/",
        "QCD_HT100to200": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/QCD/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT100to200/220808_172911/0000/",
        "QCD_HT1500to2000": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/QCD/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT1500to2000/220808_173053/0000/",
        "QCD_HT2000toInf": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/QCD/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT2000toInf/220808_173144/0000/",
        "QCD_HT200to300": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/QCD/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT200to300/220808_173118/0000/",
        "QCD_HT300to500": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/QCD/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT300to500/220808_173210/0000/",
        "QCD_HT500to700": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/QCD/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT500to700/220808_172844/0000/",
        "QCD_HT50to100": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/QCD/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT50to100/220808_172936/0000/",
        "QCD_HT700to1000": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/QCD/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT700to1000/220808_173001/0000/",
        "TTTo2L2Nu": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/TTbar/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/TTTo2L2Nu/220808_173718/0000/",
        "TTToHadronic": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/TTbar/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/TTToHadronic/220808_173601/0000/",
        "TTToSemiLeptonic": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/TTbar/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/TTToSemiLeptonic/220808_173625/0000/",
        "WJetsToQQ_HT-400to600": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/WJetsToQQ/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/WJetsToQQ_HT-400to600/220808_173834/0000/",
        "WJetsToQQ_HT-600to800": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/WJetsToQQ/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/WJetsToQQ_HT-600to800/220808_173742/0000/",
        "WJetsToQQ_HT-800toInf": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/WJetsToQQ/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/WJetsToQQ_HT-800toInf/220808_173810/0000/",
        "ZJetsToQQ_HT-200to400": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/ZJetsToQQ/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/ZJetsToQQ_HT-200to400/220808_173859/0000/",
        "ZJetsToQQ_HT-400to600": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/ZJetsToQQ/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/ZJetsToQQ_HT-400to600/220808_173950/0000/",
        "ZJetsToQQ_HT-600to800": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/ZJetsToQQ/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/ZJetsToQQ_HT-600to800/220808_174015/0000/",
        "ZJetsToQQ_HT-800toInf": "/store/group/lpcpfnano/cmantill/v2_3/2016APV/ZJetsToQQ/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/ZJetsToQQ_HT-800toInf/220808_173925/0000/"
    },
    "2017": {
        "QCD_HT1000to1500": "/store/group/lpcpfnano/cmantill/v2_3/2017/QCD/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT1000to1500/220808_164439/0000/",
        "QCD_HT100to200": "/store/group/lpcpfnano/cmantill/v2_3/2017/QCD/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT100to200/220808_164315/0000/",
        "QCD_HT1500to2000": "/store/group/lpcpfnano/cmantill/v2_3/2017/QCD/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT1500to2000/220808_164504/0000/",
        "QCD_HT2000toInf": "/store/group/lpcpfnano/cmantill/v2_3/2017/QCD/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT2000toInf/220808_164556/0000/",
        "QCD_HT200to300": "/store/group/lpcpfnano/cmantill/v2_3/2017/QCD/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT200to300/220808_164529/0000/",
        "QCD_HT300to500": "/store/group/lpcpfnano/cmantill/v2_3/2017/QCD/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT300to500/220808_164621/0000/",
        "QCD_HT500to700": "/store/group/lpcpfnano/cmantill/v2_3/2017/QCD/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT500to700/220808_164248/0000/",
        "QCD_HT50to100": "/store/group/lpcpfnano/cmantill/v2_3/2017/QCD/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT50to100/220808_164341/0000/",
        "QCD_HT700to1000": "/store/group/lpcpfnano/cmantill/v2_3/2017/QCD/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT700to1000/220808_164413/0000"
    },
    "2018": {
        'QCD_HT1000to1500':'/store/group/lpcpfnano/cmantill/v2_3/2018/QCD/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT1000to1500_PSWeights_madgraph/220808_163033/0000/',
        'QCD_HT100to200':'/store/group/lpcpfnano/cmantill/v2_3/2018/QCD/QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8/QCD_HT100to200/220808_150427/0000/',
        'QCD_HT100to200':'/store/group/lpcpfnano/cmantill/v2_3/2018/QCD/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT100to200_PSWeights_madgraph/220808_162853/0000/',
        'QCD_HT1500to2000':'/store/group/lpcpfnano/cmantill/v2_3/2018/QCD/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT1500to2000_PSWeights_madgraph/220808_163124/0000/',
        'QCD_HT2000toInf':'/store/group/lpcpfnano/cmantill/v2_3/2018/QCD/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT2000toInf_PSWeights_madgraph/220808_163214/0000/',
        'QCD_HT200to300':'/store/group/lpcpfnano/cmantill/v2_3/2018/QCD/QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8/QCD_HT200to300/220808_150637/0000/',
        'QCD_HT300to500':'/store/group/lpcpfnano/cmantill/v2_3/2018/QCD/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT300to500_PSWeights_madgraph/220808_163009/0000/',
        'QCD_HT500to700':'/store/group/lpcpfnano/cmantill/v2_3/2018/QCD/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT500to700_PSWeights_madgraph/220808_162943/0000/',
        'QCD_HT50to100':'/store/group/lpcpfnano/cmantill/v2_3/2018/QCD/QCD_HT50to100_TuneCP5_13TeV-madgraphMLM-pythia8/QCD_HT50to100/220808_150453/0000/',
        'QCD_HT700to1000':'/store/group/lpcpfnano/cmantill/v2_3/2018/QCD/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/QCD_HT700to1000_PSWeights_madgraph/220808_162918/0000/',
        'TTJets':'/store/group/lpcpfnano/cmantill/v2_3/2018/TTbar/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/TTJets/220808_151219/0000/',
        'TTTo2L2Nu':'/store/group/lpcpfnano/cmantill/v2_3/2018/TTbar/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/TTTo2L2Nu/220808_151337/0000/',
        'TTToHadronic':'/store/group/lpcpfnano/cmantill/v2_3/2018/TTbar/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/TTToHadronic/220808_151154/0000/',
        'TTToSemiLeptonic':'/store/group/lpcpfnano/cmantill/v2_3/2018/TTbar/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/TTToSemiLeptonic/220808_151244/0000/',
        'WJetsToQQ_HT-400to600':'/store/group/lpcpfnano/cmantill/v2_3/2018/WJetsToQQ/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/WJetsToQQ_HT-400to600/220808_151501/0000/',
        'WJetsToQQ_HT-600to800':'/store/group/lpcpfnano/cmantill/v2_3/2018/WJetsToQQ/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/WJetsToQQ_HT-600to800/220808_151403/0000/',
        'WJetsToQQ_HT-800toInf':'/store/group/lpcpfnano/cmantill/v2_3/2018/WJetsToQQ/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/WJetsToQQ_HT-800toInf/220808_151432/0000/',
        'ZJetsToQQ_HT-600to800':'/store/group/lpcpfnano/cmantill/v2_3/2018/ZJetsToQQ/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/ZJetsToQQ_HT-600to800/220808_151653/0000/',
        'ZJetsToQQ_HT-800toInf':'/store/group/lpcpfnano/cmantill/v2_3/2018/ZJetsToQQ/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/ZJetsToQQ_HT-800toInf/220808_151628/0000/'
    }
}


if __name__=='__main__':
    # loop over dataset dictionary
    for year, dataset in datasets.items():
	# create arg file
	argFile = open('h5_arg_{}.txt'.format(year),'w')
	for process, path in dataset.items():
	    # determine H5_maker arguments
            if ('WJets' in process) or ('ZJets' in process):
                f = -3
            elif ('TT' in process):
                f = -2
            elif ('QCD' in process):
                f = 0
	    # get the file names
	    fNames = subprocess.check_output(['{} {}'.format(eosls,path)],shell=True).split('\n')
	    fNames.remove('')
	    #fNames.remove('log')
	    for fName in fNames:
	        # create arguments
	        iFile = '{}{}{}'.format(redirector, path, fName)
	        oFile = '{}_{}_{}.h5'.format(process.replace('_','-'), fName.split('.')[0].replace('_','-'), year)
	        iYear = 2016 if 'APV' in year else year
	        # write to file
	        argFile.write(' -i {} -o {} -y {} -f {}\n'.format(iFile, oFile, iYear, f))
	# close file
	argFile.close()
