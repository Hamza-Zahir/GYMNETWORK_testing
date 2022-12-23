from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpe.global_content.HeaderContent import HeaderContent
from ssqatest.src.helpe.AboutPageContent import AboutPageContent
from ssqatest.src.helpe.DashboarPageContent import DashboarPageContent
from ssqatest.src.pages.locators.BlogPageLocators import BlogPageLocators
from ssqatest.src.pages.locators.AboutPageLocators import AboutPageLocators
from ssqatest.src.helpe.ProductPageContent import ProductPageContent 
from ssqatest.src.helpe.BlogPageContent import BlogPageContent 
from ssqatest.src.pages.locators.ProductsPageLocators import ProductsPageLocators
from ssqatest.src.pages.locators.EcoSystemPageLocators import EcoSystemPageLocators
from ssqatest.src.helpe.EcoSystemPageContent import EcoSystemPageContent
from ssqatest.src.pages.locators.global_sections.HeaderLocators import HeaderLocators
from ssqatest.src.pages.locators.DashboardPageLocators import DashboardPageLocators

class Header(HeaderLocators):
    
    def __init__(self, driver, url):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
        self.url = url
        

    def verify_all_Header_elements(self):

        
        #################### header ####################
        self.sl.wait_and_check_attribute_value_is_correct(self.LOGO_FIELD, 'src', HeaderContent.logo, 'logo is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.HOME_LINK_FIELD, 'href', HeaderContent.logo_href, 'Home link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.PRODUCTS_LINK_FIELD, 'href', HeaderContent.products_href, 'products href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.ECO_SYSTEM_LINK_FIELD, 'href', HeaderContent.ecosystem_href, 'ecosystem href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.ABOUT_LINK_FIELD, 'href', HeaderContent.about_href, 'about href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.BLOG_LINK_FIELD, 'href', HeaderContent.blog_href, 'blog href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.LAUNCH_LINK_FIELD, 'href', HeaderContent.dashboard_href, 'launch APP link href is not correct')
        # product link
        self.sl.click_into_link_and_Verify_page_by_element_text(self.PRODUCTS_LINK_FIELD, ProductsPageLocators.LANDING_TITLE_FIELD, ProductPageContent.landing_title_text, timeout=10)
        self.sl.wait_and_click(self.CUSTOM_SELECT_FIELD)
        self.sl.wait_and_click(self.CHINESE_LINK_FIELD)
        self.sl.wait_until_element_contains_text(ProductsPageLocators.LANDING_TITLE_FIELD, ProductPageContent.landing_title_chinese_text)
        
        self.driver.get(self.url)
        # eco system link
        self.sl.click_into_link_and_Verify_page_by_element_text(self.ECO_SYSTEM_LINK_FIELD, EcoSystemPageLocators.LANDING_TITLE_FIELD, EcoSystemPageContent.landing_title_text, timeout=10)
        self.sl.wait_and_click(self.CUSTOM_SELECT_FIELD)
        self.sl.wait_and_click(self.CHINESE_LINK_FIELD)
        self.sl.wait_until_element_contains_text(EcoSystemPageLocators.LANDING_TITLE_FIELD, EcoSystemPageContent.landing_title_chinese_text)

        self.driver.get(self.url)
        # about link
        self.sl.click_into_link_and_Verify_page_by_element_text(self.ABOUT_LINK_FIELD, AboutPageLocators.LANDING_TITLE_FIELD, AboutPageContent.landing_title_text, timeout=15)
        self.sl.wait_and_click(self.CUSTOM_SELECT_FIELD)
        self.sl.wait_and_click(self.CHINESE_LINK_FIELD)
        self.sl.wait_until_element_contains_text(AboutPageLocators.LANDING_TITLE_FIELD, AboutPageContent.landing_title_chinese_text)

        self.driver.get(self.url)
        # blog link
        self.sl.click_into_link_and_Verify_page_by_element_text(self.BLOG_LINK_FIELD, BlogPageLocators.LANDING_TITLE_FIELD, BlogPageContent.landing_title_text, timeout=15)
        self.sl.wait_and_click(self.CUSTOM_SELECT_FIELD)
        self.sl.wait_and_click(self.CHINESE_LINK_FIELD)
        self.sl.wait_until_element_contains_text(BlogPageLocators.LANDING_TITLE_FIELD, BlogPageContent.landing_title_chinese_text)

        self.driver.get(self.url)
        # Launch APP link 
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_element_text(self.LAUNCH_LINK_FIELD, DashboardPageLocators.HEADER_TITLE, DashboarPageContent.header_title_text)


        
    