from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToWindow:
    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        # The parent window
        driver.find_element(By.ID, "openwindow").click()
        parents_handle = driver.current_window_handle
        print("Parents handle: " + parents_handle)
        time.sleep(2)

        # Children window
        child_handle = driver.window_handles

        for handle in child_handle:
            print("The handle: " + handle)
            if handle not in parents_handle:
                driver.switch_to.window(handle)
                print("switch handle to: "+handle)
                search_box = driver.find_element(By.ID, "search-courses")
                search_box.send_keys("python")
                time.sleep(2)
                driver.close()
                break

        # Switch to parents handle
        driver.switch_to.window(parents_handle)
        driver.find_element(By.ID, "name").send_keys("hello sherry")

        time.sleep(10)


sherry_test = SwitchToWindow()
sherry_test.test()




