from selenium.webdriver.common.by import By


class EcoSystemPageLocators:


    # landing section
    LANDING_TITLE_FIELD = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(2) > section.header_section.ecosystem > div > div > div > div > h1')
    LANDING_DESC_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div/div/p')
    LANDING_BTN_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div/div/a')
    LANDING_SECTION_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]')
    

    # gym-network section
    GYM_NETWORK_TITLE_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > h2')
    GYM_NETWORK_DESC_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > h4')

    GYM_NETWORK_CARD1_NUM_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(1) > div > div > h2') 
    GYM_NETWORK_CARD1_TITLE_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(1) > div > div > h3') 
    GYM_NETWORK_CARD1_DESC_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(1) > div > div > p') 
    GYM_NETWORK_CARD1_LINK = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(1) > div > div > a') 
    GYM_NETWORK_CARD1_IMG_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(1) > div > img') 

    GYM_NETWORK_CARD2_NUM_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(2) > div > div > h2') 
    GYM_NETWORK_CARD2_TITLE_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(2) > div > div > h3') 
    GYM_NETWORK_CARD2_DESC_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(2) > div > div > p') 
    GYM_NETWORK_CARD2_LINK = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(2) > div > div > a') 
    GYM_NETWORK_CARD2_IMG_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(2) > div > img') 

    GYM_NETWORK_CARD3_NUM_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(3) > div > div > h2') 
    GYM_NETWORK_CARD3_TITLE_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(3) > div > div > h3') 
    GYM_NETWORK_CARD3_DESC_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(3) > div > div > p') 
    GYM_NETWORK_CARD3_LINK = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(3) > div > div > div') 
    GYM_NETWORK_CARD3_IMG_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(3) > div > img') 

    GYM_NETWORK_CARD4_NUM_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(4) > div > div > h2') 
    GYM_NETWORK_CARD4_TITLE_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(4) > div > div > h3') 
    GYM_NETWORK_CARD4_DESC_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(4) > div > div > p') 
    GYM_NETWORK_CARD4_LINK = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(4) > div > div > div') 
    GYM_NETWORK_CARD4_IMG_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(4) > div > img') 

    GYM_NETWORK_CARD5_NUM_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(5) > div > div > h2') 
    GYM_NETWORK_CARD5_TITLE_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(5) > div > div > h3') 
    GYM_NETWORK_CARD5_DESC_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(5) > div > div > p') 
    GYM_NETWORK_CARD5_LINK = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(5) > div > div > a') 
    GYM_NETWORK_CARD5_IMG_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(5) > div > img') 

    GYM_NETWORK_CARD6_NUM_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(6) > div > div > h2') 
    GYM_NETWORK_CARD6_TITLE_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(6) > div > div > h3') 
    GYM_NETWORK_CARD6_DESC_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(6) > div > div > p') 
    GYM_NETWORK_CARD6_LINK = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(6) > div > div > div') 
    GYM_NETWORK_CARD6_IMG_FIELD = (By.CSS_SELECTOR, 'section.gym-network > div > div > div > div:nth-child(6) > div > img') 


    # get started section
    GET_STARTED_TITLE_FIELD = (By.CSS_SELECTOR, 'section.get-started-with.container > h2') 

    GET_STARTED_CARD1_NUM_FIELD = (By.CSS_SELECTOR, 'section.get-started-with.container > div > div:nth-child(1) > h3') 
    GET_STARTED_CARD1_TITLE_FIELD = (By.CSS_SELECTOR, 'section.get-started-with.container > div > div:nth-child(1) > h4') 
    GET_STARTED_CARD1_DESC_FIELD = (By.CSS_SELECTOR, 'section.get-started-with.container > div > div:nth-child(1) > p') 
    GET_STARTED_CARD1_LINK = (By.CSS_SELECTOR, 'section.get-started-with.container > div > div:nth-child(1) > a') 
    GET_STARTED_CARD1_IMG_FIELD = (By.CSS_SELECTOR, 'section.get-started-with.container > div > div:nth-child(1) > img') 

    GET_STARTED_CARD2_NUM_FIELD = (By.CSS_SELECTOR, 'section.get-started-with.container > div > div:nth-child(2) > h3') 
    GET_STARTED_CARD2_TITLE_FIELD = (By.CSS_SELECTOR, 'section.get-started-with.container > div > div:nth-child(2) > h4') 
    GET_STARTED_CARD2_DESC_FIELD = (By.CSS_SELECTOR, 'section.get-started-with.container > div > div:nth-child(2) > p') 
    GET_STARTED_CARD2_LINK = (By.CSS_SELECTOR, 'section.get-started-with.container > div > div:nth-child(2) > a') 

    GET_STARTED_CARD3_NUM_FIELD = (By.CSS_SELECTOR, 'section.get-started-with.container > div > div:nth-child(3) > h3') 
    GET_STARTED_CARD3_TITLE_FIELD = (By.CSS_SELECTOR, 'section.get-started-with.container > div > div:nth-child(3) > h4') 
    GET_STARTED_CARD3_DESC_FIELD = (By.CSS_SELECTOR, 'section.get-started-with.container > div > div:nth-child(3) > p') 
    GET_STARTED_CARD3_LINK = (By.CSS_SELECTOR, 'section.get-started-with.container > div > div:nth-child(3) > a') 
    
    START_DIRECTLY_BTN = (By.CSS_SELECTOR, 'section.get-started-with.container > a > button') 
   


    #################### carousel section ####################
    # carousel_section-menu
    GYMSTREET_link = (By.CSS_SELECTOR, 'section.carousel_section > div > ul > li:nth-child(1) > a')
    METABLOCKS_link = (By.CSS_SELECTOR, 'section.carousel_section > div > ul > li:nth-child(2) > a')
    CASH_FT_link = (By.CSS_SELECTOR, 'section.carousel_section > div > ul > li:nth-child(3) > a')
    ZUCKERLAND_link = (By.CSS_SELECTOR, 'section.carousel_section > div > ul > li:nth-child(4) > a')
    GYM_DEX_link = (By.CSS_SELECTOR, 'section.carousel_section > div > ul > li:nth-child(5) > a')
    METAVERSE_link = (By.CSS_SELECTOR, 'section.carousel_section > div > ul > li:nth-child(6) > a')


    # gymstreet section 
    GYMSTREET_TITLE = (By.CSS_SELECTOR, '#gymstreet > div > h2')
    GYMSTREET_DESC1 = (By.CSS_SELECTOR, '#gymstreet > div > p:nth-child(4)')
    GYMSTREET_DESC2 = (By.CSS_SELECTOR, '#gymstreet > div > p:nth-child(5)')
    GYMSTREET_DESC3 = (By.CSS_SELECTOR, '#gymstreet > div > p:nth-child(6)')
    GYMSTREET_DESC4 = (By.CSS_SELECTOR, '#gymstreet > div > p:nth-child(7)')
    GYMSTREET_BTN = (By.CSS_SELECTOR, '#gymstreet > div > button > a')
    GYMSTREET_IMG = (By.CSS_SELECTOR, '#gymstreet > img')
   
    # metablocks section 
    METABLOCKS_TITLE = (By.CSS_SELECTOR, '#metablocks > div > h2')
    METABLOCKS_DESC1 = (By.CSS_SELECTOR, '#metablocks > div > p:nth-child(4)')
    METABLOCKS_DESC2 = (By.CSS_SELECTOR, '#metablocks > div > p:nth-child(5)')
    METABLOCKS_DESC3 = (By.CSS_SELECTOR, '#metablocks > div > p:nth-child(6)')
    METABLOCKS_BTN = (By.CSS_SELECTOR, '#metablocks > div > button')
    METABLOCKS_IMG = (By.CSS_SELECTOR, '#metablocks > img')
   
   
    # CashFT section
    CASH_FT_TITLE = (By.CSS_SELECTOR, '#cashft > div > h2')
    CASH_FT_DESC1 = (By.CSS_SELECTOR, '#cashft > div > p:nth-child(4)')
    CASH_FT_LI1 = (By.CSS_SELECTOR, '#cashft > div > ul > li:nth-child(1)')
    CASH_FT_LI2 = (By.CSS_SELECTOR, '#cashft > div > ul > li:nth-child(2)')
    CASH_FT_LI3 = (By.CSS_SELECTOR, '#cashft > div > ul > li:nth-child(3)')
    CASH_FT_LI4 = (By.CSS_SELECTOR, '#cashft > div > ul > li:nth-child(4)')
    CASH_FT_DESC2 = (By.CSS_SELECTOR, '#cashft > div > p:nth-child(6)')
    CASH_FT_BTN = (By.CSS_SELECTOR, '#cashft > div > button')
    CASH_FT_IMG = (By.CSS_SELECTOR, '#cashft > img')
   

    # zuckerland section 
    ZUCKERLAND_TITLE = (By.CSS_SELECTOR, '#zuckerland > div > h2')
    ZUCKERLAND_DESC1 = (By.CSS_SELECTOR, '#zuckerland > div > p:nth-child(4)')
    ZUCKERLAND_DESC2 = (By.CSS_SELECTOR, '#zuckerland > div > p:nth-child(5)')
    ZUCKERLAND_DESC3 = (By.CSS_SELECTOR, '#zuckerland > div > p:nth-child(6)')
    ZUCKERLAND_BTN = (By.CSS_SELECTOR, '#zuckerland > div > button')
    ZUCKERLAND_IMG = (By.CSS_SELECTOR, '#zuckerland > img')

    # Gym Dex section
    GYM_DEX_TITLE = (By.CSS_SELECTOR, '#gymdex > div > h2')
    GYM_DEX_DESC = (By.CSS_SELECTOR, '#gymdex > div > p.carousel_section-item__desc')
    GYM_DEX_BTN = (By.CSS_SELECTOR, '#gymdex > div > a')
    GYM_DEX_IMG = (By.CSS_SELECTOR, '#gymdex > img')

    # metaverse-campus section 
    METAVERSE_CAMPUS_TITLE = (By.CSS_SELECTOR, '#metaverse-campus > div > h2')
    METAVERSE_CAMPUS_DESC1 = (By.CSS_SELECTOR, '#metaverse-campus > div > p:nth-child(4)')
    METAVERSE_CAMPUS_DESC2 = (By.CSS_SELECTOR, '#metaverse-campus > div > p:nth-child(5)')
    METAVERSE_CAMPUS_DESC3 = (By.CSS_SELECTOR, '#metaverse-campus > div > p:nth-child(6)')
    METAVERSE_CAMPUS_BTN = (By.CSS_SELECTOR, '#metaverse-campus > div > button')
    METAVERSE_CAMPUS_IMG = (By.CSS_SELECTOR, '#metaverse-campus > img')


