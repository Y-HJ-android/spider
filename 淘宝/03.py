from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import logging
import pyautogui
import pyautogui
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
if __name__=='__main__':
    browser=webdriver.Chrome('/usr/local/chromedriver/chromedriver')
    options=webdriver.ChromeOptions()
    options.add_argument(f'--window-position={217},{172}')
    options.add_argument(f'--window-size={1200},{1000}')
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",

    })
    browser.get('https://uland.taobao.com/sem/tbsearch')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="J_LoginInfoHd"]/a[1]').click()
    browser.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys('*******')
    browser.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys('********')
    time.sleep(1)
    try:
        slider = browser.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
        if slider.is_displayed():
            print("出现滑块")
            action=ActionChains(browser)
            action.drag_and_drop_by_offset(slider,300,0).perform()
            time.sleep(0.5)
            action.release().perform()
            print("滑动完成")
    except  NoSuchElementException|WebDriverException as e:
        logger.info('未出现登录验证码')
    # coords = pyautogui.locateOnScreen('1.png')
    # x, y = pyautogui.center(coords)
    # pyautogui.leftClick(x, y)
    a=browser.find_element_by_xpath('//*[@id="login-form"]/div[4]/button')
    if a.is_displayed():
        a.click()
    print("点击登录")
    time.sleep(1)
    usrname=browser.find_element_by_xpath('//*[@id="J_LoginInfo"]/div[1]/a')
    print(usrname.text)
    a = browser.find_element_by_xpath('// *[ @ id = "mc-menu-hd"] / span[2]')
    if a.is_displayed():
        a.click()
    a = browser.find_element_by_xpath('//*[@id="J_SelectAll1"]/div/label')
    if a.is_displayed():
        a.click()
    time.sleep(2)
    a = browser.find_element_by_xpath('//*[@id="J_Go"]/span')
    if a.is_displayed():
        print("结算")
        a.click()
    time.sleep(2)
    a = browser.find_element_by_xpath('//*[@id="submitOrderPC_1"]/div/a[2]')
    if a.is_displayed():
        print("结算")
        a.click()
    time.sleep(10)
    pyautogui.press('2')
    pyautogui.press('2')
    pyautogui.press('2')
    pyautogui.press('2')
    pyautogui.press('2')
    pyautogui.press('2')
    # a = browser.find_element_by_id('payPassword_rsainput')
    # if a.is_displayed():
    #     a.send_keys('222222')
    # browser.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[2]').send_keys('2')
    # browser.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[3]').send_keys('2')
    # browser.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[4]').send_keys('2')
    # browser.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[5]').send_keys('2')
    # browser.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[6]').send_keys('2')
    browser.find_element_by_xpath('//*[@id="J_authSubmit"]').click()


