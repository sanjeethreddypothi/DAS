# -*- coding: utf-8 -*-
"""
Created on Thu May 13 00:01:45 2021

@author: Dell
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date

today = date.today()

today=today.strftime("%d/%m/%Y")
chromeOptions = webdriver.ChromeOptions()
prefs = {"plugins.always_open_pdf_externally": True}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "C:/Users/Dell/Downloads/chromedriver"
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

#browser=webdriver.Chrome("C:/Users/Dell/Downloads/chromedriver")



browser.get("https://www.bseindia.com/corporates/ann.html")
#sbox=browser.find_element_by_link_test('Search for a company')


j=["HDFC BANK LTD","TATA MOTORS LTD","RELIANCE INDUSTRIES LTD","INFOSYS LTD","ADANI ENTERPRISES LTD"]
k=0
for t in j:
    browser.get("https://www.bseindia.com/corporates/ann.html")
    browser.implicitly_wait(10)
    sbox=browser.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div[2]/div[2]/input').click()
    sbox = browser.switch_to.active_element
    sbox.send_keys(Keys.ENTER)
    sbox=browser.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div[2]/div[4]/input').click()
    sbox = browser.switch_to.active_element
    sbox.send_keys(Keys.ENTER)
    sbox = browser.find_element_by_xpath('//*[@id="scripsearchtxtbx"]')
    sbox.send_keys(t)
    sbox.send_keys(Keys.ENTER)
    sbox=browser.find_element_by_xpath('//*[@id="btnSubmit"]').click()
    hi=browser.find_elements_by_xpath("//a[contains(@class,'tablebluelink')]")
   # hi2=browser.find_elements_by_xpath("//a[contains(@class,'tablebluelink ng-binding')]")
    try: 
        for i in hi:
            i.click()   
            
        browser.get("https://www.bseindia.com/corporates/ann.html")
    except Exception:
        browser.get("https://www.bseindia.com/corporates/ann.html")
    
    
    

    
