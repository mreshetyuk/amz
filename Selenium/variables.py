from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path="C:\\Users\\Max\\Desktop\\python\\chromedriver.exe"
#driver = webdriver.Chrome("C:\\Users\\Max\\Desktop\\python\\chromedriver.exe")
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.amazon.com/ARRIS-SURFboard-SB6190-DOCSIS-Cable/dp/B016PE1X5K/ref=pd_sbs_147_8?_encoding=UTF8&pd_rd_i=B016PE1X5K&pd_rd_r=JCWW1EAQZV2T8GBBVZRV&pd_rd_w=H6UBI&pd_rd_wg=SXix4&psc=1&refRID=JCWW1EAQZV2T8GBBVZRV")
productTitle= driver.find_element_by_xpath(".//*[@id='productDetails_detailBullets_sections1']/tbody/tr[3]/td/span/span").text
print(productTitle)

