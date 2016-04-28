# -*- coding:cp936 -*-

import os
import shutil

inws = r'D:\maplet_dvk\MapPicDir\raw\�й���ʷ��ͼ��_̷_8��_dd006dd\�й���ʷ��ͼ��_��ƴ��\��3��\08����'


wfiles = os.listdir(inws)
for wfile in wfiles:
    infile = os.path.join(inws, wfile)
    if os.path.isfile(infile):
        pass
    else:
        continue
    sig_arr = wfile.split('_')
    outws = os.path.join(inws, sig_arr[0])
    if os.path.exists(outws):
        pass
    else:
        os.mkdir(outws)

    outfile = os.path.join(outws, wfile)

    shutil.move(infile, outfile)
