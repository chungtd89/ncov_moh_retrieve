# -*- coding: utf-8 -*-
from datetime import datetime
import time

# input mapping
raw_output = "data/raw/vnCovid19raw.csv"
dataframe_output = "data/vnCovid19data.csv"
covid_map = "map/map.html"

# today date
today = datetime.today().strftime("%d-%m-%Y")

# dataframe column
columns = ["Thời gian",
           "Trạng thái",
           "Số ca bệnh",
           "Thứ tự ca tử vong",
           "Thứ tự bệnh nhân",
           "Giới tính",
           "Tuổi",
           "Thông tin"]

# total time
start_time = time.time()
total_time = time.time() - start_time
display = "Process ended after %s seconds." % total_time

# params for normalize
uniChars = "àáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệđìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵÀÁẢÃẠÂẦẤẨẪẬĂẰẮẲẴẶÈÉẺẼẸÊỀẾỂỄỆĐÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴÂĂĐÔƠƯ"
unsignChars = "aaaaaaaaaaaaaaaaaeeeeeeeeeeediiiiiooooooooooooooooouuuuuuuuuuuyyyyyAAAAAAAAAAAAAAAAAEEEEEEEEEEEDIIIOOOOOOOOOOOOOOOOOOOUUUUUUUUUUUYYYYYAADOOU"




