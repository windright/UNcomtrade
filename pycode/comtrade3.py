#!/usr/bin/env python3
import os
import time
import sys
from urllib.request import urlopen
from urllib.parse import urlencode
import re
from bs4 import BeautifulSoup as BS
import urllib
from urllib import error
import csv

print("downloading with urllib")

baseUrl = 'https://comtrade.un.org/api/get?'

params = {'max': '50000', 'type': 'C', 'freq': 'A', 'px': 'HS', 'r': 'all', 'rg': 'all', 'cc': '270900',
          'uitoken': '87d1a4511735eb5547a25be51ff3a552', 'fmt': 'csv'}

country = [4, 8, 10, 12, 16, 12, 24, 28, 32, 36, 152, 156, 162, 166,
           170, 174, 178, 180, 184, 188, 312, 316, 320, 324, 328,
           332, 334, 336, 340, 344, 462, 466, 70, 474, 478,
           480, 484, 488, 492, 496, 626, 630, 634, 638, 642,
           646, 654, 658, 662, 666, 796, 798, 800, 804, 810,
           818, 826, 834, 840, 849, 40, 44, 48, 50,
           52, 56, 60, 64, 68, 72, 196, 200, 201, 204, 208,
           212, 214, 216, 218, 352, 356, 360, 364, 368, 372,
           374, 376, 380, 504, 508, 512, 516, 520, 524, 528,
           532, 536, 674, 678, 682, 686, 690, 694, 702, 704, 706,
           854, 858, 862, 872, 876, 882, 886, 890, 894, 74,
           76, 84, 86, 90, 92, 96, 100, 104, 108, 222, 226,
           230, 234, 238, 242, 246, 250, 254, 258, 384, 388, 392,
           396, 400, 404, 408, 410, 414, 418, 540, 548, 554, 558,
           562, 566, 570, 574, 578, 582, 710, 716, 720, 724, 732,
           736, 740, 744, 748, 752, 112, 116, 120, 124, 128, 132,
           136, 140, 144, 148, 262, 266, 270, 280, 288, 292, 296, 300,
           304, 308, 422, 426, 430, 434, 438, 442, 446, 450, 454, 458, 586,
           590, 598, 600, 604, 608, 612, 616, 620, 624, 756, 760, 764,
           768, 772, 776, 780, 784, 788, 792, 31, 191, 203, 231, 233, 251, 268, 275, 381, 398, 428, 440, 490, 498, 499,
           579, 583, 585, 643, 670, 688, 699, 703, 705, 729, 757, 807, 842, 887]

for year in range(2015, 2016):
    params['ps'] = str(year)
    fl = '/root/UNcomtrade/' + str(year) + '/'
    folder = os.path.exists(fl)
    if not folder:
        os.makedirs(fl)
    for item in country:
        if year == 2015 and country.index(item) < country.index(842):
            continue
        params['p'] = str(item)
        file = str(year) + '_' + str(item) + ".csv"
        print("downloading with " + file)

        LocalPath = os.path.join(fl, file)
        # os.path.join将多个路径组合后返回
        while True:
            try:
                urllib.request.urlretrieve((baseUrl + urlencode(params)), LocalPath)
            except Exception as e:
                print(e)
                print('Error occured...reset...')
                sys.stdout.flush()
                time.sleep(3)
            else:
                break
        sys.stdout.flush()
        time.sleep(37)
