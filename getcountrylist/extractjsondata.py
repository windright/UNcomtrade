import json
import collections

def saveReporter(): #reporter为国家
    with open('reporterAreas.json','r') as f:
        data1=json.load(f)

    with open('reporter.txt','w') as f:
        for each in data1['results']:
            f.write(each['id'])
            f.write(': ')
            f.write(each['text'])
            f.write('\n')

def savePartner():  #partner包括国家地区，如Western Asia, nes
    with open('partnerAreas.json','r') as f:
        data2=json.load(f)

    with open('partner.txt','w') as f:
        for each in data2['results']:
            f.write(each['id'])
            f.write(': ')
            f.write(each['text'])
            f.write('\n')

def getReporterdic():
    with open('reporterAreas.json','r') as f:
        data1=json.load(f)
    predic=data1['results']
    dic={}
    for each in predic:
        dic[each['id']]=each['text']
    return dic

def getOrderReporterdic():
    with open('reporterAreas.json','r') as f:
        data1=json.load(f)
    predic=data1['results']
    dic={}
    for each in predic:
        dic[each['id']]=each['text']
    del dic['all']
    dic=collections.OrderedDict(sorted(dic.items(), key=lambda t: int(t[0])))
    return dic

def getReporterCode():
    dic=getReporterdic()
    lst=[]
    for key in dic.keys():
        if key=='all':
            continue
        lst.append(int(key))
    lst.sort()
    return lst

def getReporterCodeS():
    dic=getReporterdic()
    lst=[]
    for key in dic.keys():
        lst.append(key)
    lst.remove('all')
    return lst

lst=getReporterCodeS()
print(lst)