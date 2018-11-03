from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToFrame:
    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)
        driver.execute_script("window.scrollBy(0,1000);")

        # Switch to Frame using frame's id
        # driver.switch_to.frame("courses-iframe")
        # Switch to Frame using frame's name
        driver.switch_to.frame("iframe-name")
        # Switch to Frame using frame's number - frame index
        # -- driver.switch_to.frame(0)

        # Find element in the frame
        driver.find_element(By.ID, "search-courses").send_keys("python")
        time.sleep(5)

        # Switch to parents handle
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,-1000);")
        driver.find_element(By.ID, "name").send_keys("hello sherry")

        time.sleep(10)


sherry_test = SwitchToFrame()
sherry_test.test()




