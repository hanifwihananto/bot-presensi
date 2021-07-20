from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
a = webdriver.Chrome(executable_path = "C:\Installer Apps\Selenium Drivers\Chrome\chromedriver.exe", chrome_options = chrome_options)

# ===== Link Presensi =====
a.get("https://docs.google.com/forms/d/e/1FAIpQLSecTBVViKVBctd5Hh80FVTVHjEN8tUS8C9brwhesv0qbcfktQ/viewform?usp=sf_link")

# ===== Nama ===== 
# full xpath
a.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("MUHAMMAD HANIF ABID WIHANANTO")

# ===== Nomor Absen =====
# full xpath
a.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys("21")

# ===== Kelas ===== 
# class name
a.find_element_by_class_name("quantumWizMenuPaperselectOptionList").click()

# full xpath
# a.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]").click()

# ===== XI =====
# full xpath
a.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[4]").click()

# selector
# a.find_element_by_css_selector("#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(3) > div > div > div.freebirdFormviewerComponentsQuestionSelectRoot > div > div.exportSelectPopup.quantumWizMenuPaperselectPopup.appsMaterialWizMenuPaperselectPopup > div.quantumWizMenuPaperselectOption.appsMaterialWizMenuPaperselectOption.freebirdThemedSelectOptionDarkerDisabled.exportOption.isSelected").click()

# ===== Tanggal =====
# full xpath
a.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input")

# ===== Keterangan =====
# full xpath
a.find_element_by_css_selector("#i22 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div").click()