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

params = {'max': '50000', 'type': 'C', 'freq': 'A', 'px': 'HS', 'p': 'all', 'rg': 'all', 'cc': '270900',
          'uitoken': '87d1a4511735eb5547a25be51ff3a552', 'fmt': 'csv'}

country = [4, 8, 12, 20, 24, 28, 31, 32, 36, 40, 44, 48, 50, 51, 52, 56, 58, 60, 64, 68, 70, 72, 76, 84, 90, 92, 96, 97,
           100, 104, 108, 112, 116, 120, 124, 132, 136, 140, 144, 148, 152, 156, 170, 174, 175, 178, 180, 184, 188, 191,
           192, 196, 200, 203, 204, 208, 212, 214, 218, 222, 226, 230, 231, 232, 233, 234, 238, 242, 246, 251, 254, 258,
           262, 266, 268, 270, 275, 276, 278, 280, 288, 292, 296, 300, 304, 308, 312, 320, 324, 328, 332, 336, 340, 344,
           348, 352, 356, 360, 364, 368, 372, 376, 381, 384, 388, 392, 398, 400, 404, 408, 410, 414, 417, 418, 422, 426,
           428, 430, 434, 440, 442, 446, 450, 454, 457, 458, 459, 461, 462, 466, 470, 474, 478, 480, 484, 490, 496, 498,
           499, 500, 504, 508, 512, 516, 524, 528, 530, 531, 532, 533, 534, 535, 540, 548, 554, 558, 562, 566, 579, 580,
           582, 583, 584, 585, 586, 588, 590, 591, 592, 598, 600, 604, 608, 616, 620, 624, 626, 634, 638, 642, 643, 646,
           647, 654, 658, 659, 660, 662, 666, 670, 674, 678, 682, 686, 688, 690, 694, 699, 702, 703, 704, 705, 706, 710,
           711, 716, 717, 720, 724, 728, 729, 736, 740, 748, 752, 757, 760, 762, 764, 768, 772, 776, 780, 784, 788, 792,
           795, 796, 798, 800, 804, 807, 810, 818, 826, 834, 835, 836, 841, 842, 850, 854, 858, 860, 862, 866, 868, 876,
           882, 886, 887, 890, 891, 894]

for year in range(2000, 2019):
    params['ps'] = str(year)
    fl = '/root/UNcomtrade/' + str(year) + '/'
    folder = os.path.exists(fl)
    if not folder:
        os.makedirs(fl)
    for item in country:
        params['r'] = str(item)
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
