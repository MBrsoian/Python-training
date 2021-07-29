# Generated by Selenium IDE
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

class TestStch():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_stch(self):
    self.driver.get("http://10.51.30.52:8090/main/desktop-login.html")
    self.driver.set_window_size(968, 1020)
    self.driver.find_element(By.ID, "idInputUsername").click()
    self.driver.find_element(By.ID, "idInputUsername").send_keys("supervisor")
    self.driver.find_element(By.ID, "idInputPassword").click()
    self.driver.find_element(By.ID, "idInputPassword").send_keys("**")
    self.driver.find_element(By.ID, "submit.button").click()
    self.driver.find_element(By.ID, "BVMAPS").click()
    self.driver.find_element(By.CSS_SELECTOR, "#UI_BADGES_GRID\\.gridView\\.row\\#22_Tcell\\#0 > div > div").click()
    self.driver.find_element(By.ID, "badge.html.ribbon.properties").click()
    self.driver.find_element(By.ID, "__selection_4").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#\\__pan_4 > .listItemNormal:nth-child(4)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "#PROPERTIES_CONTROLS td:nth-child(2) .middlePart")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, "#PROPERTIES_CONTROLS td:nth-child(2) .middlePart").click()
    self.driver.find_element(By.ID, "badge.html.ribbon.properties.apply").click()
    self.driver.find_element(By.CSS_SELECTOR, "body > img").click()
    self.driver.find_element(By.CSS_SELECTOR, "a > img").click()
    self.driver.find_element(By.ID, "main.html.btn_logout").click()

