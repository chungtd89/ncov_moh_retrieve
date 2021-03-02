# -*- coding: utf-8 -*-
import pandas as pd
from csv import reader
from csv import writer
import regex as re
import itertools as it
from ftfy import fix_encoding
import csv
from function.miscellaneous import columns
from function.normalize import covert_unicode


def joining(row):
    return covert_unicode(fix_encoding(','.join(row)))


def pattern(row):
    # tested regex, may not work properly
    pattern_date = r'^(?:0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]+ +\d{1,2}\/\d{1,2}\/\d{4}'
    pattern_case = r'(?:[(]BN+\d+[)])|(?:[(]BN+ \d+[)])|(?:(?:mã|mã số)+ \d+)'
    pattern_gender = r'(?:nam|nữ|Nam|Nữ)'
    pattern_age = r'(?i)\b(?=(?:, )(\d+ tuổi))\b'
    pattern_origin = ""
    pattern_potential = ""
    pattern_cur_location = ""
    pattern_confirmed = ""
    pattern_recovered = ""
    pattern_dead = ""
    return re.findall(pattern_date, row), re.findall(pattern_case, row), re.findall(pattern_age, row)


def create_data_frame():
    with open('data/vnCovid19data.csv', 'w', encoding="utf-8", newline='') as writer_obj:
        writer_o = csv.writer(writer_obj)
        writer_o.writerow(columns)
        with open('data/raw/vnCovid19raw', 'r', encoding="utf-8") as reader_obj:
            reader_o = csv.reader(reader_obj)
            for row in reader_o:
                row = joining(row)
            """
            Create dataframe from matched list
            """
