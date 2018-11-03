from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class HandleAlert:
    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        driver.find_element(By.ID, "name").send_keys("Sherry")
        # Alert pop-up
        alert_button = driver.find_element(By.ID, "alertbtn")
        alert_button.click()
        time.sleep(10)
        pop_up_1 = driver.switch_to.alert
        pop_up_1.accept()
        time.sleep(5)

        # Confirmation pop-up
        driver.find_element(By.ID, "name").send_keys("Sherry")
        confirm_button = driver.find_element(By.ID, "confirmbtn")
        confirm_button.click()
        time.sleep(5)
        pop_up_2 = driver.switch_to.alert
        pop_up_2.accept()
        # pop_up_2.dismiss()
        time.sleep(10)


sherry_test = HandleAlert()
sherry_test.test()




