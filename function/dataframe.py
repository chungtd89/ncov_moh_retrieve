# -*- coding: utf-8 -*-
import pandas as pd
import regex as re
import itertools
from ftfy import fix_encoding
import csv
from function.miscellaneous import columns
from function.normalize import convert_unicode


def split_cases(row):
    example_1 = "(BN2422-2426)"
    case = row.replace("(", "").replace(")", "").replace("BN", "").split("-")
    extracted = ["BN_" + str(x) for x in range(int(case[0]), int(case[1]))]
    return extracted


def duplicate(file_name):
    example = ""


def split_paragraph(row):
    pattern_paragraph = ""


def return_joined(row):
    return convert_unicode(fix_encoding(','.join(list(row))))


def pattern(row):
    # tested regex, may not work properly
    pattern_date = r'^(?:0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]+ +\d{1,2}\/\d{1,2}\/\d{4}'
    pattern_case = ""
    pattern_gender = r'nữ|nữ|Nữ|: Nam|nam|Nữ'
    pattern_age = r'\d+ (?:tuổi|tuổi)'
    pattern_origin = ""
    pattern_potential = ""
    pattern_cur_location = ""
    pattern_confirmed = ""
    pattern_recovered = ""
    pattern_dead = ""

    date = [re.sub(r'^(?:0[0-9]|1[0-9]|2[0-3]):[0-5][0-9] ', "", x) for x in re.findall(pattern_date, row)]
    case = ""
    gender = [x.replace(": ", "").lower() or x.replace(" ", "").lower() or x.lower()
              if ": " in x or " " in x else x for x in re.findall(pattern_gender, row)]
    age = [x.replace(" tuổi", "") or x.replace(" tuổi", "")
           if " tuổi" in x or " tuổi" in x else x for x in re.findall(pattern_age, row)]
    return date, gender, age


def create_data_frame():
    with open('data/vnCovid19data.csv', 'w+', encoding="utf-8", newline='') as write_obj:
        writer_o = csv.writer(write_obj)
        writer_o.writerow(columns)
        df = pd.read_csv("data/raw/vnCovid19raw.csv", header=None)
        for row in df.itertuples(index=False):
            row = return_joined(row)
            #print(row)
            date, gender, age = pattern(row)
            for d, g, a in itertools.zip_longest(date, gender, age):
                writer_o.writerow([d,"", g, a])



print(split_cases("(BN2422-2426)"))
