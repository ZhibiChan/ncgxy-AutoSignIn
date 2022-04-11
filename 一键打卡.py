from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import linecache
u=len(open(r"身份证.txt",'rU').readlines())
for x in range(u):
    options = webdriver.EdgeOptions()
    options.add_argument("headless")
    driver = webdriver.Edge(options=options)
    driver.get("https://sso.ncgxy.com:9089/login/reg?queryMap.reg_type=stu")
    key=linecache.getline('身份证.txt',x+1)
    driver.find_element_by_id("phone").send_keys(key)
    button = driver.find_element_by_class_name('btn_submit')
    button.click()
    sleep(3)
    try:
        d = driver.find_element_by_css_selector("h1").text
        if d == '我的校园出入电子通行卡':
            driver.quit()
    except:

        driver.find_element_by_css_selector("input[value='1'][name='vo.jkStatus']").click()
        driver.find_element_by_css_selector("input[value='2'][name='vo.gl']").click()
        driver.find_element_by_css_selector("input[value='2'][name='vo.jqs']").click()
        driver.find_element_by_css_selector("input[value='1'][name='vo.jzym']").click()
        Select(driver.find_element_by_id('ymxq')).select_by_index(3)
        sleep(3)
        driver.find_element_by_id('my_btn').click()
        try:
            d = driver.find_element_by_css_selector("h1").text
            if d=='您的校园出入电子通行码':
                driver.quit()
        except:
            sleep(5)
            driver.quit()
        
        
        
