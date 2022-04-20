import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json

def RA(txt):
    lst = txt.split(";")
    for i in lst:
        i = i.strip()
    return lst

#download driver and open chrome
url = "http://qldt.neu.edu.vn/LyLichKhoaHoc/LyLichKhoaHoc.aspx?Id=6FA43154818E40D7982E47581B2143E8"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(30)
driver.get(url)
time.sleep(2)

#Json format
x = {
    "other link" : "",
    "address" : driver.find_element(By.CSS_SELECTOR,'#txtDiaChiLienLac').text,
    "gender" : "",
    "degree" : driver.find_element(By.CSS_SELECTOR,'#txtHocVi').text,
    "score" : "",
    "birth" : driver.find_element(By.CSS_SELECTOR,'#txtNgaySinh').text,
    "phone" : driver.find_element(By.CSS_SELECTOR,'#txtSoDienThoai').text,
    "name" : driver.find_element(By.CSS_SELECTOR,'#txtTen').text,
    "company" : "Trường Đại học Kinh tế Quốc dân",
    "email" : driver.find_element(By.CSS_SELECTOR,'#txtSoDienThoai > span > span').text,
    "link profile" : url,
    "img" : driver.find_element(By.CSS_SELECTOR,'#zoneAvatar > img').get_attribute("src"),
    "research area" : RA(driver.find_element(By.CSS_SELECTOR,'#txtLVNC').text),
    "research area en" : [],
    "location": {'features': [{'geometry': {'coordinates': [0, 0], 'type': 'Point'}, 'type': 'Feature'}], 'type': 'FeatureCollection'}
}


driver.quit()
