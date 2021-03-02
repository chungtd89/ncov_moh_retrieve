import regex as re
import itertools as iter
import sys
import csv
from csv import reader

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

def convert_unicode(txt):
    return re.sub(r'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ',lambda x: dicchar[x.group()], txt)

def newfile():
    with open('testfor1.csv',encoding="utf-8") as read_obj1:
        csv_reader = csv.reader(read_obj1)
        with open('input1.csv', 'w', encoding="utf-8") as write_obj:
            writer = csv.writer(write_obj)
            for row in csv_reader:
                joinrow = [' '.join([row[0], row[1]])] + row[2:]
                writer.writerow(joinrow)
        write_obj.close();

if __name__ == '__main__':
    newfile()

list1 =[]
with open('input1.csv', encoding="utf-8", newline='') as read_obj2 :
        csv_reader1 = reader(read_obj2)
        for row1 in csv_reader1:
            str_list = list(filter(None, row1))
            for row2 in str_list:
                row3 = convert_unicode(row2)
                totp = re.findall(r'^(?:0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]+ +\d{1,2}\/\d{1,2}\/\d{4}',row3)
                condition = re.findall(r'(?:MẮC MỚI|TỬ VONG|KHỎI BỆNH|CHỮA KHỎI|DƯƠNG TÍNH)',row3)
                status = re.findall(r'\b\d+ (?=CA BỆNH|CA MẮC|NGƯỜI|TRƯỜNG HỢP|BỆNH NHÂN|CA DƯƠNG TÍNH)',row3)
                condition1 = re.findall(r'(?=(?:THỨ) +(\d+))\b',row3)
                order = re.findall(r'(?:[(]BN+\d+[)])|(?:[(]BN+ \d+[)])|(?:(?:mã|mã số)+ \d+)',row3)
                sex = re.findall(r'(?:nam|nữ|Nam|Nữ)', row3)
                age = re.findall(r'(?i)\b(?=(?:, )(\d+ tuổi))\b',row3)
                info = re.findall(r'(?i)\b(?:địa chỉ tại|địa chỉ|quốc tịch|ở|quê quán|ngụ tại|địa chỉ ở|tiền sử:|tại|điều trị tại|bệnh nhân khoa)+[ ,:a-zàáãảạâấầẫậăắằẵặơờớởỡợđêếềễểệôốồỗổộùúụủũưừữứửựíìĩỉịỹỷỳýỵ]+[.]',row3)
                la, lb, lc, ld, le, lf, lh = len(totp), len(condition), len(status), len(condition1), len(order), len(sex), len(age)
                max_len = max(la, lb, lc, ld, le, lf, lh)
                if not max_len == la:
                    totp.extend([''] * (max_len - la))
                if not max_len == lb:
                    condition.extend([''] * (max_len - lb))
                if not max_len == lc:
                    status.extend([''] * (max_len - lc))
                if not max_len == ld:
                    condition1.extend([''] * (max_len - ld))
                if not max_len == le:
                    order.extend([''] * (max_len - le))
                if not max_len == lf:
                    sex.extend([''] * (max_len - lf))
                if not max_len == lh:
                    age.extend([''] * (max_len - lh))
                for item in iter.zip_longest(totp, condition, status, condition1, order, sex, age):
                    with open('testfor.csv', 'w+', encoding="utf-8", newline='') as write_obj1:
                        writer1 = csv.writer(write_obj1)
                        writer1.writerow(item)



