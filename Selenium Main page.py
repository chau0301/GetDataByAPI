import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#download driver and open chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(30)
driver.get("http://qldt.neu.edu.vn/LyLichKhoaHoc/TimKiemLLKH.aspx")

time.sleep(3)

#input data
search = driver.find_element(By.ID, "txtTuKhoa")
search.send_keys("công nghệ thông tin")
driver.find_element(By.CSS_SELECTOR,'#DropLoaiTimKiem_chosen > a > span').click()
driver.find_element(By.XPATH,'//*[@id="DropLoaiTimKiem_chosen"]/div/ul/li[2]').click()
driver.find_element(By.CSS_SELECTOR,'#btnTimKiem').click()
time.sleep(3)

print(driver.page_source)


#print(driver.execute_script("return document.documentElement.innerHTML;"))
input()
driver.quit()
