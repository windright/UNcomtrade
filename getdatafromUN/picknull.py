import os
import csv
import re
import excontry

basefile=os.path.curdir
files=[]

datafile=os.path.join(basefile,'data')

for i in os.listdir(datafile):
    files.append(os.path.join(basefile,'data',str(i)))

dic=excontry.getAlldic()

with open('null.txt','w') as f:
    f.write('year\tcode\tcountry\tfile\n')


for file in files:
    fileins=os.listdir(file)
    for filein in fileins:
        filepath=os.path.join(file,filein)
        with open(filepath) as f:
            reader = csv.reader(f)
            for row in reader:
                if 'No data matches' in row[0]:
                    with open('null.txt','a') as f1:
                        splistr=re.split('[._]',filein)
                        try:
                            coutrystr=dic[splistr[1]]
                        except:
                            coutrystr='null'
                        lst=[splistr[0],'\t',splistr[1],'\t',coutrystr,'\n']
                        f1.writelines(lst)
