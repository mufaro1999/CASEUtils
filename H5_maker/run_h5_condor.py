import subprocess
import glob
import os
from collections import OrderedDict
import sys

if __name__=='__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-i', type=str, dest='iFile',
                        action='store', required=True,
                        help='input ROOT file')
    parser.add_argument('-o', type=str, dest='oFile',
                        action='store', required=True,
                        help='output H5 file')
    parser.add_argument('-y', type=str, dest='year',
                        action='store', required=True,
                        help='2016, 2016APV, 2017, 2018')
    parser.add_argument('-f', type=str, dest='f',
			action='store', required=True,
			help='sets the truth label of the output. Usually signal is 1, QCD is 0, single top -1, ttbar -2, V+jets -3')

    args = parser.parse_args()
    subprocess.call('python make_h5_local.py -i {} -o {} -y {} -f {}'.format(args.iFile, args.oFile, args.year, args.f),shell=True)
