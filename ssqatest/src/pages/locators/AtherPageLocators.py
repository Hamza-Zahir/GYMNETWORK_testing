from selenium.webdriver.common.by import By


class AtherPageLocators:
    
    # BscScan page:
    SEARCH_INPUT_FIELD = (By.ID, 'txtSearchInput')
    MAIN_ADDRESS_FIELD = (By.ID, 'mainaddress')
    
    # poocoin page:
    POOCOIN_LOGO_FIELD = (By.XPATH, '//*[@id="root"]/nav/div/div/div[1]/a[1]/img')

    # DEXTools page:
    DEX_TOOLS_LOGO_FIELD = (By.XPATH, '//*[@id="main-logo"]/a/img')

    # Whitepaper page: 
    WHITE_PAPER_TITLE = (By.XPATH, '//*[@id="title"]')

    # Support page: 
    CUSTOMER_SUPPORT_PAPER_TITLE = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/main/div[1]/div/div/div[1]/div[2]/h1')

    # marketwatch.com page
    MARKETWATCH_DESC_FIELD = (By.CSS_SELECTOR, 'section.container > div > div > h3')

    # crypto.news page
    CRYPTO_LOGO_TEXT = (By.CSS_SELECTOR, '#header > div.header__main > a > span')

    # benzinga.com page
    BENZINGA_TITLE_TEXT = (By.XPATH, '//*[@id="__next"]/div[3]/div/div[2]/div[1]/div/h1')


