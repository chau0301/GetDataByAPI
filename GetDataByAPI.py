import requests
import json

def gender(text):
    return 0 if text == "Nam" else 1

def RA(txt):
    string_list = txt.split(";")
    for i in string_list:
        i = i.strip()
    string_list = [each_string.lower() for each_string in string_list]
    return string_list

newItem = {}
listItems = []

#crate api by research_area
research_area = "toán"
api = "http://qldt.neu.edu.vn/LLKHAPI/api/ThongTinLyLich/LayDanhSach?strTuKhoa="
api += research_area
api += "&pageIndex=1&pageSize=10000&iTrangThai=1&iTinhTrang=1&loaitimkiem=LINHVUC"

#connect to api and get data
response = requests.get(api)
print(response.status_code)
data = response.json()['Data']

#add data to var newItem
for i in data:
    newItem["other link"] : ""
    newItem["address"] = i["DIACHILIENLAC"]
    newItem["gender"] = gender(i["TENGIOITINH"])
    newItem["degree"] = i["LOAIHOCVI"]
    newItem["score"] = 0
    newItem["birth"] = i["NAMSINH"]
    newItem["phone"] = i["SODIENTHOAIDIDONG"]
    newItem["name"] = i["HO"] + " " + i["TEN"]
    newItem["company"] = i["COQUANCONGTAC"]
    newItem["email"] = i["DIACHIEMAIL"]
    newItem["link profile"] = "http://qldt.neu.edu.vn/LyLichKhoaHoc/LyLichKhoaHoc.aspx?Id=" + i["ID"]
    newItem["img"] = ""
    newItem["research area"] = RA(i["LVNC_LINHVUCNGHIENCUU"])
    newItem["research area en"] = []
    newItem["location"] = {'features': [{'geometry': {'coordinates': [0, 0], 'type': 'Point'}, 'type': 'Feature'}], 'type': 'FeatureCollection'}
    listItems.append(newItem)

#add data to json file
with open("experts.json", "w") as outfile:
    json.dump(listItems, outfile)

'''
flex research area to search
create ID check duplicate
research area to en
'''

