from selenium.webdriver.common.by import By


class AboutPageLocators:

    # landing section
    LANDING_TITLE_FIELD = (By.CSS_SELECTOR, 'section.header_section.about > div > div > div > div > h1')
    LANDING_DESC_FIELD = (By.CSS_SELECTOR, 'section.header_section.about > div > div > div > div > p')
    LANDING_BTN_FIELD = (By.CSS_SELECTOR, 'section.header_section.about > div > div > div > div > a')
    LANDING_SECTION_FIELD = (By.CSS_SELECTOR, 'section.header_section.about')
   
    # Appeared on
    APPEARED_ON_TITLE_FIELD = (By.CSS_SELECTOR, 'section.listed-on > div > h2')
    APPEARED_ON_BITCOINIST_FIELD = (By.CSS_SELECTOR, 'section.listed-on > div > div > div:nth-child(1) > a')
    APPEARED_ON_LIVE_BITCOIN_NEWS_FIELD = (By.CSS_SELECTOR, 'section.listed-on > div > div > div:nth-child(2) > a')
    APPEARED_ON_NEWSBTC_1_FIELD = (By.CSS_SELECTOR, 'section.listed-on > div > div > div:nth-child(3) > a')
    APPEARED_ON_DIGITAL_JOURNAL_FIELD = (By.CSS_SELECTOR, 'section.listed-on > div > div > div:nth-child(4) > a')
    APPEARED_ON_MARKRT_WATCH_FIELD = (By.CSS_SELECTOR, 'section.listed-on > div > div > div:nth-child(5) > a')
    APPEARED_ON_INVESTING_LINK_FIELD = (By.CSS_SELECTOR, 'section.listed-on > div > div > div:nth-child(6) > a')
    APPEARED_ON_BLOCKONOMI_FIELD = (By.CSS_SELECTOR, 'section.listed-on > div > div > div:nth-child(7) > a')
    APPEARED_ON_BENZINGA_FIELD = (By.CSS_SELECTOR, 'section.listed-on > div > div > div:nth-child(8) > a')
    APPEARED_ON_YAHOO_FINANCE_FIELD = (By.CSS_SELECTOR, 'section.listed-on > div > div > div:nth-child(9) > a')
    APPEARED_ON_CRYPTO_DAILY_FIELD = (By.CSS_SELECTOR, 'section.listed-on > div > div > div:nth-child(10) > a')
    APPEARED_ON_NEWSBTC_2_FIELD = (By.CSS_SELECTOR, 'section.listed-on > div > div > div:nth-child(11) > a')
    APPEARED_ON_U_TODAY_FIELD = (By.CSS_SELECTOR, 'section.listed-on > div > div > div:nth-child(12) > a')
    APPEARED_ON_CRYPTO_POTATO_FIELD = (By.CSS_SELECTOR, 'section.listed-on > div > div > div:nth-child(13) > a')
    APPEARED_ON_CRYPTONEWS_FIELD = (By.CSS_SELECTOR, 'section.listed-on > div > div > div:nth-child(14) > a')
    
    # Our mission
    OUR_MISSION_TITLE_FIELD = (By.CSS_SELECTOR, 'section.mission-section.container > h2')
    OUR_MISSION_CARD1_DESC_FIELD = (By.CSS_SELECTOR, 'section.mission-section.container > div > div:nth-child(1) > p')
    OUR_MISSION_CARD1_IMG_FIELD = (By.CSS_SELECTOR, 'section.mission-section.container > div > div:nth-child(1) > img')
    OUR_MISSION_CARD2_DESC_FIELD = (By.CSS_SELECTOR, 'section.mission-section.container > div > div:nth-child(2) > p')
    OUR_MISSION_CARD2_IMG_FIELD = (By.CSS_SELECTOR, 'section.mission-section.container > div > div:nth-child(2) > img')
    OUR_MISSION_CARD3_DESC_FIELD = (By.CSS_SELECTOR, 'section.mission-section.container > div > div:nth-child(3) > p')
    OUR_MISSION_CARD3_IMG_FIELD = (By.CSS_SELECTOR, 'section.mission-section.container > div > div:nth-child(3) > img')
    OUR_MISSION_CARD4_DESC_FIELD = (By.CSS_SELECTOR, 'section.mission-section.container > div > div:nth-child(4) > p')
    OUR_MISSION_CARD4_IMG_FIELD = (By.CSS_SELECTOR, 'section.mission-section.container > div > div:nth-child(4) > img')

    # DAO section
    DAO_TITLE_FIELD = (By.CSS_SELECTOR, 'section.dao_section > div > h2')
    DAO_DESC1_FIELD = (By.CSS_SELECTOR, 'section.dao_section > div > div > div > p:nth-child(1)')
    DAO_DESC2_FIELD = (By.CSS_SELECTOR, 'section.dao_section > div > div > div > p:nth-child(2)')
    DAO_DESC3_FIELD = (By.CSS_SELECTOR, 'section.dao_section > div > div > div > p:nth-child(3)')
    DAO_SECTION_FIELD = (By.CSS_SELECTOR, 'section.dao_section')

    # Team section
    TEAM_TITLE_FIELD = (By.CSS_SELECTOR, 'section.team_section > div > h2')
    TEAM_DESC_FIELD = (By.CSS_SELECTOR, 'section.team_section > div > div > p')

    TEAM_CARD1_IMG_FIELD = (By.CSS_SELECTOR, 'section.team_section > div > div > div:nth-child(1) > img')
    TEAM_CARD1_NAME_FIELD = (By.CSS_SELECTOR, 'section.team_section > div > div > div:nth-child(1) > div > h4')
    TEAM_CARD1_POSITION_FIELD = (By.CSS_SELECTOR, 'section.team_section > div > div > div:nth-child(1) > div > p')
    
    TEAM_CARD2_IMG_FIELD = (By.CSS_SELECTOR, 'section.team_section > div > div > div:nth-child(2) > img')
    TEAM_CARD2_NAME_FIELD = (By.CSS_SELECTOR, 'section.team_section > div > div > div:nth-child(2) > div > h4')
    TEAM_CARD2_POSITION_FIELD = (By.CSS_SELECTOR, 'section.team_section > div > div > div:nth-child(2) > div > p')
    
    TEAM_CARD3_IMG_FIELD = (By.CSS_SELECTOR, 'section.team_section > div > div > div:nth-child(3) > img')
    TEAM_CARD3_NAME_FIELD = (By.CSS_SELECTOR, 'section.team_section > div > div > div:nth-child(3) > div > h4')
    TEAM_CARD3_POSITION_FIELD = (By.CSS_SELECTOR, 'section.team_section > div > div > div:nth-child(3) > div > p')
    
    TEAM_CARD4_IMG_FIELD = (By.CSS_SELECTOR, 'section.team_section > div > div > div:nth-child(4) > img')
    TEAM_CARD4_NAME_FIELD = (By.CSS_SELECTOR, 'section.team_section > div > div > div:nth-child(4) > div > h4')
    TEAM_CARD4_POSITION_FIELD = (By.CSS_SELECTOR, 'section.team_section > div > div > div:nth-child(4) > div > p')
    TEAM_CARD4_FIELD = (By.CSS_SELECTOR, 'section.team_section > div > div > div:nth-child(4)')
    
    
    # ux/ui section
    UX_UI_TITLE_FIELD = (By.CSS_SELECTOR, 'section.team-info.py-5 > h3')
   
    UX_UI_CARD1_IMG_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[6]/div/div/div/div/div[1]/div/div/div/div/img')
    UX_UI_CARD1_NAME_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[6]/div/div/div/div/div[1]/div/div/div/div/div/h4')
    UX_UI_CARD1_POSITION_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[6]/div/div/div/div/div[1]/div/div/div/div/div/p')
    UX_UI_CARD1_DESC_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[6]/div/div/div/div/div[1]/div/div/div/p')
    
    UX_UI_CARD2_IMG_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[6]/div/div/div/div/div[2]/div/div/div/div/img')
    UX_UI_CARD2_NAME_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[6]/div/div/div/div/div[2]/div/div/div/div/div/h4')
    UX_UI_CARD2_POSITION_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[6]/div/div/div/div/div[2]/div/div/div/div/div/p')
    UX_UI_CARD2_DESC_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[6]/div/div/div/div/div[2]/div/div/div/p')
        
    UX_UI_CARD3_IMG_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[6]/div/div/div/div/div[3]/div/div/div/div/img')
    UX_UI_CARD3_NAME_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[6]/div/div/div/div/div[3]/div/div/div/div/div/h4')
    UX_UI_CARD3_POSITION_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[6]/div/div/div/div/div[3]/div/div/div/div/div/p')
    UX_UI_CARD3_DESC_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[2]/section[6]/div/div/div/div/div[3]/div/div/div/p')
    

    # tokenomics section
    TOKENOMICS_TITLE_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section > div > div > h2')
    TOKENOMICS_DESC_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section> div > div > h4')
    TOKENOMICS_LOGO_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section > div > div > h4 > img')
    TOKENOMICS_DESC_SPAN_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section> div > div > h4 span')
    TOKENOMICS_BG_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section.row > div.tokenomics-img')
    
    SUPPLY_SLIDE1_NUM_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section> div > div > div > div > div:nth-child(1) > h4')
    SUPPLY_SLIDE1_TITLE_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section > div > div > div > div > div:nth-child(1) > div > h4.supply-slide_item-title')
    SUPPLY_SLIDE1_PERCENT_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section.row > div > div > div > div > div:nth-child(1) > div > h4.supply-slide_item-percent')
    
    SUPPLY_SLIDE2_NUM_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section> div > div > div > div > div:nth-child(2) > h4')
    SUPPLY_SLIDE2_TITLE_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section > div > div > div > div > div:nth-child(2) > div > h4.supply-slide_item-title')
    SUPPLY_SLIDE2_PERCENT_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section.row > div > div > div > div > div:nth-child(2) > div > h4.supply-slide_item-percent')
    
    SUPPLY_SLIDE3_NUM_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section> div > div > div > div > div:nth-child(3) > h4')
    SUPPLY_SLIDE3_TITLE_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section > div > div > div > div > div:nth-child(3) > div > h4.supply-slide_item-title')
    SUPPLY_SLIDE3_PERCENT_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section.row > div > div > div > div > div:nth-child(3) > div > h4.supply-slide_item-percent')

    SUPPLY_SLIDE4_NUM_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section> div > div > div > div > div:nth-child(4) > h4')
    SUPPLY_SLIDE4_TITLE_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section > div > div > div > div > div:nth-child(4) > div > h4.supply-slide_item-title')
    SUPPLY_SLIDE4_PERCENT_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section.row > div > div > div > div > div:nth-child(4) > div > h4.supply-slide_item-percent')

    SUPPLY_SLIDE5_NUM_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section> div > div > div > div > div:nth-child(5) > h4')
    SUPPLY_SLIDE5_TITLE_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section > div > div > div > div > div:nth-child(5) > div > h4.supply-slide_item-title')
    SUPPLY_SLIDE5_PERCENT_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section.row > div > div > div > div > div:nth-child(5) > div > h4.supply-slide_item-percent')

    SUPPLY_SLIDE6_NUM_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section> div > div > div > div > div:nth-child(6) > h4')
    SUPPLY_SLIDE6_TITLE_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section > div > div > div > div > div:nth-child(6) > div > h4.supply-slide_item-title')
    SUPPLY_SLIDE6_PERCENT_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section.row > div > div > div > div > div:nth-child(6) > div > h4.supply-slide_item-percent')

    SUPPLY_SLIDE7_NUM_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section> div > div > div > div > div:nth-child(7) > h4')
    SUPPLY_SLIDE7_TITLE_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section > div > div > div > div > div:nth-child(7) > div > h4.supply-slide_item-title')
    SUPPLY_SLIDE7_PERCENT_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section.row > div > div > div > div > div:nth-child(7) > div > h4.supply-slide_item-percent')
    
    SUPPLY_SLIDE8_NUM_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section> div > div > div > div > div:nth-child(8) > h4')
    SUPPLY_SLIDE8_TITLE_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section > div > div > div > div > div:nth-child(8) > div > h4.supply-slide_item-title')
    SUPPLY_SLIDE8_PERCENT_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section.row > div > div > div > div > div:nth-child(8) > div > h4.supply-slide_item-percent')
    
    SUPPLY_SLIDE9_NUM_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section> div > div > div > div > div:nth-child(9) > h4')
    SUPPLY_SLIDE9_TITLE_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section > div > div > div > div > div:nth-child(9) > div > h4.supply-slide_item-title')
    SUPPLY_SLIDE9_PERCENT_FIELD = (By.CSS_SELECTOR, 'section.tokenomics_section.row > div > div > div > div > div:nth-child(9) > div > h4.supply-slide_item-percent')


    # more section
    MORE_TITLE_FIELD = (By.CSS_SELECTOR, 'section.more_section > h2')

    GUIDE_TITLE_FIELD = (By.CSS_SELECTOR, 'section.more_section > div > div:nth-child(1) > div.guide > h3')
    GUIDE_DESC_FIELD = (By.CSS_SELECTOR, 'section.more_section > div > div:nth-child(1) > div.guide > p')
    GUIDE_LINK_FIELD = (By.CSS_SELECTOR, 'section.more_section > div > div:nth-child(1) > div.guide > a')
   
    TWITTER_TITLE_FIELD = (By.CSS_SELECTOR, 'section.more_section > div > div:nth-child(1) > div.twitter > h3')
    TWITTER_DESC_FIELD = (By.CSS_SELECTOR, 'section.more_section > div > div:nth-child(1) > div.twitter > p')
    TWITTER_LINK_FIELD = (By.CSS_SELECTOR, 'section.more_section > div > div:nth-child(1) > div.twitter > a')

    TELEGRAM_TITLE_FIELD = (By.CSS_SELECTOR, 'section.more_section > div > div:nth-child(2) > div.telegrem > h3')
    TELEGRAM_DESC_FIELD = (By.CSS_SELECTOR, 'section.more_section > div > div:nth-child(2) > div.telegrem > p')
    TELEGRAM_LINK_FIELD = (By.CSS_SELECTOR, 'section.more_section > div > div:nth-child(2) > div.telegrem > a')

    BLOG_TITLE_FIELD = (By.CSS_SELECTOR, 'section.more_section > div > div:nth-child(3) > div.guide > h3')
    BLOG_DESC_FIELD = (By.CSS_SELECTOR, 'section.more_section > div > div:nth-child(3) > div.guide > p')
    BLOG_LINK_FIELD = (By.CSS_SELECTOR, 'section.more_section > div > div:nth-child(3) > div.guide > a')

    SUPPORT_TITLE_FIELD = (By.CSS_SELECTOR, 'section.more_section > div > div:nth-child(3) > div.support > h3')
    SUPPORT_DESC_FIELD = (By.CSS_SELECTOR, 'section.more_section > div > div:nth-child(3) > div.support > p')
    SUPPORT_LINK_FIELD = (By.CSS_SELECTOR, 'section.more_section > div > div:nth-child(3) > div.support > a')
