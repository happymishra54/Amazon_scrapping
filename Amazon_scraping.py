#!/usr/bin/env python
# coding: utf-8

# In[34]:


from selenium import webdriver
import pandas as pd
from time import sleep
driver=webdriver.Chrome()
driver.get("https://amazon.in")
driver.maximize_window()
print("--------------------")
print(driver.title)
print("--------------------")
searchbox=driver.find_element('xpath','//*[@id="twotabsearchtextbox"]')
searchbutton=driver.find_element('xpath','//*[@id="nav-search-submit-button"]')
searchbox.send_keys('mobiles under 50000')
searchbutton.click()
mobile_names=[]
mobile_mrp=[]
mobile_price=[]
allmobiles=driver.find_elements('xpath','//div[@data-component-type="s-search-result"]')
for mobiles in allmobiles:
    names=mobiles.find_elements('xpath','//div[@class="a-section a-spacing-none puis-padding-right-small s-title-instructions-style"]')
    mrp=mobiles.find_elements('xpath','//div[@class="a-section aok-inline-block"]')
    price=mobiles.find_elements('xpath','//span[@class="a-price-whole"]')
    for name in names:
        mobile_names.append(name.text)
    for mrps in mrp:
        mobile_mrp.append(mrps.text)
    for prices in price:
        mobile_price.append(prices.text)
data=pd.DataFrame()
data['Names']=mobile_names
data['MRP']=mobile_mrp
data['Price']=mobile_price
data.to_excel('mobiles.xlsx',index=False)
sleep(5)
driver.quit()


# In[ ]:




