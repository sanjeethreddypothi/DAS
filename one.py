from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


chromeOptions = webdriver.ChromeOptions()
prefs = {"plugins.always_open_pdf_externally": True}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "C:/Users/Dell/Downloads/chromedriver"
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

actionChains = ActionChains(browser)

#browser=webdriver.Chrome("C:/Users/Dell/Downloads/chromedriver")



browser.get('https://www.screener.in/')
#sbox=browser.find_element_by_link_test('Search for a company')
sbox = browser.switch_to.active_element
#avenue super(1-4), adani green(1-3), divi(1-10), "SBI Life Insura"(1-3),sbi card(1)
j=["Reliance Industr","TCS","HDFC Bank","Infosys","Hindustan Unilever Ltd","HDFC","ICICI Bank","kotak mahi","state bank of india","Bajaj Finance","Bharti Airtel","HCL Technologies","ITC","Asian Paints","Wipro","Axis Bank","Maruti Suzuki","UltraTech C","Larsen & Toubro","Nestle India","Adani Ports","Bajaj Finserv","JSW Steel","Sun Pharmaceuticals Industries Ltd","HDFC Life In","Titan Company","Hindustan Zinc","O N G C","Adani Ente","Shree Cement","Tata Motors","Adani Transmissi","Tata Steel","Adani Total Gas","Power Grid Corp","Bajaj Auto","NTPC","Tech Mahindra","Dabur India","M & M","Pidilite Ind","Grasim In","BPCL","Britannia In","Vedanta"]

for t in j:
    sbox.send_keys(t)

    sbox.click()

    sbox.send_keys(Keys.RETURN)

    down=browser.find_element_by_link_text('Documents')
    down.click()
#source=browser.find_element_by_link_text("")
    for i in range(1,12):
        t=browser.find_element_by_xpath("//*[@id='documents']/div[2]/div[2]/div/ul/li["+str(i)+"]/a")
#actionChains.context_click(t).send_keys(Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()

        href = t.get_attribute('href')
        download = browser.get(href)
    browser.get('https://www.screener.in/')
    sbox = browser.switch_to.active_element



#obtain page sourcck()
#link.click()


