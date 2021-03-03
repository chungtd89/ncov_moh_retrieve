# -*- coding: utf-8 -*-
import pandas as pd
import regex as re
import itertools
from ftfy import fix_encoding
import csv
from function.miscellaneous import columns
from function.normalize import convert_unicode

#def split_cases(row):


def joining(row):
    return convert_unicode(fix_encoding(','.join(row)))


def pattern(row):
    # tested regex, may not work properly
    pattern_date = r'^(?:0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]+ +\d{1,2}\/\d{1,2}\/\d{4}'
    pattern_case = r'(?:[(]BN+\d+[)])|(?:[(]BN+ \d+[)])|(?:(?:mã|mã số)+ \d+)'
    pattern_gender = "r'(?:nam|nữ|Nam|Nữ)'"
    pattern_age = r'(?i)\b(?=(?:, )(\d+ tuổi))\b'
    pattern_origin = ""
    pattern_potential = ""
    pattern_cur_location = ""
    pattern_confirmed = ""
    pattern_recovered = ""
    pattern_dead = ""
    return re.findall(pattern_date, row), re.findall(pattern_case, row), re.findall(pattern_age, row)


def create_data_frame():
    with open('data/vnCovid19data.csv', 'w+', encoding="utf-8", newline='') as writer_obj:
        writer_o = csv.writer(writer_obj)
        writer_o.writerow(columns)
        df = pd.read_csv("data/raw/vnCovid19raw.csv", header=None)
        for row in df.itertuples(index=False):
            row = list(row)
            row = joining(row)
            date, case, age = pattern(row)
            print(date)
            #for item in itertools.zip_longest(date, case, age):
                #writer_o.writerow(item)
