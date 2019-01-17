import os
import csv
import excontry

basefile = os.path.curdir
files = []

datafile = os.path.join(basefile, 'data')

for i in os.listdir(datafile):
    files.append(os.path.join(basefile, 'data', str(i)))

countrylst = excontry.getReporterCodeS()

for file in files:
    filesins = os.listdir(file)
    rows = []
    for filesin in filesins:
        filepath = os.path.join(file, filesin)
        with open(filepath) as f1:
            reader = csv.DictReader(f1)
            for row in reader:
                lst = [row['Reporter Code'], row['Partner Code'], row['Netweight (kg)']]
                if '' in lst:
                    continue
                if lst[1] not in countrylst:
                    continue
                if lst[0]==lst[1]:
                    continue
                rows.append(lst)
    # crows = rows[:]  # 创建副本
    for line1 in rows:
        if line1==[]:
            continue
        for line2 in rows:
            if line2==[]:
                continue
            if set([line1[0], line1[1]]) == set([line2[0], line2[1]]) and rows.index(line1) != rows.index(line2):
                rows[rows.index(line2)].clear()
    while [] in rows:
        rows.remove([])
    rows.sort(key=lambda x:(int(x[0]),int(x[1])))
    path = os.path.split(file)
    resultpath = 'crudeiglst/predate/' + path[1] + '.edgelist'
    with open(resultpath, 'w') as f2:
        for line in rows:
            f2.writelines(line[0] + ' ' + line[1] + ' {\'weight\':' + line[2] + '}\n')
