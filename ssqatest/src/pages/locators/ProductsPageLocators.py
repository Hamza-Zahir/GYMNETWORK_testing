from selenium.webdriver.common.by import By


class ProductsPageLocators:
    
    
    # # header
    # LOGO_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[1]/nav/div/a/img')
    # HOME_LINK_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[1]/nav/div/a')
    # PRODUCTS_LINK_FIELD = (By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[1]/a')
    # ECO_SYSTEM_LINK_FIELD = (By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/a')
    # ABOUT_LINK_FIELD = (By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[3]/a')
    # BLOG_LINK_FIELD = (By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[4]/a')
    # LAUNCH_LINK_FIELD = (By.XPATH, '//*[@id="navbarSupportedContent"]/form/a')
   
    # landing section
    LANDING_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.header_section > div > div > div > h1')
    LANDING_DESC_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.header_section > div > div > div > p')
    LAUNCH_APP_BTN = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.header_section > div > div > div > a')
    LANDING_SECTION_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]')
    

    # earning section
    EARNING_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.earning_section > h2')
    EARNING_IMG_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.earning_section > img')


    # products section
    PRODUCTS_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.products_section > div > h2')

    PRODUCTS_CARD1_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.products_section > div > div > div > div:nth-child(1) > div > h3')
    PRODUCTS_CARD1_DESC_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.products_section > div > div > div > div:nth-child(1) > div > p')
    PRODUCTS_CARD1_BTN_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.products_section > div > div > div > div:nth-child(1) > div > a')
    PRODUCTS_CARD1_IMG_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.products_section > div > div > div > div:nth-child(1) > img')

    PRODUCTS_CARD2_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.products_section > div > div > div > div:nth-child(2) > div > h3')
    PRODUCTS_CARD2_DESC_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.products_section > div > div > div > div:nth-child(2) > div > p')
    PRODUCTS_CARD2_BTN_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.products_section > div > div > div > div:nth-child(2) > div > a')
    PRODUCTS_CARD2_IMG_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.products_section > div > div > div > div:nth-child(2) > img')

    PRODUCTS_CARD3_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.products_section > div > div > div > div:nth-child(3) > div > h3')
    PRODUCTS_CARD3_DESC_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.products_section > div > div > div > div:nth-child(3) > div > p')
    PRODUCTS_CARD3_BTN_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.products_section > div > div > div > div:nth-child(3) > div > a')
    PRODUCTS_CARD3_IMG_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.products_section > div > div > div > div:nth-child(3) > img')

    PRODUCTS_CARD4_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.products_section > div > div > div > div:nth-child(4) > div > h3')
    PRODUCTS_CARD4_DESC_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.products_section > div > div > div > div:nth-child(4) > div > p')
    PRODUCTS_CARD4_BTN_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.products_section > div > div > div > div:nth-child(4) > div > a')
    PRODUCTS_CARD4_IMG_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.products_section > div > div > div > div:nth-child(4) > img')


    # vault section 
    VAULT_TITLE_FIELD = (By.CSS_SELECTOR, '#vault > h2')
    VAULT_DESC1_FIELD = (By.CSS_SELECTOR, '#vault > p:nth-child(2)')
    VAULT_DESC2_FIELD = (By.CSS_SELECTOR, '#vault > p:nth-child(3)')


    # vault next section
    VAULT_NEXT_DESC1_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[5]/div/div/div/p[1]')
    VAULT_NEXT_DESC2_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[5]/div/div/div/p[2]')
    VAULT_NEXT_BTN_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[5]/div/div/div/button/a')
    VAULT_NEXT_IMG_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[5]/div/div/img')
    VAULT_NEXT_SECTION_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[5]')


    # farming section 
    FARMING_BTN_FIELD = (By.CSS_SELECTOR,'#farming > div.position-relative.overflow-hidden.w-100.show-for-desktop > div.animationSection.farm > div.farming > h2')
    SINGLE_POOL_BTN_FIELD = (By.CSS_SELECTOR,'#farming > div.position-relative.overflow-hidden.w-100.show-for-desktop > div.animationSection.single_pool > div.farming > h2')
    
    SINGLE_POOL_TITLE_FIELD = (By.CSS_SELECTOR,'#farming > div.position-relative.overflow-hidden.w-100.show-for-desktop > div.animationSection.farm > div.single-pool > h2')
    SINGLE_POOL_DESC_FIELD = (By.CSS_SELECTOR,'#farming > div.position-relative.overflow-hidden.w-100.show-for-desktop > div.animationSection.farm > div.single-pool > p')
    SINGLE_POOL_START_BTN_FIELD = (By.CSS_SELECTOR,'#farming > div.position-relative.overflow-hidden.w-100.show-for-desktop > div.animationSection.farm > div.single-pool > a')

    FARMING_TITLE_FIELD = (By.CSS_SELECTOR,'#farming > div.position-relative.overflow-hidden.w-100.show-for-desktop > div.animationSection.single_pool > div.single-pool > h2')
    FARMING_DESC_FIELD = (By.CSS_SELECTOR,'#farming > div.position-relative.overflow-hidden.w-100.show-for-desktop > div.animationSection.single_pool > div.single-pool > p')
    FARMING_BTN_START_FIELD = (By.CSS_SELECTOR,'#farming > div.position-relative.overflow-hidden.w-100.show-for-desktop > div.animationSection.single_pool > div.single-pool > a')


    # holder section
    HOLDER_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.holder_section.container > h2')
    
    HOLDER_CARD1_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.holder_section.container > div > div:nth-child(1) > h4')
    HOLDER_CARD1_DESC_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.holder_section.container > div > div:nth-child(1) > p')
    
    HOLDER_CARD2_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.holder_section.container > div > div:nth-child(2) > h4')
    HOLDER_CARD2_DESC_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.holder_section.container > div > div:nth-child(2) > p')
    
    HOLDER_CARD3_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.holder_section.container > div > div.holder_section-benefits_item.withBg > h4')
    HOLDER_CARD3_DESC1_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.holder_section.container > div > div.holder_section-benefits_item.withBg > p:nth-child(2)')
    HOLDER_CARD3_DESC2_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.holder_section.container > div > div.holder_section-benefits_item.withBg > p:nth-child(3)')
    
    HOLDER_CARD4_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.holder_section.container > div > div:nth-child(4) > h4')
    HOLDER_CARD4_DESC_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.holder_section.container > div > div:nth-child(4) > p')
 

    # get started section
    GET_STARTED_TITLE_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > h2') 

    GET_STARTED_CARD1_NUM_FIELD = (By.CSS_SELECTOR, '.network_item:nth-child(1) h2') 
    GET_STARTED_CARD1_TITLE_FIELD = (By.CSS_SELECTOR, '.network_item:nth-child(1) h3') 
    GET_STARTED_CARD1_DESC_FIELD = (By.CSS_SELECTOR, '.network_item:nth-child(1) p') 
    GET_STARTED_CARD1_LINK = (By.CSS_SELECTOR, '.network_item:nth-child(1) a') 
    GET_STARTED_CARD1_IMG_FIELD = (By.CSS_SELECTOR, '.network_item:nth-child(1) .network_item-img img') 

    GET_STARTED_CARD2_NUM_FIELD = (By.CSS_SELECTOR, '.network_item:nth-child(2) h2') 
    GET_STARTED_CARD2_TITLE_FIELD = (By.CSS_SELECTOR, '.network_item:nth-child(2) h3') 
    GET_STARTED_CARD2_DESC_FIELD = (By.CSS_SELECTOR, '.network_item:nth-child(2) p') 
    GET_STARTED_CARD2_LINK = (By.CSS_SELECTOR, '.network_item:nth-child(2) a') 
    GET_STARTED_CARD2_IMG_FIELD = (By.CSS_SELECTOR, '.network_item:nth-child(2) .network_item-img img') 

    GET_STARTED_CARD3_NUM_FIELD = (By.CSS_SELECTOR, '.network_item:nth-child(3) h2') 
    GET_STARTED_CARD3_TITLE_FIELD = (By.CSS_SELECTOR, '.network_item:nth-child(3) h3') 
    GET_STARTED_CARD3_DESC_FIELD = (By.CSS_SELECTOR, '.network_item:nth-child(3) p') 
    GET_STARTED_CARD3_LINK = (By.CSS_SELECTOR, '.network_item:nth-child(3) a') 
    GET_STARTED_CARD3_IMG_FIELD = (By.CSS_SELECTOR, '.network_item:nth-child(3) .network_item-img img') 


    # join telegram section 
    # JOIN_TELEGRAM_TITLE_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[9]/div/h2') 
    # JOIN_TELEGRAM_DESC_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[9]/div/p') 
    JOIN_TELEGRAM_BTN_LINK_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[9]/div/a') 

