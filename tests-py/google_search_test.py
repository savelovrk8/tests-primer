import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
  wd = webdriver.Chrome()
  request.addfinalizer(wd.quit)
  return wd

def test_example(driver):
  driver.get("https://www.google.com/ncr")
  driver.find_element_by_name("q").send_keys("webdriver")
  driver.find_element_by_name("q").send_keys(u'\ue007')
  WebDriverWait(driver, 10).until(EC.title_is("webdriver - Google Search"))
