#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Copyright:    WZP
Filename:     unwrapByGAMMA.py
Description:

@author:      wuzhipeng
@email:       763008300@qq.com
@website:     https://wuzhipeng.cn/
@create on:   2/15/2021 3:51 PM
@software:    PyCharm
"""

import argparse
import os,sys
import tifffile
import glob
from concurrent.futures import ThreadPoolExecutor,wait
import numpy as np
import subprocess
import multiprocessing

parser = argparse.ArgumentParser(description='unwrapByGAMMA for InSARProcesser')
parser.add_argument('-i', '--inputdir', dest='inputdir',type=str, required=True ,help='interf dir of InSARProcesser')
parser.add_argument('-n', '--nparallel', dest='nparallel',type=int, default=None ,help='Number of parallel processing (Default: # of usable CPU)')
parser.add_argument('-pr', '--npat_r', dest='npat_r',type=str, default='-',help='number of patches in range (Default: - for automatic patching)')
parser.add_argument('-pa', '--npat_az', dest='npat_az',type=str, default='-',help='number of patches in azimuth (Default: - for automatic patching)')
parser.add_argument('-in', '--inName', dest='inName',type=str, default='dint_filter.tif',help='file name to be unwrapped (Default: dint_filter.tif)')
# parser.add_argument('-on', '--outName', dest='outName',type=str, default='unwrap_pha.tif',help='file name of unwrapped (Default: unwrap_pha.tif)')

args = parser.parse_args()
print(args.inputdir,flush=True)

if not args.nparallel:
    try:
        n_para = len(os.sched_getaffinity(0))
    except:
        n_para = multiprocessing.cpu_count()
else:
    n_para = args.nparallel

def unwrap(text, folder):
    print(text, flush = True)
    interf = tifffile.imread(os.path.join(folder,args.inName)).astype(np.complex64)
    interfTmp = os.path.join(folder,'dint_filter.wzpComplex')
    np.exp(1j * interf).tofile(interfTmp)

    coh = tifffile.imread(os.path.join(folder,'coh_multi.tif' if args.inName=='dint_filter.tif' else 'coh_geocode.tif'))
    cohTmp = os.path.join(folder, 'coh_multi.wzp')
    coh.tofile(cohTmp)

    unwrapTmp = os.path.join(folder, 'unwrap_pha.wzp')
    unwrapFile = os.path.join(folder, 'unwrap_pha.tif' if args.inName=='dint_filter.tif' else 'pha_geocode.tif')

    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
    rootPath = os.path.dirname(dirname)
    command = ' '.join([os.path.join(rootPath,'GammaMCF','mcf.exe'),interfTmp,cohTmp,'-',unwrapTmp,str(interf.shape[1]),'0 0 0 - -',args.npat_r,args.npat_az])

    process = subprocess.Popen(command)
    process.wait()
    unw = np.fromfile(unwrapTmp,dtype=np.float32).reshape(interf.shape)
    tifffile.imwrite(unwrapFile,unw)

    os.remove(interfTmp)
    os.remove(cohTmp)
    os.remove(unwrapTmp)


pool = ThreadPoolExecutor(n_para)
all_task = []
folders = glob.glob(args.inputdir+'/*/')
for idx, folder in enumerate(folders):
    text = '{}/{} {}'.format(idx+1,len(folders),folder)
    all_task.append(pool.submit(unwrap, text, folder))
    

wait(all_task)
print('Over!')