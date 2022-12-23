from selenium.webdriver.common.by import By


class HeaderLocators:
    
    # header
    LOGO_FIELD = (By.CSS_SELECTOR, 'nav a.navbar-brand img')
    HOME_LINK_FIELD = (By.CSS_SELECTOR, 'nav a.navbar-brand')
    PRODUCTS_LINK_FIELD = (By.CSS_SELECTOR, 'nav ul > li:nth-child(1) > a')
    ECO_SYSTEM_LINK_FIELD = (By.CSS_SELECTOR, 'nav ul > li:nth-child(2) > a')
    ABOUT_LINK_FIELD = (By.CSS_SELECTOR, 'nav ul > li:nth-child(3) > a')
    BLOG_LINK_FIELD = (By.CSS_SELECTOR, 'nav ul > li:nth-child(4) > a')
    LAUNCH_LINK_FIELD = (By.CSS_SELECTOR, 'nav form > a')
   
    CUSTOM_SELECT_FIELD = (By.CSS_SELECTOR, '#navbarSupportedContent > form > div > button')
    CHINESE_LINK_FIELD = (By.CSS_SELECTOR, '#navbarSupportedContent > form > div > div > ul > li:nth-child(9)')
    