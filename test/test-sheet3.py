import regex as re
import itertools as iter
import sys
import csv
from csv import reader
import pandas as pd
from functools import reduce
import numpy as np
import VietnameseTextNormalizer

uniChars = "àáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệđìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵÀÁẢÃẠÂẦẤẨẪẬĂẰẮẲẴẶÈÉẺẼẸÊỀẾỂỄỆĐÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴÂĂĐÔƠƯ"
unsignChars = "aaaaaaaaaaaaaaaaaeeeeeeeeeeediiiiiooooooooooooooooouuuuuuuuuuuyyyyyAAAAAAAAAAAAAAAAAEEEEEEEEEEEDIIIOOOOOOOOOOOOOOOOOOOUUUUUUUUUUUYYYYYAADOOU"

def loaddicchar():
    dic = {}
    char1252 = 'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ'.split('|')
    charutf8 = "à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ".split('|')
    for i in range(len(char1252)):
        dic[char1252[i]] = charutf8[i]
    return dic

dicchar = loaddicchar()

def covert_unicode(txt):
    return re.sub(r'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ',lambda x: dicchar[x.group()], txt)

def my_function(x):
  return list(dict.fromkeys(x))
l=[]
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
l7=[]
df = pd.read_csv("vnCovid19Summary.csv", header=None)
for row in df.itertuples(index=False):
    i = list(row)
    x2 = ','.join(i)
    x3 = covert_unicode(x2)
    x1 = VietnameseTextNormalizer.Normalize(x3)
    order = re.findall(r'(?:(?:CA MẮC MỚI )[(]BN+\d+[)])|(?:(?:CA MẮC MỚI [(]BN+ \d+[)]))|(?:(?:CA BỆNH )+\d+ [(]BN+\d+[)])|(?:(?:mã|mã số)+ \d+)|(?:[(]BN+ \d+[)])|(?:(?:Bệnh nhân |Bệnh nhân thứ )+\d+ [(]BN+ \d+[)])|(?:(?:Bệnh nhân |Bệnh nhân thứ )+\d+ [(]BN+\d+[)])|(?:\bBN+\d+\b)|(?:\bBN+ \d+\b)',x1)
    order = ' '.join(order).replace('BN', '').replace('mã số', '').replace('CA MẮC MỚI','').replace('CA BỆNH','').replace('Bệnh nhân','').replace('(','').replace(')','').replace('Bệnh nhân thứ','').replace('thứ','').split()
    order = my_function(order)
    totp = re.findall(r'^(?:0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]+ +\d{1,2}\/\d{1,2}\/\d{4}', x1)
    confirmed = re.findall(r'(?:CA MẮC MỚI|DƯƠNG TÍNH|CA MẮC|CA BỆNH)', x1)
    confirmed = ' '.join(confirmed).replace('CA MẮC MỚI', '1').replace('DƯƠNG TÍNH','1').replace('CA MẮC','1').replace('CA BỆNH','1').split()
    recovery = re.findall(r'(?:KHỎI BỆNH|CHỮA KHỎI|công bố khỏi bệnh|rút trường hợp)',x1)
    recovery = ' '.join(recovery).replace('KHỎI BỆNH', '1').replace('CHỮA KHỎI','1').replace('rút trường hợp','1').replace('công bố khỏi bệnh','1').split()
    dead = re.findall(r'(?:TỬ VONG)',x1)
    dead = ' '.join(dead).replace('TỬ VONG','1').split()
    gender = re.findall(r'(?:Nam|Nữ|na nuwx)', x1)
    gender = ' '.join(gender).replace('nam','Male').replace('nữ','Female').replace('Nam','Male').replace('Nữ','Female').split()
    age = re.findall(r'(?i)\b(?=(?:, )(\d+ tuổi))\b', x1)
    age = ' '.join(age).replace('tuổi', '').split()
    age = my_function(age)
    l.append(totp)
    l1.append(order)
    l2.append(confirmed)
    l3.append(recovery)
    l4.append(dead)
    l5.append(gender)
    l6.append(age)
df = pd.DataFrame(zip(l,l1,l5,l2,l3,l4),columns=['Time','Case','Gender','Confirmed','Recovery','Dead'])
r = df.explode('Time').explode('Case').explode('Gender').explode('Confirmed').explode('Recovery').explode('Dead').reset_index(drop=True)
r1 = r.drop_duplicates()
r1.to_csv('file1.csv',index=None)
