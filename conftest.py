import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options as chOptions
# from selenium.webdriver.firefox.options import Options as ffOptions
# import os

@pytest.fixture(scope="class")
def init_driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    # driver.quit()

@pytest.fixture(scope="class")
def init_driver_with_metamask(request):
    EXTENSION_PATH = "D:\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\nkbihfbeogaeaoehlefnkodbefgpgknn\\10.14.1_0.crx"

    opt = webdriver.ChromeOptions()
    opt.add_extension(EXTENSION_PATH)
    driver = webdriver.Chrome(chrome_options=opt)
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    # driver.quit()





