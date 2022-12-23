from selenium.webdriver.common.by import By


class DashboardPageLocators:
    HEADER_TITLE = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[3]/div[1]/h2')
    CONNECT_WALLET_BTN = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[3]/div[3]/div[2]/button') 
    METAMASK_BTN = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[3]/div[3]/div[2]/div/div/div/div/div/div/div[1]/button')
    SPONSOR_ID_INFO = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div[4]/div/div[1]/div/div/div/div')


