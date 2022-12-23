from selenium.webdriver.common.by import By


class HomePageLocators:
    
    # contract address section
    CONTRACT_LOGO = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div[1]/img')
    CONTRACT_ADDRESS = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div')
    CONTRACT_SYMPOL = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div[1]/span')
    COPY_ADDRESS_BTN_FIELD = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div[3]')

    # audited section
    AUDITED_SECTION = (By.CLASS_NAME, 'audited-section')
    AUDITED_SECTION_CLOSE_BTN = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[2]/img')

    CERTIK_IMG = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/div[1]/a/img') 
    CERTIK_LINK = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/div[1]/a') 
    PECKSHIELD_IMG = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/a/img') 
    PECKSHIELD_LINK = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/div[2]/a') 
    TELEGRAM_IMG = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/div[3]/a/img') 
    TELEGRAM_LINK = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/div[3]/a') 
    ALPACA_FINANCE_IMG = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/div[4]/a/img') 
    ALPACA_FINANCE_LINK = (By.XPATH, '//*[@id="__layout"]/div/div[2]/div[1]/div/div[4]/a') 
   
    
    # header
    LOGO_FIELD = (By.XPATH, '//*[@id="__layout"]/div/main/header/nav/div/div/a/img')
    HOME_LINK_FIELD = (By.XPATH, '//*[@id="__layout"]/div/main/header/nav/div/div/a')
    PRODUCTS_LINK_FIELD = (By.XPATH, '//*[@id="navbarText"]/ul/li[1]/a')
    ECO_SYSTEM_LINK_FIELD = (By.XPATH, '//*[@id="navbarText"]/ul/li[2]/a')
    ABOUT_LINK_FIELD = (By.XPATH, '//*[@id="navbarText"]/ul/li[3]/a')
    BLOG_LINK_FIELD = (By.XPATH, '//*[@id="navbarText"]/ul/li[4]/a')
    LAUNCH_LINK_FIELD = (By.XPATH, '//*[@id="navbarText"]/div/a')
    CUSTOM_SELECT_FIELD = (By.CSS_SELECTOR, '#navbarText > div > div > div > button')
    CHINESE_LINK_FIELD = (By.CSS_SELECTOR, '#navbarText > div > div > div > div > ul > li:nth-child(9)')
    
    # landing section
    LAUNCH_APP_BTN = (By.XPATH, '//header/div/div/div/div[1]/a') 
    Header_TITLE_FIELD = (By.CLASS_NAME, 'header-info_title')
    Header_LANDING_DESC_FIELD = (By.XPATH, '//*[@id="__layout"]/div/main/header/div/div/div/div[1]/p')
    HEADER_BG_IMG_FIELD = (By.XPATH, '//*[@id="__layout"]/div/main/header/div')


    # listed On section
    LISTED_ON_TITLE_FIELD = (By.CSS_SELECTOR, '#listedOn > div > h2') 
    CRYPTO_LINK_FIELD = (By.CSS_SELECTOR, '#listedOn > div > div > div:nth-child(1) > a') 
    CRYPTO_IMG_FIELD = (By.CSS_SELECTOR, '#listedOn > div > div > div:nth-child(1) > a > img') 
    COIN_GECKO_LINK_FIELD = (By.CSS_SELECTOR, '#listedOn > div > div > div:nth-child(2) > a') 
    COIN_GECKO_IMG_FIELD = (By.CSS_SELECTOR, '#listedOn > div > div > div:nth-child(2) > a > img') 
    PANCAKESWAP_LINK_FIELD = (By.CSS_SELECTOR, '#listedOn > div > div > div:nth-child(3) > a') 
    PANCAKESWAP_IMG_FIELD = (By.CSS_SELECTOR, '#listedOn > div > div > div:nth-child(3) > a > img') 
    BINANCE_LINK_FIELD = (By.CSS_SELECTOR, '#listedOn > div > div > div:nth-child(4) > a') 
    BINANCE_IMG_FIELD = (By.CSS_SELECTOR, '#listedOn > div > div > div:nth-child(4) > a > img') 
    COINBASE_LINK_FIELD = (By.CSS_SELECTOR, '#listedOn > div > div > div:nth-child(5) > a') 
    COINBASE_IMG_FIELD = (By.CSS_SELECTOR, '#listedOn > div > div > div:nth-child(5) > a > img') 
    LIVE_COIN_WATCH_LINK_FIELD = (By.CSS_SELECTOR, '#listedOn > div > div > div:nth-child(6) > a') 
    LIVE_COIN_WATCH_IMG_FIELD = (By.CSS_SELECTOR, '#listedOn > div > div > div:nth-child(6) > a > img') 
    POO_COIN_CHARTS_LINK_FIELD = (By.CSS_SELECTOR, '#listedOn > div > div > div:nth-child(7) > a') 
    POO_COIN_CHARTS_IMG_FIELD = (By.CSS_SELECTOR, '#listedOn > div > div > div:nth-child(7) > a > img') 
    DEXTOOLS_LINK_FIELD = (By.CSS_SELECTOR, '#listedOn > div > div > div:nth-child(8) > a') 
    DEXTOOLS_IMG_FIELD = (By.CSS_SELECTOR, '#listedOn > div > div > div:nth-child(8) > a > img') 

    # investment System section
    INVESTMENT_SYSTEM_TITLE_FIELD = (By.CSS_SELECTOR, '#investmentSystem > div.container-lg > div > h2') 
    INVESTMENT_SYSTEM_DESC_FIELD = (By.CSS_SELECTOR, '#investmentSystem > div.investment-system_bg > div > div > p') 
    GO_TO_PRODUCTS_LINK = (By.CSS_SELECTOR, '#investmentSystem > div.investment-system_bg > div > div > a')
    INVESTMENT_SYSTEM_BG_FIELD =  (By.CSS_SELECTOR, '#investmentSystem > div.investment-system_bg') 

    # GYM Street section
    GYM_STREET_TITLE_FIELD = (By.CSS_SELECTOR, '#GYMStreet > div > h2') 
    GYM_STREET_DESC_FIELD = (By.CSS_SELECTOR, '#GYMStreet > div > p') 
    GYM_STREET_LINK = (By.CSS_SELECTOR, '#GYMStreet > div > a')

    # exchange-crypto section
    EXCHANGE_CRYPTO_TITLE_FIELD = (By.CSS_SELECTOR, '#exchange-crypto > div > div > div > h2') 
    EXCHANGE_CRYPTO_IMG_FIELD = (By.CSS_SELECTOR, '#exchange-crypto > div > div > div > img') 

    # Metaverse section
    METAVERSE_DESC_FIELD = (By.CSS_SELECTOR, '#metavese > div > div > div.col-sm-6.col-12.d-flex.align-items-center > p') 
    METAVERSE_IMG_FIELD = (By.CSS_SELECTOR, '#metavese > div > div > div.col-sm-6.col-12.metavese-img > img') 
    METAVERSE_BG_FIELD =  (By.ID, 'metavese') 

    # ivendpay section
    IVENDPAY_TITLE_FIELD = (By.CSS_SELECTOR, '#ivendpay > div > h1') 
    IVENDPAY_CARD1_TITLE_FIELD = (By.CSS_SELECTOR, '#ivendpay > div > div > div:nth-child(1) > div.ivendpay-card-info > div') 
    IVENDPAY_CARD1_IMG_FIELD = (By.CSS_SELECTOR, '#ivendpay > div > div > div:nth-child(1) > div.ivendpay-card-img > img') 
    IVENDPAY_CARD2_TITLE_FIELD = (By.CSS_SELECTOR, '#ivendpay > div > div > div:nth-child(2) > div.ivendpay-card-info > div.ivendpay-card-info--title') 
    IVENDPAY_CARD2_DESC_FIELD = (By.CSS_SELECTOR, '#ivendpay > div > div > div:nth-child(2) > div.ivendpay-card-info > div.ivendpay-card-info--text') 
    IVENDPAY_CARD2_IMG_FIELD = (By.CSS_SELECTOR, '#ivendpay > div > div > div:nth-child(2) > div.ivendpay-card-img > img') 
    IVENDPAY_CARD2_LINK_FIELD = (By.CSS_SELECTOR, '#ivendpay > div > div > div:nth-child(2) > div.ivendpay-card-info > a') 
    IVENDPAY_CARD3_TITLE_FIELD = (By.CSS_SELECTOR, '#ivendpay > div > div > div:nth-child(3) > div.ivendpay-card-info > div.ivendpay-card-info--title') 
    IVENDPAY_CARD3_DESC_FIELD = (By.CSS_SELECTOR, '#ivendpay > div > div > div:nth-child(3) > div.ivendpay-card-info > div.ivendpay-card-info--text') 
    IVENDPAY_CARD3_IMG_FIELD = (By.CSS_SELECTOR, '#ivendpay > div > div > div:nth-child(3) > div.ivendpay-card-img > img') 
    IVENDPAY_CARD3_LINK_FIELD = (By.CSS_SELECTOR, '#ivendpay > div > div > div:nth-child(3) > div.ivendpay-card-info > a') 

    # protection-tools section 
    PROTECTION_TOOLD_TITLE_FIELD = (By.CSS_SELECTOR, '#protection-tools > h3') 
    PROTECTION_TOOLD_CARD1_TITLE_FIELD = (By.CSS_SELECTOR, '#protection-tools > div > div:nth-child(1) > div > div > h3') 
    PROTECTION_TOOLD_CARD1_DESC_FIELD = (By.CSS_SELECTOR, '#protection-tools > div > div:nth-child(1) > div > div > p') 
    PROTECTION_TOOLD_CARD1_IMG_FIELD = (By.CSS_SELECTOR, '#protection-tools > div > div:nth-child(1) > div > img') 
    PROTECTION_TOOLD_CARD2_TITLE_FIELD = (By.CSS_SELECTOR, '#protection-tools > div > div:nth-child(2) > div > div > h3') 
    PROTECTION_TOOLD_CARD2_DESC_FIELD = (By.CSS_SELECTOR, '#protection-tools > div > div:nth-child(2) > div > div > p') 
    PROTECTION_TOOLD_CARD2_IMG_FIELD = (By.CSS_SELECTOR, '#protection-tools > div > div:nth-child(2) > div > img') 
    PROTECTION_TOOLD_CARD3_TITLE_FIELD = (By.CSS_SELECTOR, '#protection-tools > div > div:nth-child(3) > div > div > h3') 
    PROTECTION_TOOLD_CARD3_DESC_FIELD = (By.CSS_SELECTOR, '#protection-tools > div > div:nth-child(3) > div > div > p') 
    PROTECTION_TOOLD_CARD3_IMG_FIELD = (By.CSS_SELECTOR, '#protection-tools > div > div:nth-child(3) > div > img') 
    PROTECTION_TOOLD_CARD4_TITLE_FIELD = (By.CSS_SELECTOR, '#protection-tools > div > div:nth-child(4) > div > div > h3') 
    PROTECTION_TOOLD_CARD4_DESC_FIELD = (By.CSS_SELECTOR, '#protection-tools > div > div:nth-child(4) > div > div > p') 
    PROTECTION_TOOLD_CARD4_IMG_FIELD = (By.CSS_SELECTOR, '#protection-tools > div > div:nth-child(4) > div > img') 


    # get started section
    GET_STARTED_TITLE_FIELD = (By.CSS_SELECTOR, '#GYMNetwork > div > div > h2') 
    GET_STARTED_CARD1_NUM_FIELD = (By.CSS_SELECTOR, '#GYMNetwork > div > div > div > div:nth-child(1) > a > div.network_item-card > div > h2') 
    GET_STARTED_CARD1_TITLE_FIELD = (By.CSS_SELECTOR, '#GYMNetwork > div > div > div > div:nth-child(1) > a > div.network_item-card > div > h3') 
    GET_STARTED_CARD1_DESC_FIELD = (By.CSS_SELECTOR, '#GYMNetwork > div > div > div > div:nth-child(1) > a > div.network_item-card > div > p') 
    GET_STARTED_CARD1_LINK = (By.CSS_SELECTOR, '#GYMNetwork > div > div > div > div:nth-child(1) > a') 
    GET_STARTED_CARD1_IMG_FIELD = (By.CSS_SELECTOR, '#GYMNetwork > div > div > div > div:nth-child(1) > a > div.network_item-img > img') 
    GET_STARTED_CARD2_NUM_FIELD = (By.CSS_SELECTOR, '#GYMNetwork > div > div > div > div:nth-child(2) > a > div.network_item-card > div > h2') 
    GET_STARTED_CARD2_TITLE_FIELD = (By.CSS_SELECTOR, '#GYMNetwork > div > div > div > div:nth-child(2) > a > div.network_item-card > div > h3') 
    GET_STARTED_CARD2_DESC_FIELD = (By.CSS_SELECTOR, '#GYMNetwork > div > div > div > div:nth-child(2) > a > div.network_item-card > div > p') 
    GET_STARTED_CARD2_LINK = (By.CSS_SELECTOR, '#GYMNetwork > div > div > div > div:nth-child(2) > a') 
    GET_STARTED_CARD2_IMG_FIELD = (By.CSS_SELECTOR, '#GYMNetwork > div > div > div > div:nth-child(2) > a > div.network_item-img > img')
    GET_STARTED_CARD3_NUM_FIELD = (By.CSS_SELECTOR, '#GYMNetwork > div > div > div > div:nth-child(3) > a > div.network_item-card > div > h2') 
    GET_STARTED_CARD3_TITLE_FIELD = (By.CSS_SELECTOR, '#GYMNetwork > div > div > div > div:nth-child(3) > a > div.network_item-card > div > h3') 
    GET_STARTED_CARD3_DESC_FIELD = (By.CSS_SELECTOR, '#GYMNetwork > div > div > div > div:nth-child(3) > a > div.network_item-card > div > p') 
    GET_STARTED_CARD3_LINK = (By.CSS_SELECTOR, '#GYMNetwork > div > div > div > div:nth-child(3) > a') 
    GET_STARTED_CARD3_IMG_FIELD = (By.CSS_SELECTOR, '#GYMNetwork > div > div > div > div:nth-child(3) > a > div.network_item-img > img')

    # roadmap section
    ROADMAP_TITLE_FIELD = (By.CSS_SELECTOR, '#roadmap > h2') 
    ROADMAP_DESC_FIELD = (By.CSS_SELECTOR, '#roadmap > p') 

    ROADMAP_CARD1_DATE_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(1) > p.date') 
    ROADMAP_CARD1_TITLE_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(1) > h3') 
    ROADMAP_CARD1_DESC_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(1) > p.landing-desc_small') 
    ROADMAP_CARD1_IMG_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(1) > img') 
    
    ROADMAP_CARD2_DATE_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(2) > p.date') 
    ROADMAP_CARD2_TITLE_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(2) > h3') 
    ROADMAP_CARD2_DESC_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(2) > p.landing-desc_small') 
    ROADMAP_CARD2_IMG_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(2) > img') 

    ROADMAP_CARD3_DATE_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(3) > p.date') 
    ROADMAP_CARD3_TITLE_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(3) > h3') 
    ROADMAP_CARD3_DESC_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(3) > p.landing-desc_small') 
    ROADMAP_CARD3_IMG_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(3) > img') 
    
    ROADMAP_CARD4_DATE_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(4) > p.date') 
    ROADMAP_CARD4_TITLE_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(4) > h3') 
    ROADMAP_CARD4_DESC_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(4) > p.landing-desc_small') 
    ROADMAP_CARD4_IMG_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(4) > img') 

    ROADMAP_CARD5_DATE_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(5) > p.date') 
    ROADMAP_CARD5_TITLE_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(5) > h3') 
    ROADMAP_CARD5_DESC_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(5) > p.landing-desc_small') 
    ROADMAP_CARD5_IMG_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(5) > img') 
    
    ROADMAP_CARD6_DATE_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(6) > p.date') 
    ROADMAP_CARD6_TITLE_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(6) > h3') 
    ROADMAP_CARD6_DESC_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(6) > p.landing-desc_small') 
    ROADMAP_CARD6_IMG_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(6) > img') 

    ROADMAP_CARD7_DATE_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(7) > p.date') 
    ROADMAP_CARD7_TITLE_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(7) > h3') 
    ROADMAP_CARD7_DESC_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(7) > p.landing-desc_small') 
    ROADMAP_CARD7_IMG_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(7) > img') 
    
    ROADMAP_CARD8_DATE_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(8) > p.date') 
    ROADMAP_CARD8_TITLE_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(8) > h3') 
    ROADMAP_CARD8_DESC_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(8) > p.landing-desc_small') 
    ROADMAP_CARD8_IMG_FIELD = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--content > div:nth-child(8) > img') 
    
    ROADMAP_NEXT_BTN = (By.CSS_SELECTOR, '#roadmap > div > div > div.roadmap-slider--arrows > div.roadmap-slider--arrows__item.next')

    # faq section 
    FAQ_TITLE_FIELD = (By.CSS_SELECTOR, '#faq > div > div > div.col-xl-3.col-lg-5.col-12 > h2') 

    WHAT_IS_DEFI_BTN_FIELD = (By.CSS_SELECTOR, '#what_defi0 > button') 
    WHAT_IS_DEFI_ANSWER_FIELD = (By.CSS_SELECTOR, '#what_defi__0 > div') 

    WHAT_ARE_SMART_CONTRACTS_BTN_FIELD = (By.CSS_SELECTOR, '#what_smart_contract1 > button') 
    WHAT_ARE_SMART_CONTRACTS_ANSWER_FIELD = (By.CSS_SELECTOR, '#what_smart_contract__1 > div') 

    WHAT_IS_LIQUIDITY_MINING_BTN_FIELD = (By.CSS_SELECTOR, '#what_liquidity_meaning2 > button') 
    WHAT_IS_LIQUIDITY_MINING_ANSWER_FIELD = (By.CSS_SELECTOR, '#what_liquidity_meaning__2 > div') 

    WHAT_EXACTLY_ARE_LIQUIDITY_POOLS_BTN_FIELD = (By.CSS_SELECTOR, '#what_liquidity_pool3 > button') 
    WHAT_EXACTLY_ARE_LIQUIDITY_POOLS_ANSWER_FIELD = (By.CSS_SELECTOR, '#what_liquidity_pool__3 > div') 

    LEARN_MORE_BTN_FIELD = (By.CSS_SELECTOR, '#accordionFlushExample > button') 

    WHAT_IS_DAO_BTN_FIELD = (By.CSS_SELECTOR, '#what_dao4 > button') 
    WHAT_IS_DAO_ANSWER_FIELD = (By.CSS_SELECTOR, '#what_dao__4 > div') 

    WHAT_IS_DAO_GOVERNANCE_BTN_FIELD = (By.CSS_SELECTOR, '#what_dao_governance5 > button') 
    WHAT_IS_DAO_GOVERNANCE_ANSWER_FIELD = (By.CSS_SELECTOR, '#what_dao_governance__5 > div') 

    HOW_CAN_I_USE_GYM_NETWORK_BTN_FIELD = (By.CSS_SELECTOR, '#how_use_network6 > button') 
    HOW_CAN_I_USE_GYM_NETWORK_ANSWER_FIELD = (By.CSS_SELECTOR, '#how_use_network__6 > div') 

    WHICH_WALLET_USE_TO_CONNECT_BTN_FIELD = (By.CSS_SELECTOR, '#which_wallet_use_to_connect7 > button') 
    WHICH_WALLET_USE_TO_CONNECT_ANSWER_FIELD = (By.CSS_SELECTOR, '#which_wallet_use_to_connect__7 > div') 

    WHAT_IS_APY_APR_BTN_FIELD = (By.CSS_SELECTOR, '#what_apy_apr8 > button') 
    WHAT_IS_APY_APR_ANSWER_FIELD = (By.CSS_SELECTOR, '#what_apy_apr__8 > div') 

    WHERE_REWORDS_VAULTS_COME_FROM_BTN_FIELD = (By.CSS_SELECTOR, '#where_rewords_vaults_come_from9 > button') 
    WHERE_REWORDS_VAULTS_COME_FROM_ANSWER_FIELD = (By.CSS_SELECTOR, '#where_rewords_vaults_come_from__9 > div') 


    WHO_OR_WHAT_IS_ALPACA_BTN_FIELD = (By.CSS_SELECTOR, '#who_what_alpaca10 > button') 
    WHO_OR_WHAT_IS_ALPACA_ANSWER_FIELD = (By.CSS_SELECTOR, '#who_what_alpaca__10 > div') 

    WHAT_IS_BINANCE_BTN_FIELD = (By.CSS_SELECTOR, '#what_binance11 > button') 
    WHAT_IS_BINANCE_ANSWER_FIELD = (By.CSS_SELECTOR, '#what_binance__11 > div') 
    
    WHAT_DO_WITH_GYMNET_FIELD = (By.CSS_SELECTOR, '#what_do_with_gymnet12 > button') 
    WHAT_DO_WITH_GYMNET_ANSWER_FIELD = (By.CSS_SELECTOR, '#what_do_with_gymnet__12 > div') 

    WHERE_GYMNET_TOKEN_LISTED_FIELD = (By.CSS_SELECTOR, '#where_gymnet_lysted13 > button') 
    WHERE_GYMNET_TOKEN_LISTED_ANSWER_FIELD = (By.CSS_SELECTOR, '#where_gymnet_lysted__13 > div') 

    WHER_FIND_TUTORIALS_FIELD = (By.CSS_SELECTOR, '#where_find_tutorials14 > button') 
    WHER_FIND_TUTORIALS_ANSWER_FIELD = (By.CSS_SELECTOR, '#where_find_tutorials__14 > div') 


    HOW_AFFILIATE_WORK_FIELD = (By.CSS_SELECTOR, '#how_affiliate_work15 > button') 
    HOW_AFFILIATE_WORK_ANSWER_FIELD = (By.CSS_SELECTOR, '#how_affiliate_work__15 > div') 

    # # join telegram section 
    # JOIN_TELEGRAM_TITLE_FIELD = (By.CSS_SELECTOR, '#join-group > div > h2') 
    # JOIN_TELEGRAM_DESC_FIELD = (By.CSS_SELECTOR, '#join-group > div > p') 
    # JOIN_TELEGRAM_BTN_LINK_FIELD = (By.CSS_SELECTOR, '#join-group > div > a') 


    # footer section
    FOOTER_LOGO_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div > a') 
    FOOTER_DESC_FIELD = (By.CSS_SELECTOR, 'footer > div > div > div > p') 
    FOOTER_TWITTER_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div > div > a:nth-child(1)') 
    FOOTER_TELEGRAM_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div > div > a:nth-child(2)') 
    FOOTER_PRODUCTS_TITLE_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(3) > h4') 
    FOOTER_PRODUCTS_VULTE_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(3) > ul > li:nth-child(1) > a') 
    FOOTER_PRODUCTS_FARMING_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(3) > ul > li:nth-child(2) > a') 
    FOOTER_PRODUCTS_SINGLE_POOL_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(3) > ul > li:nth-child(3) > a') 
    FOOTER_PRODUCTS_BUY_GYMNET_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(3) > ul > li:nth-child(4) > a') 

    FOOTER_ECO_SYSTEM_TITLE_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(4) > h4') 
    FOOTER_GYMSTREET_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(4) > ul > li:nth-child(1) > a') 
    FOOTER_METABOCKS_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(4) > ul > li:nth-child(2) > a') 
    FOOTER_CASH_FT_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(4) > ul > li:nth-child(3) > a') 
    FOOTER_ZUCKERLAND_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(4) > ul > li:nth-child(4) > a') 
    FOOTER_GYM_DEX_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(4) > ul > li:nth-child(5) > a') 
    FOOTER_METAVERSE_CAMPUS_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(4) > ul > li:nth-child(6) > a') 
    FOOTER_WHITEPAPER_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(4) > ul > li:nth-child(7) > a') 

    FOOTER_ABOUT_TITLE_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(5) > h4') 
    FOOTER_BLOG_NEWS_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(5) > ul > li:nth-child(1) > a') 
    FOOTER_SUPPORT_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(5) > ul > li:nth-child(2) > a') 
    FOOTER_GUIDE_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(5) > ul > li:nth-child(3) > a') 
    FOOTER_TOKEN_CONTRACT_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.row > div:nth-child(5) > ul > li:nth-child(4) > a') 

    FOOTER_INFO_LINK_FIELD = (By.CSS_SELECTOR, 'footer > div > div.footer-info.text-center > a')


