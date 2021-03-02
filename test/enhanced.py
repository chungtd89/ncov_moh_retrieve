import regex as re
import itertools as iter
import sys
import csv
from csv import reader

"""
print("Nhap du lieu: \n")
input = sys.stdin.read()
input1 = str.splitlines()
"""
"""
order = ["1","2","3"]
gender = ["nam","nữ","nam","nữ","nam"]
age = ["99","101"]
for treble in iter.zip_longest(order, gender, age):
    print(treble)

"""
with open('testfor.csv', 'w+', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Thời gian", "Trạng thái", "Số ca bệnh","Thứ tự ca tử vong", "Thứ tự bệnh nhân", "Giới tính", "Tuổi","Thông tin"])
    with open('input.csv', 'r', encoding="utf-8") as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
                r = ','.join(row)
                totp = re.findall(r'^(?:0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]+ +\d{1,2}\/\d{1,2}\/\d{4}',r) #thời gian đăng tin
                condition = re.findall(r'(?:MẮC MỚI|TỬ VONG|KHỎI BỆNH|CHỮA KHỎI|DƯƠNG TÍNH)',r) #Tình trạng
                #z = list(map(lambda x: x.lower(),re.findall(r'\b\d+ (?=CA BỆNH|CA MẮC|NGƯỜI|TRƯỜNG HỢP|BỆNH NHÂN|CA DƯƠNG TÍNH)',r)))
                status = re.findall(r'\b\d+ (?=CA BỆNH|CA MẮC|NGƯỜI|TRƯỜNG HỢP|BỆNH NHÂN|CA DƯƠNG TÍNH)',r)
                condition1 = re.findall(r'(?=(?:THỨ) +(\d+))\b',r)
                order = re.findall(r'(?=(?=(?:\(BN)+(\d+)\))|(?=(?:\(BN) +(\d+)\)))',r) #số thứ tự bệnh nhân
                order1 = re.findall(r'(?=(?:\(BN) +(\d+)\))',r)
                sex = re.findall(r'(?:nam|nữ)', r)  # giới tính
                age = re.findall(r'(?i)\b(?=(?:, )(\d+ tuổi))\b',r) #tuổi
                info = re.findall(r'(?i)\b(?:địa chỉ tại|địa chỉ|quốc tịch|ở|quê quán|ngụ tại|địa chỉ ở|tiền sử:|tại)+[ ,:a-zàáãảạâấầẫậăắằẵặơờớởỡợđêếềễểệôốồỗổộùúụủũưừữứửựíìĩỉịỹỷỳýỵ]+[.]',r) #thông tin
                print(order)
                for treble in iter.zip_longest(totp, condition, status, condition1, order, sex, age):#, info):
                    with open('testfor.csv', 'w+', encoding="utf-8", newline='') as file:
                        writer.writerow(treble)