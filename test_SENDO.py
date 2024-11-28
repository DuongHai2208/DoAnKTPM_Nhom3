import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime 

class TestTestCase3():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_testCase3(self,a,b):
    with open(a, "r", encoding="utf-8") as f:
      tc = []
      for line in f:
          parts = line.strip() 
          tc.append(parts)
    print(tc)
    self.driver.get("https://www.sendo.vn/")
    self.driver.maximize_window()

    f = open(b, "w")
    f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    f.close()

    time.sleep(2)
    for i in tc:
      self.driver.find_element(By.ID, "sendo-search").click()
      self.driver.find_element(By.ID, "sendo-search").send_keys(i)
      time.sleep(2)
      self.driver.find_element(By.CSS_SELECTOR, ".d7ed-AREzVq > .d7ed-SwZDZ2").click()
      time.sleep(3)
      element = self.driver.find_element(By.CSS_SELECTOR, ".d7ed-d4keTB:nth-child(1) .d7ed-fMmmQd")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).perform()
      self.vars["window_handles"] = self.driver.window_handles
      self.driver.find_element(By.CSS_SELECTOR, ".d7ed-d4keTB:nth-child(1) .d7ed-fMmmQd").click()
      time.sleep(2)
      self.vars["win7530"] = self.wait_for_window(2000)
      element = self.driver.find_element(By.CSS_SELECTOR, "body")
      actions = ActionChains(self.driver)
      # actions.move_to_element(element, 0, 0).perform()
      time.sleep(1)
      self.driver.switch_to.window(self.vars["win7530"])
      time.sleep(2)
      self.driver.find_element(By.CSS_SELECTOR, ".d7ed-d4keTB > .d7ed-Bb3ss4").click()
      time.sleep(2)
      self.driver.find_element(By.CSS_SELECTOR, ".\\_61de-TWfhEi .d7ed-SwZDZ2").click()
      time.sleep(2)
      element = self.driver.find_element(By.CSS_SELECTOR, ".d7ed-ytwGPk.d7ed-oGo8Ct.d7ed-KXpuoS")
      link_text_value = element.text
      if link_text_value ==  i:
        rs = "Passed"
      else:
        rs = "Failed"
      print(rs)
      with open(b, "a") as f:
        f.write(f"\n{rs}")

test_1 = TestTestCase3()
test_1.setup_method(open)
test_1.test_testCase3("textInputTest.txt","result.txt")
test_1.teardown_method(quit)