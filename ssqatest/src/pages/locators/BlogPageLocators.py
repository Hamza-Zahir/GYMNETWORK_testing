from selenium.webdriver.common.by import By


class BlogPageLocators:

    # landing section
    LANDING_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div > div > div > div > h2')
    LANDING_DESC_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div > div > div > div > p')
   
    LANDING_LINK_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div > div > div > div > a')
    LANDING_LINK_IMG_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div > div > div > div > a img')
    LANDING_LINK_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div > div > div > div > a h3')
    LANDING_LINK_DESC_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div > div > div > div > a p:nth-child(2)')
    LANDING_LINK_DATE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div > div > div > div > a p:nth-child(3)')
   
    # blogs container
    DROPDOWN_BTN = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div > div > div > button')
    NEWEST_FIRST_BTN = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div > div > div > ul > li:nth-child(1) > button')
    LASTES_ARTICLES_BTN = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div > div > div > ul > li:nth-child(2) > button')
    MOST_POPULAR_BTN = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div > div > div > ul > li:nth-child(3) > button')

    CARD1_LINK_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(1) > a')
    CARD1_LINK_IMG_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(1) > a img')
    CARD1_LINK_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(1) > a h3')
    CARD1_LINK_DESC_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(1) > p:nth-child(2)')
    CARD1_LINK_DATE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(1) > p:nth-child(3)')
   
    CARD2_LINK_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(2) > a')
    CARD2_LINK_IMG_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(2) > a img')
    CARD2_LINK_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(2) > a h3')
    CARD2_LINK_DESC_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(2) > p:nth-child(2)')
    CARD2_LINK_DATE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(2) > p:nth-child(3)')
   
    CARD3_LINK_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(3) > a')
    CARD3_LINK_IMG_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(3) > a img')
    CARD3_LINK_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(3) > a h3')
    CARD3_LINK_DESC_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(3) > p:nth-child(2)')
    CARD3_LINK_DATE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(3) > p:nth-child(3)')
   
    CARD4_LINK_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(4) > a')
    CARD4_LINK_IMG_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(4) > a img')
    CARD4_LINK_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(4) > a h3')
    CARD4_LINK_DESC_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(4) > p:nth-child(2)')
    CARD4_LINK_DATE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(4) > p:nth-child(3)')
   
    CARD5_LINK_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(5) > a')
    CARD5_LINK_IMG_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(5) > a img')
    CARD5_LINK_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(5) > a h3')
    CARD5_LINK_DESC_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(5) > p:nth-child(2)')
    CARD5_LINK_DATE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > div> div > div:nth-child(5) > p:nth-child(3)')
   

