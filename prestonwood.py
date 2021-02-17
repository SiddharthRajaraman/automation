from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://prestonwood.com/')

driver.find_element_by_id('p_lt_Header_MyProfilePages_lblSignIn').click()


username = driver.find_element_by_id('p_lt_ContentWidgets_pageplaceholder_p_lt_zoneContent_CHO_Widget_LoginFormWithFullscreenBackground_XLarge_loginCtrl_BaseLogin_UserName')
username.clear()
username.send_keys("bxrbxr")

password = driver.find_element_by_id('p_lt_ContentWidgets_pageplaceholder_p_lt_zoneContent_CHO_Widget_LoginFormWithFullscreenBackground_XLarge_loginCtrl_BaseLogin_Password')
password.clear()
password.send_keys('WNNmPq8H#KNZ')

driver.find_element_by_id('p_lt_ContentWidgets_pageplaceholder_p_lt_zoneContent_CHO_Widget_LoginFormWithFullscreenBackground_XLarge_loginCtrl_BaseLogin_LoginButton').click()


driver.find_element_by_id('p_lt_ContentWidgets_pageplaceholder_p_lt_zoneSM30_CHO_Widget_QuickLinkMenu_Small_rptItems_ctl00_hrefLink').click()

driver.find_element_by_xpath('//a[@href="'"../prestonwoodccnc_golf_m56/Member_msg?user=R313&name=Bala Rajaraman&message="'"]').click()

time.sleep(5)
print ('hi')








