#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Copyright:    WZP
Filename:     getMaskFile.py
Description:

@author:      wuzhipeng
@email:       763008300@qq.com
@website:     https://wuzhipeng.cn/
@create on:   2/24/2021 4:15 PM
@software:    PyCharm
"""
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.widgets import RectangleSelector
import argparse
import matplotlib.pyplot as plt
import matplotlib.patches as mpathes
import glob
import os
import numpy as np

parser = argparse.ArgumentParser(description='Get a text file of a list of ranges to be masked (format is x1:x2/y1:y2)')
parser.add_argument('-i', '--inputdir', dest='inputdir',type=str, default='GEOCml1' ,help='inputdir (default: GEOCml1)')
parser.add_argument('-o', '--outputfile', dest='outputfile',type=str, default='masklist.txt' ,help='output file (default: masklist.txt)')
args = parser.parse_args()

global x1, y1, x2, y2, current_ax,flag


def line_select_callback(eclick, erelease):
    'eclick and erelease are the press and release events'
    global x1, y1, x2, y2,flag
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    if x1>x2:
        x1,x2=x2,x1
    if y1>y2:
        y1,y2=y2,y1
    print("(%3.2f, %3.2f) --> (%3.2f, %3.2f)" % (x1, y1, x2, y2))
    print(" The button you used were: %s %s" % (eclick.button, erelease.button))
    flag = 1


def toggle_selector(event):
    global x1, y1, x2, y2,current_ax,flag
    # print(' Key pressed.')
    if event.key in ['enter', 'v'] and toggle_selector.RS.active and flag:
        print(' Key pressed.')

        # polygon = mpathes.Rectangle((x1,y1), x2-x1, y2-y1, color='r', alpha=0.3)
        # current_ax.add_patch(polygon)

        toggle_selector.RS.set_active(False)
        toggle_selector.RS.set_active(True)

        with open(args.outputfile,'a+') as f:
            f.write('{}:{}/{}:{}\n'.format(round(x1),round(x2),round(y1),round(y2)))
            flag=0

        print("(%3.2f, %3.2f) --> (%3.2f, %3.2f)" % (x1, y1, x2, y2))


    # if event.key in ['Enter', 'enter'] and toggle_selector.RS.active:
    #     print(' RectangleSelector deactivated.')
    #     toggle_selector.RS.set_active(False)
    # if event.key in ['A', 'a'] and not toggle_selector.RS.active:
    #     print(' RectangleSelector activated.')
    #     toggle_selector.RS.set_active(True)


fig, current_ax = plt.subplots()                 # make a new plotting range
flag = 0
# unwFile = glob.glob(args.inputdir+'/*/*.unw')[0]
unwFile = glob.glob(args.inputdir+'/*/*.cc')[0]
try:
    parFile = glob.glob(args.inputdir + '/slc.mli.par')[0]
    with open(parFile, 'r') as f:
        info = f.read()
    length = eval(info.split('azimuth_lines:')[1].strip().split()[0])
    width = eval(info.split('range_samples:')[1].strip().split()[0])
except:
    print('  "info.txt" cannot find in {}. Please check'.format(args.inputdir), flush=True)
    exit()

unw = np.fromfile(unwFile, dtype=np.float32 if unwFile.endswith('unw') else np.uint8).reshape(length, width).astype(np.float32)
unw[unw==0] = np.nan
plt.imshow(unw)

print("\n      click  -->  release")
if os.path.exists(args.outputfile):
    os.remove(args.outputfile)

# drawtype is 'box' or 'line' or 'none'
toggle_selector.RS = RectangleSelector(current_ax, line_select_callback,
                                       drawtype='box', useblit=True,
                                       button=[1, 3],  # don't use middle button
                                       minspanx=5, minspany=5,
                                       spancoords='pixels',
                                       interactive=True)
plt.connect('key_press_event', toggle_selector)
plt.jet()
plt.show()