from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpe.AtherPageContent import AtherPageContent
from ssqatest.src.pages.locators.global_sections.JoinTelegramLocators import JoinTelegramLocators
from ssqatest.src.helpe.global_content.JoinTelegramContent import JoinTelegramContent


class JoinTelegram(JoinTelegramLocators):
    
    def __init__(self, driver, url):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
        self.url = url


    def verify_all_JoinTelegram_section_elements(self):


        #################### join telegram section  ####################
        self.sl.wait_until_element_contains_text(self.JOIN_TELEGRAM_TITLE_FIELD, JoinTelegramContent.join_telegram_title_text)
        self.sl.wait_until_element_contains_text(self.JOIN_TELEGRAM_DESC_FIELD, JoinTelegramContent.join_telegram_desc_text)
        self.sl.wait_until_element_contains_text(self.JOIN_TELEGRAM_BTN_LINK_FIELD, JoinTelegramContent.join_telegram_btn_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.JOIN_TELEGRAM_BTN_LINK_FIELD, 'href', JoinTelegramContent.join_telegram_link_href, 'join telegram link href is not correct')    
       
        # # join telegram btn
        # self.sl.click_into_link_Verify_page_by_title(self.JOIN_TELEGRAM_BTN_LINK_FIELD, AtherPageContent.telegram_page_title, page_name='telegram')
        # self.driver.get(self.url)
