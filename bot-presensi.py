from selenium import webdriver
import pyautogui
import time

browser = webdriver.Chrome("C:/Installer Apps/Selenium Drivers/Chrome/chromedriver.exe")

# ===== Link Presensi =====
browser.get("https://docs.google.com/forms/d/e/1FAIpQLSdkR1H59J2RA9zCADZfS9kkiWTBrf3gPMjd9Ti_byDA6CCFKg/formResponse")

# ===== Nama =====
browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("MUHAMMAD HANIF ABID WIHANANTO")

# ===== Nomor Absen =====
browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("21")

# ===== Kelas =====
browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]").click()

# XI 
index_number = 2
time.sleep(1)
for _ in range(index_number):
	pyautogui.keyDown("down"); pyautogui.keyUp("down")
pyautogui.keyDown("enter"); pyautogui.keyUp("enter")

# ===== Tanggal =====
info_waktu = time.localtime()
tgl = info_waktu[2]
bln = info_waktu[1]
thn = info_waktu[0]

browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input").send_keys(tgl)
browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input").send_keys(bln)
browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input").send_keys(thn)

# ===== Keterangan =====
radio_button = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupEl")
for radio in radio_button:
	if radio.get_attribute("data-value").lower() == "hadir":
		radio.click()

# ===== Berikutnya =====
berikutnya = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
berikutnya.click()

# ===== Kelas =====
browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]").click()

# XI MIPA 8
index_number1 = 8
time.sleep(1)
for _ in range(index_number1):
	pyautogui.keyDown("down"); pyautogui.keyUp("down")
pyautogui.keyDown("enter"); pyautogui.keyUp("enter")

# Kirim 
kirim = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span/span').click()