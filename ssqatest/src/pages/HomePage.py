from ssqatest.src.pages.locators.HomePageLocators import HomePageLocators
from ssqatest.src.pages.locators.ProductsPageLocators import ProductsPageLocators
from ssqatest.src.pages.locators.EcoSystemPageLocators import EcoSystemPageLocators
from ssqatest.src.pages.locators.DashboardPageLocators import DashboardPageLocators
from ssqatest.src.pages.locators.AboutPageLocators import AboutPageLocators
from ssqatest.src.pages.locators.BlogPageLocators import BlogPageLocators
from ssqatest.src.pages.locators.AtherPageLocators import AtherPageLocators
from ssqatest.src.pages.locators.global_sections.JoinTelegramLocators import JoinTelegramLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpe.HomeContent import HomeContent
from ssqatest.src.helpe.ProductPageContent import ProductPageContent 
from ssqatest.src.helpe.EcoSystemPageContent import EcoSystemPageContent
from ssqatest.src.helpe.AboutPageContent import AboutPageContent 
from ssqatest.src.helpe.BlogPageContent import BlogPageContent 
from ssqatest.src.helpe.DashboarPageContent import DashboarPageContent 
from ssqatest.src.helpe.AtherPageContent import AtherPageContent
from ssqatest.src.pages.components.JoinTelegramSection import JoinTelegram

class HomePage(HomePageLocators):
    
    def __init__(self, driver):
        self.url = "https://gymnetwork.io/"
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
        self.JoinTelegram_section = JoinTelegram(self.driver, self.url)

    def open_home_page(self):
        self.driver.get(self.url)


    def open_home_page_and_verify_title(self):
        self.driver.get(self.url)
        home_page_title = 'GYM NETWORK - DeFi Aggregator Investment System combining the best yields with high rewards'
        assert self.driver.title == home_page_title
        



    def copy_contract_address_and_verify_if_coped_successfully(self):
        contract_address = '0x0012365F0a1E5F30a5046c680DCB21D07b15FcF7'
        self.sl.wait_and_click(self.COPY_ADDRESS_BTN_FIELD)
        self.driver.switch_to.new_window('tab')
        self.driver.get("https://bscscan.com/")

        self.sl.wait_and_pest_text(AtherPageLocators.SEARCH_INPUT_FIELD)
        self.sl.wait_and_enter(AtherPageLocators.SEARCH_INPUT_FIELD)
        self.sl.wait_until_element_contains_text(AtherPageLocators.MAIN_ADDRESS_FIELD, contract_address )
        self.driver.close()
        
        

    def verify_all_home_page_elements(self):

        # #################### contract address section ####################
        # self.sl.wait_and_check_attribute_value_is_correct(self.CONTRACT_LOGO, 'src', HomeContent.contract_logo_src, 'contract logo src is not correct')
        # self.sl.wait_until_element_contains_text(self.CONTRACT_SYMPOL, HomeContent.contract_logo_text)
        # self.sl.wait_until_element_contains_text(self.CONTRACT_ADDRESS, HomeContent.contract_addres)
       

        # #################### landing-audited-section ####################
        # self.sl.wait_and_check_attribute_value_is_correct(self.CERTIK_LINK, 'href', HomeContent.certik_href, 'certik link is not correct')
        # self.sl.wait_and_check_attribute_value_is_correct(self.CERTIK_IMG, 'src', HomeContent.certik_src, 'certik src is not correct')
        # self.sl.wait_and_check_attribute_value_is_correct(self.PECKSHIELD_LINK, 'href', HomeContent.peckshield_href, 'peckshield link is not correct')
        # self.sl.wait_and_check_attribute_value_is_correct(self.PECKSHIELD_IMG, 'src', HomeContent.peckshield_src, 'peckshield src is not correct')
        # self.sl.wait_and_check_attribute_value_is_correct(self.TELEGRAM_LINK, 'href', HomeContent.telegram_href, 'telegram link is not correct')
        # self.sl.wait_and_check_attribute_value_is_correct(self.TELEGRAM_IMG, 'src', HomeContent.telegram_src, 'telegram src is not correct')
        # self.sl.wait_and_check_attribute_value_is_correct(self.ALPACA_FINANCE_LINK, 'href', HomeContent.alpacafinance_href, 'alpacafinance link is not correct')
        # self.sl.wait_and_check_attribute_value_is_correct(self.ALPACA_FINANCE_IMG, 'src', HomeContent.alpacafinance_src, 'alpacafinance src is not correct')
        # # certik link 
        # self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.CERTIK_LINK, page_name='certik', page_title=AtherPageContent.certik_page_title)
        # # PeckShield link
        # self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.PECKSHIELD_LINK, page_name='PeckShield' , page_title=AtherPageContent.PeckShield_page_title)
        # # telegram link
        # self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.TELEGRAM_LINK, page_name='telegram' , page_title=AtherPageContent.telegram_page_title)
        # # Alpaca_Finance link
        # self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.ALPACA_FINANCE_LINK, page_name='Alpaca Finance' , page_title=AtherPageContent.Alpaca_Finance_page_title)

        # self.sl.wait_and_click(self.AUDITED_SECTION_CLOSE_BTN)
        # self.sl.wait_until_invisibility(self.AUDITED_SECTION)

        #################### header ####################
        self.sl.wait_and_check_attribute_value_is_correct(self.LOGO_FIELD, 'src', HomeContent.logo, 'logo is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.HOME_LINK_FIELD, 'href', HomeContent.logo_href, 'Home link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.PRODUCTS_LINK_FIELD, 'href', HomeContent.products_href, 'products href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.ECO_SYSTEM_LINK_FIELD, 'href', HomeContent.ecosystem_href, 'ecosystem href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.ABOUT_LINK_FIELD, 'href', HomeContent.about_href, 'about href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.BLOG_LINK_FIELD, 'href', HomeContent.blog_href, 'blog href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.LAUNCH_LINK_FIELD, 'href', HomeContent.dashboard_href, 'launch APP link href is not correct')
        self.sl.wait_and_click(self.CUSTOM_SELECT_FIELD)
        self.sl.wait_and_click(self.CHINESE_LINK_FIELD)
        self.sl.wait_until_element_contains_text(self.Header_TITLE_FIELD, HomeContent.header_chinese_title)
        # product link
        self.sl.click_into_link_and_Verify_page_by_element_text(self.PRODUCTS_LINK_FIELD, ProductsPageLocators.LANDING_TITLE_FIELD, ProductPageContent.landing_title_text)
        self.open_home_page()
        # eco-system link
        self.sl.click_into_link_and_Verify_page_by_element_text(self.ECO_SYSTEM_LINK_FIELD, EcoSystemPageLocators.LANDING_TITLE_FIELD, EcoSystemPageContent.landing_title_text)
        self.open_home_page()
        # about link
        self.sl.click_into_link_and_Verify_page_by_element_text(self.ABOUT_LINK_FIELD, AboutPageLocators.LANDING_TITLE_FIELD, AboutPageContent.landing_title_text)
        self.open_home_page()
        # blog link
        self.sl.click_into_link_and_Verify_page_by_element_text(self.BLOG_LINK_FIELD, BlogPageLocators.LANDING_TITLE_FIELD, BlogPageContent.landing_title_text)
        self.open_home_page()
        # Launch APP link 
        self.sl.click_into_link_and_Verify_page_by_element_text(self.LAUNCH_LINK_FIELD, DashboardPageLocators.HEADER_TITLE, DashboarPageContent.header_title_text)
        self.open_home_page()
  

        #################### landing section  #########################
        self.sl.wait_until_element_contains_text(self.Header_TITLE_FIELD, HomeContent.header_title)
        self.sl.wait_until_element_contains_text(self.Header_LANDING_DESC_FIELD, HomeContent.header_landing_desc)
        self.sl.wait_until_element_contains_text(self.LAUNCH_APP_BTN, HomeContent.Launch_APP_btn_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.LAUNCH_APP_BTN, 'href', HomeContent.dashboard_href, 'launch APP btn href is not correct')
        self.sl.check_value_of_css_property(self.HEADER_BG_IMG_FIELD, 'background-image', HomeContent.header_landing_background_image, 'header landing background image is not correct')
        # Launch APP btn  
        self.sl.click_into_link_and_Verify_page_by_element_text(self.LAUNCH_APP_BTN, DashboardPageLocators.HEADER_TITLE, DashboarPageContent.header_title_text)
        self.open_home_page()
        

        #################### listed On section ####################
        self.sl.wait_until_element_contains_text(self.LISTED_ON_TITLE_FIELD, HomeContent.listed_on_title_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.CRYPTO_LINK_FIELD, 'href', HomeContent.crypto_link_href, 'crypto link is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.CRYPTO_IMG_FIELD, 'src', HomeContent.crypto_link_src, 'crypto src is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.COIN_GECKO_LINK_FIELD, 'href', HomeContent.coin_gecko_link_href, 'coin_gecko link is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.COIN_GECKO_IMG_FIELD, 'src', HomeContent.coin_gecko_link_src, 'coin_gecko src is not correct')    
        self.sl.wait_and_check_attribute_value_is_correct(self.PANCAKESWAP_LINK_FIELD, 'href', HomeContent.pancakeswap_link_href, 'pancakeswap link is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.PANCAKESWAP_IMG_FIELD, 'src', HomeContent.pancakeswap_link_src, 'pancakeswap src is not correct')    
        self.sl.wait_and_check_attribute_value_is_correct(self.BINANCE_LINK_FIELD, 'href', HomeContent.binance_link_href, 'binance link is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.BINANCE_IMG_FIELD, 'src', HomeContent.binance_link_src, 'binance src is not correct')    
        self.sl.wait_and_check_attribute_value_is_correct(self.COINBASE_LINK_FIELD, 'href', HomeContent.coinbase_link_href, 'coinbase link is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.COINBASE_IMG_FIELD, 'src', HomeContent.coinbase_link_src, 'coinbase src is not correct')    
        self.sl.wait_and_check_attribute_value_is_correct(self.LIVE_COIN_WATCH_LINK_FIELD, 'href', HomeContent.live_coin_watch_link_href, 'live_coin_watch link is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.LIVE_COIN_WATCH_IMG_FIELD, 'src', HomeContent.live_coin_watch_link_src, 'live_coin_watch src is not correct')    
        self.sl.wait_and_check_attribute_value_is_correct(self.POO_COIN_CHARTS_LINK_FIELD, 'href', HomeContent.poo_coin_charts_link_href, ' link is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.POO_COIN_CHARTS_IMG_FIELD, 'src', HomeContent.poo_coin_charts_link_src, ' src is not correct')    
        self.sl.wait_and_check_attribute_value_is_correct(self.DEXTOOLS_LINK_FIELD, 'href', HomeContent.dectools_link_href, ' link is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.DEXTOOLS_IMG_FIELD, 'src', HomeContent.dectools_link_src, ' src is not correct')    

        # Crypto.com link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.CRYPTO_LINK_FIELD, page_name='Crypto.com' , page_title=AtherPageContent.Crypto_page_title)
        # CoinGecko link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.COIN_GECKO_LINK_FIELD, page_name='CoinGecko' , page_title=AtherPageContent.CoinGecko_page_title)
        # PancakeSwap link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.PANCAKESWAP_LINK_FIELD, page_name='PancakeSwap', page_title= AtherPageContent.PancakeSwap_page_title, timeout=10 )
        # Binance link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.BINANCE_LINK_FIELD, page_name='Binance' , page_title=AtherPageContent.Binance_page_title)
        # Coinbase link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.COINBASE_LINK_FIELD, page_name='Coinbase', page_title= AtherPageContent.Coinbase_page_title, timeout=8 )
        # live coin watch link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.LIVE_COIN_WATCH_LINK_FIELD, page_name='live_coin_watch' , page_title=AtherPageContent.live_coin_watch_page_title)
        # PooCoin Charts link 
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_logo(self.POO_COIN_CHARTS_LINK_FIELD, page_name='PooCoin_Charts', logo_locator=AtherPageLocators.POOCOIN_LOGO_FIELD, logo_src=AtherPageContent.PooCoin_Charts_logo_src)
        # DEXTools link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_logo(self.DEXTOOLS_LINK_FIELD, page_name='DEXTools', logo_locator=AtherPageLocators.DEX_TOOLS_LOGO_FIELD, logo_src=AtherPageContent.DEXTools_logo_src)


        #################### investment System section ####################
        self.sl.wait_until_element_contains_text(self.INVESTMENT_SYSTEM_TITLE_FIELD, HomeContent.investment_System_title_text)
        self.sl.wait_until_element_contains_text(self.INVESTMENT_SYSTEM_DESC_FIELD, HomeContent.investment_System_desc_text)
        self.sl.wait_until_element_contains_text(self.GO_TO_PRODUCTS_LINK, HomeContent.investment_System_btn_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.GO_TO_PRODUCTS_LINK, 'href', HomeContent.investment_System_btn_href, 'investment System button href is not correct')    
        self.sl.check_value_of_css_property(self.INVESTMENT_SYSTEM_BG_FIELD, 'background-image', HomeContent.investment_System_background_image, 'investment_System background image is not correct')
        # Go to the products btn
        self.sl.click_into_link_and_Verify_page_by_element_text(self.GO_TO_PRODUCTS_LINK, ProductsPageLocators.LANDING_TITLE_FIELD, ProductPageContent.landing_title_text)
        self.open_home_page()

       
       
        #################### GYM Street section ####################
        self.sl.wait_until_element_contains_text(self.GYM_STREET_TITLE_FIELD, HomeContent.GYM_Street_title_text)
        self.sl.wait_until_element_contains_text(self.GYM_STREET_DESC_FIELD, HomeContent.GYM_Street_desc_text)
        self.sl.wait_until_element_contains_text(self.GYM_STREET_LINK, HomeContent.GYM_Street_btn_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.GYM_STREET_LINK, 'href', HomeContent.GYM_Street_btn_href, 'GYM Street button href is not correct')    
        # Go to GYM Street
        self.sl.click_into_link_and_Verify_page_by_element_text(self.GYM_STREET_LINK, EcoSystemPageLocators.GYMSTREET_TITLE, EcoSystemPageContent.gymstreet_title_text)
        assert self.driver.current_url == 'https://pages.gymnetwork.io/ecosystem/#gymstreet'
        self.open_home_page()


        #################### exchange-crypto section ####################
        self.sl.wait_until_element_contains_text(self.EXCHANGE_CRYPTO_TITLE_FIELD, HomeContent.exchange_crypto_title_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.EXCHANGE_CRYPTO_IMG_FIELD, 'src', HomeContent.exchange_crypto_img_src, 'exchange_crypto img src is not correct')    


        #################### Metaverse section ####################
        self.sl.wait_until_element_contains_text(self.METAVERSE_DESC_FIELD, HomeContent.Metaverse_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.METAVERSE_IMG_FIELD, 'src', HomeContent.Metaverse_img_src, 'Metaverse img src is not correct')    
        self.sl.check_value_of_css_property(self.METAVERSE_BG_FIELD, 'background-image', HomeContent.Metaverse_background_image, 'Metaverse background image is not correct')


        #################### ivendpay section ####################
        self.sl.wait_until_element_contains_text(self.IVENDPAY_TITLE_FIELD, HomeContent.ivendpay_title_text)
        self.sl.wait_until_element_contains_text(self.IVENDPAY_CARD1_TITLE_FIELD, HomeContent.ivendpay_card1_title_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.IVENDPAY_CARD1_IMG_FIELD, 'src', HomeContent.ivendpay_card1_img_src, 'ivendpay card1 img src is not correct')    
        self.sl.wait_until_element_contains_text(self.IVENDPAY_CARD2_TITLE_FIELD, HomeContent.ivendpay_card2_title_text)
        self.sl.wait_until_element_contains_text(self.IVENDPAY_CARD2_DESC_FIELD, HomeContent.ivendpay_card2_desc_text)
        self.sl.wait_until_element_contains_text(self.IVENDPAY_CARD2_LINK_FIELD, HomeContent.ivendpay_card2_link_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.IVENDPAY_CARD2_IMG_FIELD, 'src', HomeContent.ivendpay_card2_img_src, 'ivendpay card2 img src is not correct')    
        self.sl.wait_and_check_attribute_value_is_correct(self.IVENDPAY_CARD2_LINK_FIELD, 'href', HomeContent.ivendpay_card2_link_href, 'ivendpay card2 link href is not correct')    
        self.sl.wait_until_element_contains_text(self.IVENDPAY_CARD3_TITLE_FIELD, HomeContent.ivendpay_card3_title_text)
        self.sl.wait_until_element_contains_text(self.IVENDPAY_CARD3_DESC_FIELD, HomeContent.ivendpay_card3_desc_text)
        self.sl.wait_until_element_contains_text(self.IVENDPAY_CARD3_LINK_FIELD, HomeContent.ivendpay_card3_link_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.IVENDPAY_CARD3_IMG_FIELD, 'src', HomeContent.ivendpay_card3_img_src, 'ivendpay card3 img src is not correct')    
        self.sl.wait_and_check_attribute_value_is_correct(self.IVENDPAY_CARD3_LINK_FIELD, 'href', HomeContent.ivendpay_card3_link_href, 'ivendpay card3 link href is not correct')    
        # Vending machines link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.IVENDPAY_CARD2_LINK_FIELD, page_name='Vending machines' , page_title=AtherPageContent.Vending_machines_page_title)
        #  POS machines link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.IVENDPAY_CARD3_LINK_FIELD, page_name='POS machines' , page_title=AtherPageContent.POS_machines_page_title)
      

        #################### protection-tools section  ####################
        self.sl.wait_until_element_contains_text(self.PROTECTION_TOOLD_TITLE_FIELD, HomeContent.protection_tools_title_text)
        self.sl.wait_until_element_contains_text(self.PROTECTION_TOOLD_CARD1_TITLE_FIELD, HomeContent.protection_tools_card1_title_text)
        self.sl.wait_until_element_contains_text(self.PROTECTION_TOOLD_CARD1_DESC_FIELD, HomeContent.protection_tools_card1_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.PROTECTION_TOOLD_CARD1_IMG_FIELD, 'src', HomeContent.protection_tools_card1_img_src, 'protection-tools card1 img src is not correct')    
        self.sl.wait_until_element_contains_text(self.PROTECTION_TOOLD_CARD2_TITLE_FIELD, HomeContent.protection_tools_card2_title_text)
        self.sl.wait_until_element_contains_text(self.PROTECTION_TOOLD_CARD2_DESC_FIELD, HomeContent.protection_tools_card2_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.PROTECTION_TOOLD_CARD2_IMG_FIELD, 'src', HomeContent.protection_tools_card2_img_src, 'protection-tools card2 img src is not correct')    
        self.sl.wait_until_element_contains_text(self.PROTECTION_TOOLD_CARD3_TITLE_FIELD, HomeContent.protection_tools_card3_title_text)
        self.sl.wait_until_element_contains_text(self.PROTECTION_TOOLD_CARD3_DESC_FIELD, HomeContent.protection_tools_card3_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.PROTECTION_TOOLD_CARD3_IMG_FIELD, 'src', HomeContent.protection_tools_card3_img_src, 'protection-tools card3 img src is not correct')    
        self.sl.wait_until_element_contains_text(self.PROTECTION_TOOLD_CARD4_TITLE_FIELD, HomeContent.protection_tools_card4_title_text)
        self.sl.wait_until_element_contains_text(self.PROTECTION_TOOLD_CARD4_DESC_FIELD, HomeContent.protection_tools_card4_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.PROTECTION_TOOLD_CARD4_IMG_FIELD, 'src', HomeContent.protection_tools_card4_img_src, 'protection-tools card4 img src is not correct')    


        #################### get started section ####################
        self.sl.wait_until_element_contains_text(self.GET_STARTED_TITLE_FIELD, HomeContent.get_started_title_text)

        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD1_NUM_FIELD, HomeContent.get_started_card1_num)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD1_TITLE_FIELD, HomeContent.get_started_card1_title_text)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD1_DESC_FIELD, HomeContent.get_started_card1_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.GET_STARTED_CARD1_IMG_FIELD, 'src', HomeContent.get_started_card1_img_src, 'get started card1 img src is not correct')    
        self.sl.wait_and_check_attribute_value_is_correct(self.GET_STARTED_CARD1_LINK, 'href', HomeContent.get_started_card1_link_href, 'get started card1 link href is not correct')    

        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD2_NUM_FIELD, HomeContent.get_started_card2_num)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD2_TITLE_FIELD, HomeContent.get_started_card2_title_text)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD2_DESC_FIELD, HomeContent.get_started_card2_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.GET_STARTED_CARD2_IMG_FIELD, 'src', HomeContent.get_started_card2_img_src, 'get started card2 img src is not correct')    
        self.sl.wait_and_check_attribute_value_is_correct(self.GET_STARTED_CARD2_LINK, 'href', HomeContent.get_started_card2_link_href, 'get started card2 link href is not correct')    

        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD3_NUM_FIELD, HomeContent.get_started_card3_num)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD3_TITLE_FIELD, HomeContent.get_started_card3_title_text)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD3_DESC_FIELD, HomeContent.get_started_card3_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.GET_STARTED_CARD3_IMG_FIELD, 'src', HomeContent.get_started_card3_img_src, 'get started card3 img src is not correct')    
        self.sl.wait_and_check_attribute_value_is_correct(self.GET_STARTED_CARD3_LINK, 'href', HomeContent.get_started_card3_link_href, 'get started card3 link href is not correct')    

        # choose a crypto wallet link
        self.sl.click_into_link_Verify_page_by_title(self.GET_STARTED_CARD1_LINK, AtherPageContent.choose_a_crypto_wallet_video_page_title, page_name='choose_a_crypto_wallet_video')
        self.open_home_page()

        # make your deposit link     
        self.sl.click_into_link_Verify_page_by_title(self.GET_STARTED_CARD2_LINK, AtherPageContent.make_your_deposit_video_page_title, page_name='make_your_deposit_link_video')
        self.open_home_page()

        # connect your wallet link
        self.sl.click_into_link_Verify_page_by_title(self.GET_STARTED_CARD3_LINK, AtherPageContent.connect_your_wallet_video_page_title, page_name='connect_your_wallet_video')
        self.open_home_page()


       #################### roadmap section ####################
        self.sl.wait_until_element_contains_text(self.ROADMAP_TITLE_FIELD, HomeContent.roadmap_title_text)
        self.sl.wait_until_element_contains_text(self.ROADMAP_DESC_FIELD, HomeContent.roadmap_desc_text)

        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD1_DATE_FIELD, HomeContent.roadmap_card1_date)
        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD1_TITLE_FIELD, HomeContent.roadmap_card1_title_text)
        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD1_DESC_FIELD, HomeContent.roadmap_card1_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.ROADMAP_CARD1_IMG_FIELD, 'src', HomeContent.roadmap_card1_img_src, 'roadmap card1 img src is not correct')    

        self.sl.scrollIntoView_and_click(self.ROADMAP_NEXT_BTN)

        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD2_DATE_FIELD, HomeContent.roadmap_card2_date)
        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD2_TITLE_FIELD, HomeContent.roadmap_card2_title_text)
        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD2_DESC_FIELD, HomeContent.roadmap_card2_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.ROADMAP_CARD2_IMG_FIELD, 'src', HomeContent.roadmap_card2_img_src, 'roadmap card2 img src is not correct')   

        self.sl.scrollIntoView_and_click(self.ROADMAP_NEXT_BTN)


        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD3_DATE_FIELD, HomeContent.roadmap_card3_date)
        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD3_TITLE_FIELD, HomeContent.roadmap_card3_title_text)
        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD3_DESC_FIELD, HomeContent.roadmap_card3_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.ROADMAP_CARD3_IMG_FIELD, 'src', HomeContent.roadmap_card3_img_src, 'roadmap card3 img src is not correct')   

        self.sl.scrollIntoView_and_click(self.ROADMAP_NEXT_BTN)

        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD4_DATE_FIELD, HomeContent.roadmap_card4_date)
        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD4_TITLE_FIELD, HomeContent.roadmap_card4_title_text)
        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD4_DESC_FIELD, HomeContent.roadmap_card4_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.ROADMAP_CARD4_IMG_FIELD, 'src', HomeContent.roadmap_card4_img_src, 'roadmap card4 img src is not correct')   

        self.sl.scrollIntoView_and_click(self.ROADMAP_NEXT_BTN)

        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD5_DATE_FIELD, HomeContent.roadmap_card5_date)
        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD5_TITLE_FIELD, HomeContent.roadmap_card5_title_text)
        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD5_DESC_FIELD, HomeContent.roadmap_card5_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.ROADMAP_CARD5_IMG_FIELD, 'src', HomeContent.roadmap_card5_img_src, 'roadmap card5 img src is not correct')   

        self.sl.scrollIntoView_and_click(self.ROADMAP_NEXT_BTN)

        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD6_DATE_FIELD, HomeContent.roadmap_card6_date)
        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD6_TITLE_FIELD, HomeContent.roadmap_card6_title_text)
        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD6_DESC_FIELD, HomeContent.roadmap_card6_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.ROADMAP_CARD6_IMG_FIELD, 'src', HomeContent.roadmap_card6_img_src, 'roadmap card6 img src is not correct')   

        self.sl.scrollIntoView_and_click(self.ROADMAP_NEXT_BTN)

        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD7_DATE_FIELD, HomeContent.roadmap_card7_date)
        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD7_TITLE_FIELD, HomeContent.roadmap_card7_title_text)
        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD7_DESC_FIELD, HomeContent.roadmap_card7_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.ROADMAP_CARD7_IMG_FIELD, 'src', HomeContent.roadmap_card7_img_src, 'roadmap card7 img src is not correct')   

        self.sl.scrollIntoView_and_click(self.ROADMAP_NEXT_BTN)

        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD8_DATE_FIELD, HomeContent.roadmap_card8_date)
        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD8_TITLE_FIELD, HomeContent.roadmap_card8_title_text)
        self.sl.wait_until_element_contains_text(self.ROADMAP_CARD8_DESC_FIELD, HomeContent.roadmap_card8_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.ROADMAP_CARD8_IMG_FIELD, 'src', HomeContent.roadmap_card8_img_src, 'roadmap card8 img src is not correct')   


       #################### faq section  ####################
        self.sl.wait_until_element_contains_text(self.FAQ_TITLE_FIELD, HomeContent.faq_title_text)

        self.sl.wait_until_element_contains_text(self.WHAT_IS_DEFI_BTN_FIELD, HomeContent.what_defi)
        self.sl.scrollIntoView_and_click(self.WHAT_IS_DEFI_BTN_FIELD)
        self.sl.wait_until_element_contains_text(self.WHAT_IS_DEFI_ANSWER_FIELD, HomeContent.what_defi_answer)

        self.sl.wait_until_element_contains_text(self.WHAT_ARE_SMART_CONTRACTS_BTN_FIELD, HomeContent.what_smart_contract)
        self.sl.scrollIntoView_and_click(self.WHAT_ARE_SMART_CONTRACTS_BTN_FIELD)
        self.sl.wait_until_element_contains_text(self.WHAT_ARE_SMART_CONTRACTS_ANSWER_FIELD, HomeContent.what_smart_contract_answer)

        self.sl.wait_until_element_contains_text(self.WHAT_IS_LIQUIDITY_MINING_BTN_FIELD, HomeContent.what_liquidity_meaning)
        self.sl.scrollIntoView_and_click(self.WHAT_IS_LIQUIDITY_MINING_BTN_FIELD)
        self.sl.wait_until_element_contains_text(self.WHAT_IS_LIQUIDITY_MINING_ANSWER_FIELD, HomeContent.what_liquidity_meaning_answer)

        self.sl.wait_until_element_contains_text(self.WHAT_EXACTLY_ARE_LIQUIDITY_POOLS_BTN_FIELD, HomeContent.what_liquidity_pool)
        self.sl.scrollIntoView_and_click(self.WHAT_EXACTLY_ARE_LIQUIDITY_POOLS_BTN_FIELD)
        self.sl.wait_until_element_contains_text(self.WHAT_EXACTLY_ARE_LIQUIDITY_POOLS_ANSWER_FIELD, HomeContent.what_liquidity_pool_answer)

        self.sl.wait_until_element_contains_text(self.LEARN_MORE_BTN_FIELD, HomeContent.Learn_more_btn_text)
        self.sl.scrollIntoView_and_click(self.LEARN_MORE_BTN_FIELD)

        self.sl.wait_until_element_contains_text(self.WHAT_IS_DAO_BTN_FIELD, HomeContent.what_dao)
        self.sl.scrollIntoView_and_click(self.WHAT_IS_DAO_BTN_FIELD)
        self.sl.wait_until_element_contains_text(self.WHAT_IS_DAO_ANSWER_FIELD, HomeContent.what_dao_answer)

        self.sl.wait_until_element_contains_text(self.WHAT_IS_DAO_GOVERNANCE_BTN_FIELD, HomeContent.what_dao_governance)
        self.sl.scrollIntoView_and_click(self.WHAT_IS_DAO_GOVERNANCE_BTN_FIELD)
        self.sl.wait_until_element_contains_text(self.WHAT_IS_DAO_GOVERNANCE_ANSWER_FIELD, HomeContent.what_dao_governance_answer)

        self.sl.wait_until_element_contains_text(self.HOW_CAN_I_USE_GYM_NETWORK_BTN_FIELD, HomeContent.how_use_network)
        self.sl.scrollIntoView_and_click(self.HOW_CAN_I_USE_GYM_NETWORK_BTN_FIELD)
        self.sl.wait_until_element_contains_text(self.HOW_CAN_I_USE_GYM_NETWORK_ANSWER_FIELD, HomeContent.how_use_network_answer)

        self.sl.wait_until_element_contains_text(self.WHICH_WALLET_USE_TO_CONNECT_BTN_FIELD, HomeContent.which_wallet_use_to_connect)
        self.sl.scrollIntoView_and_click(self.WHICH_WALLET_USE_TO_CONNECT_BTN_FIELD)
        self.sl.wait_until_element_contains_text(self.WHICH_WALLET_USE_TO_CONNECT_ANSWER_FIELD, HomeContent.which_wallet_use_to_connect_answer)

        self.sl.wait_until_element_contains_text(self.WHAT_IS_APY_APR_BTN_FIELD, HomeContent.what_apy_apr)
        self.sl.scrollIntoView_and_click(self.WHAT_IS_APY_APR_BTN_FIELD)
        self.sl.wait_until_element_contains_text(self.WHAT_IS_APY_APR_ANSWER_FIELD, HomeContent.what_apy_apr_answer)

        self.sl.wait_until_element_contains_text(self.WHERE_REWORDS_VAULTS_COME_FROM_BTN_FIELD, HomeContent.where_rewords_vaults_come_from)
        self.sl.scrollIntoView_and_click(self.WHERE_REWORDS_VAULTS_COME_FROM_BTN_FIELD)
        self.sl.wait_until_element_contains_text(self.WHERE_REWORDS_VAULTS_COME_FROM_ANSWER_FIELD, HomeContent.where_rewords_vaults_come_from_answer) 

        self.sl.wait_until_element_contains_text(self.WHO_OR_WHAT_IS_ALPACA_BTN_FIELD, HomeContent.who_what_alpaca)
        self.sl.scrollIntoView_and_click(self.WHO_OR_WHAT_IS_ALPACA_BTN_FIELD)
        self.sl.wait_until_element_contains_text(self.WHO_OR_WHAT_IS_ALPACA_ANSWER_FIELD, HomeContent.who_what_alpaca_answer)

        self.sl.wait_until_element_contains_text(self.WHAT_IS_BINANCE_BTN_FIELD, HomeContent.what_binance)
        self.sl.scrollIntoView_and_click(self.WHAT_IS_BINANCE_BTN_FIELD)
        self.sl.wait_until_element_contains_text(self.WHAT_IS_BINANCE_ANSWER_FIELD, HomeContent.what_binance_answer)

        self.sl.wait_until_element_contains_text(self.WHAT_DO_WITH_GYMNET_FIELD, HomeContent.what_do_with_gymnet)
        self.sl.scrollIntoView_and_click(self.WHAT_DO_WITH_GYMNET_FIELD)
        self.sl.wait_until_element_contains_text(self.WHAT_DO_WITH_GYMNET_ANSWER_FIELD, HomeContent.what_do_with_gymnet_answer)

        self.sl.wait_until_element_contains_text(self.WHERE_GYMNET_TOKEN_LISTED_FIELD, HomeContent.where_gymnet_lysted)
        self.sl.scrollIntoView_and_click(self.WHERE_GYMNET_TOKEN_LISTED_FIELD)
        self.sl.wait_until_element_contains_text(self.WHERE_GYMNET_TOKEN_LISTED_ANSWER_FIELD, HomeContent.where_gymnet_lysted_answer)

        self.sl.wait_until_element_contains_text(self.WHER_FIND_TUTORIALS_FIELD, HomeContent.where_find_tutorials)
        self.sl.scrollIntoView_and_click(self.WHER_FIND_TUTORIALS_FIELD)
        self.sl.wait_until_element_contains_text(self.WHER_FIND_TUTORIALS_ANSWER_FIELD, HomeContent.where_find_tutorials_answer)

        self.sl.wait_until_element_contains_text(self.HOW_AFFILIATE_WORK_FIELD, HomeContent.how_affiliate_work)
        self.sl.scrollIntoView_and_click(self.HOW_AFFILIATE_WORK_FIELD)
        self.sl.wait_until_element_contains_text(self.HOW_AFFILIATE_WORK_ANSWER_FIELD, HomeContent.how_affiliate_work_answer)


        #################### join telegram section  ####################
        
        self.JoinTelegram_section.verify_all_JoinTelegram_section_elements()
        # join telegram btn
        self.sl.click_into_link_Verify_page_by_title(JoinTelegramLocators.JOIN_TELEGRAM_BTN_LINK_FIELD, AtherPageContent.telegram_page_title, page_name='telegram')
        self.driver.get(self.url)



        #################### footer section ####################

        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_LOGO_FIELD, 'href',  HomeContent.logo_href, 'footer logo link href is not correct')
        self.sl.wait_until_element_contains_text( self.FOOTER_DESC_FIELD, HomeContent.footer_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_TWITTER_LINK_FIELD, 'href', HomeContent.footer_twitter_link_href, 'footer twitter link href is not correct')    
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_TELEGRAM_LINK_FIELD, 'href', HomeContent.join_telegram_link_href, 'footer telegram link href is not correct')    
        
        self.sl.wait_until_element_contains_text( self.FOOTER_PRODUCTS_TITLE_FIELD, HomeContent.footer_product_title_text)
        self.sl.wait_until_element_contains_text( self.FOOTER_PRODUCTS_VULTE_LINK_FIELD, HomeContent.footer_vault_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_PRODUCTS_VULTE_LINK_FIELD, 'href', HomeContent.footer_vault_link_href, 'footer vault link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_PRODUCTS_FARMING_LINK_FIELD, HomeContent.footer_Farming_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_PRODUCTS_FARMING_LINK_FIELD, 'href', HomeContent.footer_Farming_link_href, 'footer Farming link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_PRODUCTS_SINGLE_POOL_LINK_FIELD, HomeContent.footer_Single_Pool_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_PRODUCTS_SINGLE_POOL_LINK_FIELD, 'href', HomeContent.footer_Single_Pool_link_href, 'footer Single_Pool link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_PRODUCTS_BUY_GYMNET_LINK_FIELD, HomeContent.footer_Buy_GYMNET_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_PRODUCTS_BUY_GYMNET_LINK_FIELD, 'href', HomeContent.footer_Buy_GYMNET_link_href, 'footer Buy_GYMNET link href is not correct')    

        self.sl.wait_until_element_contains_text( self.FOOTER_ECO_SYSTEM_TITLE_FIELD, HomeContent.footer_Eco_system_title_text)
        self.sl.wait_until_element_contains_text( self.FOOTER_GYMSTREET_LINK_FIELD, HomeContent.footer_Gymstreet_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_GYMSTREET_LINK_FIELD, 'href', HomeContent.footer_Gymstreet_link_href, 'footer Gymstreet link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_METABOCKS_LINK_FIELD, HomeContent.footer_Metablocks_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_METABOCKS_LINK_FIELD, 'href', HomeContent.footer_Metablocks_link_href, 'footer Metablocks link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_CASH_FT_LINK_FIELD, HomeContent.footer_CashFT_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_CASH_FT_LINK_FIELD, 'href', HomeContent.footer_CashFT_link_href, 'footer CashFT link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_ZUCKERLAND_LINK_FIELD, HomeContent.footer_Zuckerland_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_ZUCKERLAND_LINK_FIELD, 'href', HomeContent.footer_Zuckerland_link_href, 'footer Zuckerland link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_GYM_DEX_LINK_FIELD, HomeContent.footer_Gym_Dex_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_GYM_DEX_LINK_FIELD, 'href', HomeContent.footer_Gym_Dex_link_href, 'footer Gym_Dex link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_METAVERSE_CAMPUS_LINK_FIELD, HomeContent.footer_Metaverse_Campus_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_METAVERSE_CAMPUS_LINK_FIELD, 'href', HomeContent.footer_Metaverse_Campus_link_href, 'footer Metaverse link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_WHITEPAPER_LINK_FIELD, HomeContent.footer_Whitepaper_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_WHITEPAPER_LINK_FIELD, 'href', HomeContent.footer_Whitepaper_link_href, 'footer Whitepaper link href is not correct')    

        self.sl.wait_until_element_contains_text( self.FOOTER_ABOUT_TITLE_FIELD, HomeContent.footer_About_title_text)
        self.sl.wait_until_element_contains_text( self.FOOTER_BLOG_NEWS_LINK_FIELD, HomeContent.footer_Blog_News_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_BLOG_NEWS_LINK_FIELD, 'href', HomeContent.footer_Blog_News_link_href, 'footer Blog_News link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_SUPPORT_LINK_FIELD, HomeContent.footer_Support_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_SUPPORT_LINK_FIELD, 'href', HomeContent.footer_Support_link_href, 'footer Support link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_GUIDE_LINK_FIELD, HomeContent.footer_Guide_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_GUIDE_LINK_FIELD, 'href', HomeContent.footer_Guide_link_href, 'footer Guide link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_TOKEN_CONTRACT_LINK_FIELD, HomeContent.footer_Token_Contract_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_TOKEN_CONTRACT_LINK_FIELD, 'href', HomeContent.footer_Token_Contract_link_href, 'footer Token_Contract link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_INFO_LINK_FIELD, HomeContent.footer_info_text)
    
        # Twitter LINK
        self.sl.click_into_link_Verify_page_by_title( self.FOOTER_TWITTER_LINK_FIELD, AtherPageContent.Twitter_page_title, page_name='Twitter', timeout= 7)
        self.driver.get(self.url)
        # telegram LINK
        self.sl.click_into_link_Verify_page_by_title( self.FOOTER_TELEGRAM_LINK_FIELD, AtherPageContent.telegram_page_title, page_name='telegram')
        self.driver.get(self.url)

        ########## PRODUCTS LINKS ##########

        # Vault LINK
        self.sl.click_into_link_and_Verify_page_by_element_text( self.FOOTER_PRODUCTS_VULTE_LINK_FIELD, ProductsPageLocators.VAULT_TITLE_FIELD, ProductPageContent.vault_title_text)
        assert self.driver.current_url == 'https://pages.gymnetwork.io/products/#vault'
        self.driver.get(self.url)
  
        # farming LINK
        self.sl.click_into_link_and_Verify_page_by_element_text( self.FOOTER_PRODUCTS_FARMING_LINK_FIELD, ProductsPageLocators.FARMING_TITLE_FIELD, ProductPageContent.farming_btn_text)
        assert self.driver.current_url == 'https://pages.gymnetwork.io/products/#farmandsingle'
        self.driver.get(self.url)

        # Single Pool LINK
        self.sl.click_into_link_and_Verify_page_by_element_text( self.FOOTER_PRODUCTS_SINGLE_POOL_LINK_FIELD, ProductsPageLocators.LANDING_TITLE_FIELD, ProductPageContent.landing_title_text)
        assert self.driver.current_url == 'https://pages.gymnetwork.io/products/#farmandsingle'
        self.driver.get(self.url)
    
        # Buy GYMNET LINK
        self.sl.click_into_link_and_Verify_page_by_logo( self.FOOTER_PRODUCTS_BUY_GYMNET_LINK_FIELD, page_name='PooCoin_Charts', logo_locator=AtherPageLocators.POOCOIN_LOGO_FIELD, logo_src=AtherPageContent.PooCoin_Charts_logo_src)
        self.driver.get(self.url)


        ########## Eco-system LINKS ##########

        # Gymstreet link
        self.sl.click_into_link_and_Verify_page_by_element_text( self.FOOTER_GYMSTREET_LINK_FIELD, EcoSystemPageLocators.GYMSTREET_TITLE, EcoSystemPageContent.gymstreet_title_text)
        assert self.driver.current_url == 'https://pages.gymnetwork.io/ecosystem/#gymstreet'
        self.driver.get(self.url)

        # metablocks link
        self.sl.click_into_link_and_Verify_page_by_element_text( self.FOOTER_METABOCKS_LINK_FIELD, EcoSystemPageLocators.METABLOCKS_TITLE, EcoSystemPageContent.metablocks_title_text)
        assert self.driver.current_url == 'https://pages.gymnetwork.io/ecosystem/#metablocks'
        self.driver.get(self.url) 

        # CashFT link
        self.sl.click_into_link_and_Verify_page_by_element_text( self.FOOTER_CASH_FT_LINK_FIELD, EcoSystemPageLocators.LANDING_TITLE_FIELD, EcoSystemPageContent.landing_title_text)
        assert self.driver.current_url == 'https://pages.gymnetwork.io/ecosystem/#cashFT'
        self.driver.get(self.url) 

        # Zuckerland link
        self.sl.click_into_link_and_Verify_page_by_element_text( self.FOOTER_ZUCKERLAND_LINK_FIELD, EcoSystemPageLocators.ZUCKERLAND_TITLE, EcoSystemPageContent.zuckerland_title_text)
        assert self.driver.current_url == 'https://pages.gymnetwork.io/ecosystem/#zuckerland'
        self.driver.get(self.url) 

        # Gym Dex link
        self.sl.click_into_link_and_Verify_page_by_element_text( self.FOOTER_GYM_DEX_LINK_FIELD, EcoSystemPageLocators.GYM_DEX_TITLE, EcoSystemPageContent.Gym_Dex_title_text)
        assert self.driver.current_url == 'https://pages.gymnetwork.io/ecosystem/#gym-dex'
        self.driver.get(self.url) 

        # Metaverse Campus link
        self.sl.click_into_link_and_Verify_page_by_element_text( self.FOOTER_METAVERSE_CAMPUS_LINK_FIELD, EcoSystemPageLocators.METAVERSE_CAMPUS_TITLE, EcoSystemPageContent.metaverse_title_text)
        assert self.driver.current_url == 'https://pages.gymnetwork.io/ecosystem/#metaverse'
        self.driver.get(self.url) 

        # Whitepaper link
        self.sl.scrollIntoView_and_click( self.FOOTER_WHITEPAPER_LINK_FIELD)
        assert self.driver.current_url == 'https://gymnetwork.b-cdn.net/GYMNET-Whitepaper.pdf'
        self.driver.get(self.url) 


        ########## About LINKS ##########

        # Blog & News LINK 
        self.sl.click_into_link_and_Verify_page_by_element_text( self.FOOTER_BLOG_NEWS_LINK_FIELD, BlogPageLocators.LANDING_TITLE_FIELD, BlogPageContent.landing_title_text)
        self.driver.get(self.url)
        

        # Support LINK
        self.sl.click_into_link_and_Verify_page_by_element_text( self.FOOTER_SUPPORT_LINK_FIELD, AtherPageLocators.CUSTOMER_SUPPORT_PAPER_TITLE, AtherPageContent.customer_support_title_text)
        self.driver.get(self.url)

        # Guide LINK
        self.sl.click_into_link_Verify_page_by_title( self.FOOTER_GUIDE_LINK_FIELD, AtherPageContent.docs_gymnetwork_title_text, page_name=self.driver.title , timeout=10)
        self.driver.get(self.url)

        # Token Contract LINK
        self.sl.click_into_link_Verify_page_by_title( self.FOOTER_TOKEN_CONTRACT_LINK_FIELD, AtherPageContent.Tokenomics_page_title, page_name='Tokenomics')
        self.driver.get(self.url)
