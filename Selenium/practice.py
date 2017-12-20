from selenium import webdriver
import time as t
from selenium.webdriver.common.keys import Keys
from amazon1.login.sql_connection import mysqlconn
chrome_driver_path="C:\\Users\\Max\\Desktop\\python\\chromedriver.exe"
#driver = webdriver.Chrome("C:\\Users\\Max\\Desktop\\python\\chromedriver.exe")
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.amazon.com/Motorola-Certified-Comcast-Spectrum-BrightHouse/dp/B01A1E6BA2/ref=pd_sim_147_1?_encoding=UTF8&pd_rd_i=B01A1E6BA2&pd_rd_r=KJWSG8QVJFK5ZKMTQC7G&pd_rd_w=UKfRh&pd_rd_wg=MMAxP&psc=1&refRID=KJWSG8QVJFK5ZKMTQC7G")
#productTitle= driver.find_element_by_xpath("//*[@id='productTitle']").text
#print(productTitle)


item_name= driver.find_element_by_xpath("//*[@id='productTitle']").text
price=driver.find_element_by_xpath("//*[@id='priceblock_ourprice']").text
brand_name=driver.find_element_by_xpath("//*[@id='productDetails_techSpec_section_1']/tbody/tr[1]/td").text
series=driver.find_element_by_xpath("//*[@id='productDetails_techSpec_section_1']/tbody/tr[2]/td").text
asin=driver.find_element_by_xpath("//*[@id='productDetails_detailBullets_sections1']/tbody/tr[1]/td").text
#category` have to parce bsr and choose one where len bigger !!!!   
color=driver.find_element_by_xpath("//*[@id='productDetails_techSpec_section_1']/tbody/tr[7]/td").text
weight=driver.find_element_by_xpath("//*[@id='productDetails_techSpec_section_1']/tbody/tr[4]/td").text
shipping_weight = driver.find_element_by_xpath("//*[@id='productDetails_detailBullets_sections1']/tbody/tr[4]/td").text
product_size =driver.find_element_by_xpath("//*[@id='productDetails_techSpec_section_1']/tbody/tr[5]/td").text
item_size =driver.find_element_by_xpath("//*[@id='productDetails_techSpec_section_1']/tbody/tr[6]/td").text
quality =driver.find_element_by_xpath("//*[@id='acrPopover']/span[1]/a/i[1]/span").text
seller_name =driver.find_element_by_xpath("//*[@id='bylineInfo']").text
bsr_1 =driver.find_element_by_xpath("//*[@id='productDetails_detailBullets_sections1']/tbody/tr[3]/td/span/span").text
#bsr_2 =driver.find_element_by_xpath("//*[@id='productDetails_detailBullets_sections1']/tbody/tr[3]/td/span/span[2]").text
#bsr_3 =driver.find_element_by_xpath("//*[@id='productDetails_detailBullets_sections1']/tbody/tr[3]/td/span/span[3]").text
count_reviews =driver.find_element_by_xpath("//*[@id='acrCustomerReviewText']").text
answered_questions =driver.find_element_by_xpath("//*[@id='askATFLink']/span").text
date_first_available = driver.find_element_by_xpath("//*[@id='productDetails_detailBullets_sections1']/tbody/tr[7]/td").text



print (item_name)
print (price)
print (brand_name)
print (series)
print (asin)
#print(category)
print (color)
print (weight)
print (shipping_weight)
print (product_size)
print (item_size)
print (quality)
print (seller_name)
print (bsr_1)
#print ("bsr_2")
#print ("bsr_3")
print (count_reviews)
print (answered_questions)
print (date_first_available)

sql = """insert into amazon.temp (
						item_name,
						price,
						brand_name ,
						series , 
						asin, 
						color, 
						weight, 
						shipping_weight,
						product_size, 
						item_size, 
						quality,
						seller_name,
						bsr_1, 
						count_reviews,
						answered_questions,
						date_first_available
						)
						values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" ,(item_name , price, brand_name , series ,asin , color ,weight , shipping_weight , product_size , item_size , quality, seller_name ,bsr_1 , count_reviews ,answered_questions, date_first_available  )

mysqlconn(sql)