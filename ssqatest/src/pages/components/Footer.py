from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpe.global_content.FooterContent import FooterContent
from ssqatest.src.helpe.AtherPageContent import AtherPageContent
from ssqatest.src.pages.locators.AtherPageLocators import AtherPageLocators
from ssqatest.src.pages.locators.BlogPageLocators import BlogPageLocators
from ssqatest.src.helpe.ProductPageContent import ProductPageContent 
from ssqatest.src.helpe.BlogPageContent import BlogPageContent 
from ssqatest.src.pages.locators.ProductsPageLocators import ProductsPageLocators
from ssqatest.src.pages.locators.EcoSystemPageLocators import EcoSystemPageLocators
from ssqatest.src.helpe.EcoSystemPageContent import EcoSystemPageContent
from ssqatest.src.pages.locators.global_sections.FooterLocators import FooterLocators

class Footer(FooterLocators):
    
    def __init__(self, driver, url):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
        self.url = url

    def verify_all_footer_elements(self):

        #################### footer section ####################
        
        self.sl.wait_and_check_attribute_value_is_correct(self.FOOTER_LOGO_FIELD, 'href',  FooterContent.logo_href,  FooterContent.logo_href + ' footer logo link href is not correct')
        self.sl.wait_until_element_contains_text( self.FOOTER_DESC_FIELD, FooterContent.footer_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_TWITTER_LINK_FIELD, 'href', FooterContent.footer_twitter_link_href, 'footer twitter link href is not correct')    
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_TELEGRAM_LINK_FIELD, 'href', FooterContent.join_telegram_link_href, 'footer telegram link href is not correct')    
        
        self.sl.wait_until_element_contains_text( self.FOOTER_PRODUCTS_TITLE_FIELD, FooterContent.footer_product_title_text)
        self.sl.wait_until_element_contains_text( self.FOOTER_PRODUCTS_VULTE_LINK_FIELD, FooterContent.footer_vault_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_PRODUCTS_VULTE_LINK_FIELD, 'href', FooterContent.footer_vault_link_href, 'footer vault link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_PRODUCTS_FARMING_LINK_FIELD, FooterContent.footer_Farming_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_PRODUCTS_FARMING_LINK_FIELD, 'href', FooterContent.footer_Farming_link_href, 'footer Farming link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_PRODUCTS_SINGLE_POOL_LINK_FIELD, FooterContent.footer_Single_Pool_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_PRODUCTS_SINGLE_POOL_LINK_FIELD, 'href', FooterContent.footer_Single_Pool_link_href, 'footer Single_Pool link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_PRODUCTS_BUY_GYMNET_LINK_FIELD, FooterContent.footer_Buy_GYMNET_text)
        # self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_PRODUCTS_BUY_GYMNET_LINK_FIELD, 'href', FooterContent.footer_Buy_GYMNET_link_href, 'footer Buy_GYMNET link href is not correct')    

        self.sl.wait_until_element_contains_text( self.FOOTER_ECO_SYSTEM_TITLE_FIELD, FooterContent.footer_Eco_system_title_text)
        self.sl.wait_until_element_contains_text( self.FOOTER_GYMSTREET_LINK_FIELD, FooterContent.footer_Gymstreet_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_GYMSTREET_LINK_FIELD, 'href', FooterContent.footer_Gymstreet_link_href, 'footer Gymstreet link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_METABOCKS_LINK_FIELD, FooterContent.footer_Metablocks_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_METABOCKS_LINK_FIELD, 'href', FooterContent.footer_Metablocks_link_href, 'footer Metablocks link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_CASH_FT_LINK_FIELD, FooterContent.footer_CashFT_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_CASH_FT_LINK_FIELD, 'href', FooterContent.footer_CashFT_link_href, 'footer CashFT link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_ZUCKERLAND_LINK_FIELD, FooterContent.footer_Zuckerland_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_ZUCKERLAND_LINK_FIELD, 'href', FooterContent.footer_Zuckerland_link_href, 'footer Zuckerland link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_GYM_DEX_LINK_FIELD, FooterContent.footer_Gym_Dex_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_GYM_DEX_LINK_FIELD, 'href', FooterContent.footer_Gym_Dex_link_href, 'footer Gym_Dex link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_WHITEPAPER_LINK_FIELD, FooterContent.footer_Whitepaper_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_WHITEPAPER_LINK_FIELD, 'href', FooterContent.footer_Whitepaper_link_href, 'footer Whitepaper link href is not correct')    

        self.sl.wait_until_element_contains_text( self.FOOTER_ABOUT_TITLE_FIELD, FooterContent.footer_About_title_text)
        self.sl.wait_until_element_contains_text( self.FOOTER_BLOG_NEWS_LINK_FIELD, FooterContent.footer_Blog_News_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_BLOG_NEWS_LINK_FIELD, 'href', FooterContent.footer_Blog_News_link_href, 'footer Blog_News link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_SUPPORT_LINK_FIELD, FooterContent.footer_Support_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_SUPPORT_LINK_FIELD, 'href', FooterContent.footer_Support_link_href, 'footer Support link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_GUIDE_LINK_FIELD, FooterContent.footer_Guide_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_GUIDE_LINK_FIELD, 'href', FooterContent.footer_Guide_link_href, 'footer Guide link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_TOKEN_CONTRACT_LINK_FIELD, FooterContent.footer_Token_Contract_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.FOOTER_TOKEN_CONTRACT_LINK_FIELD, 'href', FooterContent.footer_Token_Contract_link_href, 'footer Token_Contract link href is not correct')    
        self.sl.wait_until_element_contains_text( self.FOOTER_INFO_LINK_FIELD, FooterContent.footer_info_text)
    
        # Twitter LINK
        self.sl.click_into_link_Verify_page_by_title( self.FOOTER_TWITTER_LINK_FIELD, AtherPageContent.Twitter_page_title, page_name='Twitter', timeout=20)
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
        self.sl.click_into_link_and_Verify_page_by_element_text( self.FOOTER_PRODUCTS_FARMING_LINK_FIELD, ProductsPageLocators.FARMING_BTN_FIELD, ProductPageContent.farming_title_text)
        assert self.driver.current_url == 'https://pages.gymnetwork.io/products/#farming'
        self.driver.get(self.url)

        # Single Pool LINK
        self.sl.click_into_link_and_Verify_page_by_element_text( self.FOOTER_PRODUCTS_SINGLE_POOL_LINK_FIELD, ProductsPageLocators.LANDING_TITLE_FIELD, ProductPageContent.landing_title_text)
        assert self.driver.current_url == 'https://pages.gymnetwork.io/products/#farming'
        self.driver.get(self.url)
    
        # Buy GYMNET LINK
        # self.sl.click_into_link_and_Verify_page_by_logo( self.FOOTER_PRODUCTS_BUY_GYMNET_LINK_FIELD, page_name='PooCoin_Charts', logo_locator=AtherPageLocators.POOCOIN_LOGO_FIELD, logo_src=AtherPageContent.PooCoin_Charts_logo_src)
        # self.driver.get(self.url)
       

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
        assert self.driver.current_url == 'https://pages.gymnetwork.io/ecosystem/#cashft'
        self.driver.get(self.url) 

        # Zuckerland link
        self.sl.click_into_link_and_Verify_page_by_element_text( self.FOOTER_ZUCKERLAND_LINK_FIELD, EcoSystemPageLocators.ZUCKERLAND_TITLE, EcoSystemPageContent.zuckerland_title_text)
        assert self.driver.current_url == 'https://pages.gymnetwork.io/ecosystem/#zuckerland'
        self.driver.get(self.url) 

        # Gym Dex link
        self.sl.click_into_link_and_Verify_page_by_element_text( self.FOOTER_GYM_DEX_LINK_FIELD, EcoSystemPageLocators.GYM_DEX_TITLE, EcoSystemPageContent.Gym_Dex_title_text)
        assert self.driver.current_url == 'https://pages.gymnetwork.io/ecosystem/#gymdex'
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
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_element_text(self.FOOTER_SUPPORT_LINK_FIELD, AtherPageLocators.CUSTOMER_SUPPORT_PAPER_TITLE, AtherPageContent.customer_support_title_text)

        # Guide LINK
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.FOOTER_GUIDE_LINK_FIELD, page_name='docs_gymnetwork' , page_title=AtherPageContent.docs_gymnetwork_title_text, timeout=10)

        # Token Contract LINK
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.FOOTER_TOKEN_CONTRACT_LINK_FIELD, page_name='Tokenomics' , page_title=AtherPageContent.Tokenomics_page_title, timeout=10)

