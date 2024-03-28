import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EkwFetcher:
  def __init__(self):
      self.driver = webdriver.Firefox()

  def fetchContents(self, department: str, registryNumber: str, controlDigit: str ) -> str:
    self.driver.get('https://przegladarka-ekw.ms.gov.pl/eukw_prz/KsiegiWieczyste/wyszukiwanieKW')
    # Wait until the form is fully loaded
    department_input = WebDriverWait(self.driver, 15).until(
        EC.visibility_of_element_located((By.ID, 'kodWydzialuInput'))
    )
    self.driver.find_element(By.ID, 'kodWydzialuInput').send_keys(department)
    self.driver.find_element(By.ID, 'numerKsiegiWieczystej').send_keys(registryNumber)
    self.driver.find_element(By.ID, 'cyfraKontrolna').send_keys(controlDigit)
    self.driver.find_element(By.ID, 'wyszukaj').click()
    self.driver.find_element(By.ID, 'przyciskWydrukZwykly').click()
    self.driver.find_element(By.CSS_SELECTOR, 'td:nth-child(4) input:nth-child(7)').click()
    html = self.driver.page_source
    self.driver.quit()
    return html
