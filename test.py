import json

with open("research_area.json", encoding='utf8') as json_file:
    research = json.load(json_file)

researchList = []
for i in research:
    researchList.append(i["name_vn"])
    for j in i["keys"] :
        if j not in researchList:
            researchList.append(j)

print(researchList)
