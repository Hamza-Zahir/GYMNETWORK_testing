
from selenium.webdriver.common.by import By


class FooterLocators:

    # footer
     
    FOOTER_LOGO_FIELD = (By.CSS_SELECTOR, '.footer_gym a.footer-brand') 
    FOOTER_DESC_FIELD = (By.CSS_SELECTOR, '.footer_gym p') 

    FOOTER_TWITTER_LINK_FIELD = (By.CSS_SELECTOR, '.footer_gym .footer-social a:nth-child(1)') 
    FOOTER_TELEGRAM_LINK_FIELD = (By.CSS_SELECTOR, '.footer_gym .footer-social a:nth-child(2)') 

    FOOTER_PRODUCTS_TITLE_FIELD = (By.CSS_SELECTOR, '.footer_gym div:nth-child(3) > h4') 
    FOOTER_PRODUCTS_VULTE_LINK_FIELD = (By.CSS_SELECTOR, '.footer_gym div:nth-child(3) > ul > li:nth-child(1) > a') 
    FOOTER_PRODUCTS_FARMING_LINK_FIELD = (By.CSS_SELECTOR, '.footer_gym div:nth-child(3) > ul > li:nth-child(2) > a') 
    FOOTER_PRODUCTS_SINGLE_POOL_LINK_FIELD = (By.CSS_SELECTOR, '.footer_gym div:nth-child(3) > ul > li:nth-child(3) > a') 
    FOOTER_PRODUCTS_BUY_GYMNET_LINK_FIELD = (By.CSS_SELECTOR, '.footer_gym div:nth-child(3) > ul > li:nth-child(4) > a') 

    FOOTER_ECO_SYSTEM_TITLE_FIELD = (By.CSS_SELECTOR, '.footer_gym div:nth-child(4) > h4') 
    FOOTER_GYMSTREET_LINK_FIELD = (By.CSS_SELECTOR, '.footer_gym div:nth-child(4) > ul > li:nth-child(1) > a') 
    FOOTER_METABOCKS_LINK_FIELD = (By.CSS_SELECTOR, '.footer_gym div:nth-child(4) > ul > li:nth-child(2) > a') 
    FOOTER_CASH_FT_LINK_FIELD = (By.CSS_SELECTOR, '.footer_gym div:nth-child(4) > ul > li:nth-child(3) > a') 
    FOOTER_ZUCKERLAND_LINK_FIELD = (By.CSS_SELECTOR, '.footer_gym div:nth-child(4) > ul > li:nth-child(4) > a') 
    FOOTER_GYM_DEX_LINK_FIELD = (By.CSS_SELECTOR, '.footer_gym div:nth-child(4) > ul > li:nth-child(5) > a') 
    FOOTER_WHITEPAPER_LINK_FIELD = (By.CSS_SELECTOR, '.footer_gym div:nth-child(4) > ul > li:nth-child(6) > a') 

    FOOTER_ABOUT_TITLE_FIELD = (By.CSS_SELECTOR, '.footer_gym div:nth-child(5) > h4') 
    FOOTER_BLOG_NEWS_LINK_FIELD = (By.CSS_SELECTOR, '.footer_gym div:nth-child(5) > ul > li:nth-child(1) > a') 
    FOOTER_SUPPORT_LINK_FIELD = (By.CSS_SELECTOR, '.footer_gym div:nth-child(5) > ul > li:nth-child(2) > a') 
    FOOTER_GUIDE_LINK_FIELD = (By.CSS_SELECTOR, '.footer_gym div:nth-child(5) > ul > li:nth-child(3) > a') 
    FOOTER_TOKEN_CONTRACT_LINK_FIELD = (By.CSS_SELECTOR, '.footer_gym div:nth-child(5) > ul > li:nth-child(4) > a') 

    FOOTER_INFO_LINK_FIELD = (By.CLASS_NAME, 'footer-info_item')

