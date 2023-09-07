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

    args = parser.parse_args()
    subprocess.call('python make_jet_images.py -i {} -o {}'.format(args.iFile, args.oFile),shell=True)
