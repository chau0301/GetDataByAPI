import requests
import json
import unicodedata

def gender(text):
    return 0 if text == "Nam" else 1

def RA(txt):
    txtList = []
    txtList = txt.split("-")
    for i in range(len(txtList)):
        txtList[i] = txtList[i].strip().lower()
    while "" in txtList:
        txtList.remove("")
    return txtList

def createAPI(RA):
    research_area = RA
    api = "http://qldt.neu.edu.vn/LLKHAPI/api/ThongTinLyLich/LayDanhSach?strTuKhoa="
    api += research_area
    api += "&pageIndex=1&pageSize=10000&iTrangThai=1&iTinhTrang=1&loaitimkiem=LINHVUC"
    return api

def duplicateCheckRead(idExist):
    with open('duplicateCheck.txt', 'r') as f:
        idExist = f.read().splitlines()

def duplicateCheckWrite(idExist):
    with open('duplicateCheck.txt', 'w') as f:
        for id in idExist:
            f.write(id)
            f.write('\n')

with open("research_area.json", encoding='utf8') as json_file:
    research = json.load(json_file)

listItems = []
researchList = []
idExist = []

#add data to var newItem
def dataJsonFile(data, research_area):
    newItem = {}
    for i in data:
        if i["ID"] not in idExist:
            idExist.append(i["ID"])
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
            newItem["research area"] = research_area
            newItem["research area en"] = []
            newItem["location"] = {'features': [{'geometry': {'coordinates': [0, 0], 'type': 'Point'}, 'type': 'Feature'}], 'type': 'FeatureCollection'}
            listItems.append(newItem)
            newItem= {}


for i in research:
    researchList.append(i["name_vn"])
    for j in i["keys"] :
        if j not in researchList:
            researchList.append(j)

for reasearchArea in researchList:
    duplicateCheckRead(idExist)
    api = createAPI(reasearchArea)
    response = requests.get(api)
    if int(response.status_code) == 200:
        data = response.json()['Data']
        dataJsonFile(data,reasearchArea)
        duplicateCheckWrite(idExist)
        fileName = "./jsonData/" + reasearchArea + ".json"
        with open(fileName, "w") as outfile:
            json.dump(listItems, outfile)
    else:
        print("Error:" + reasearchArea)



