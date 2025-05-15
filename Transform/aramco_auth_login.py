from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://aramco-lb.qa.sps.secops.bmc.com/rsso/start")

driver.find_element(By.ID, "username").send_keys("hannah_admin")
driver.find_element(By.ID, "password").send_keys("Password_1234" + Keys.RETURN)

# Wait and navigate post-login
print(driver.current_url)
driver.quit()
