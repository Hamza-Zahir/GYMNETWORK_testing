from ssqatest.src.pages.locators.EcoSystemPageLocators import EcoSystemPageLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpe.EcoSystemPageContent import EcoSystemPageContent 
from ssqatest.src.helpe.DashboarPageContent import DashboarPageContent 
from ssqatest.src.pages.locators.DashboardPageLocators import DashboardPageLocators
from ssqatest.src.pages.components.Footer import Footer
from ssqatest.src.pages.components.Header import Header
from ssqatest.src.pages.components.JoinTelegramSection import JoinTelegram
from ssqatest.src.pages.locators.global_sections.JoinTelegramLocators import JoinTelegramLocators
from ssqatest.src.helpe.AtherPageContent import AtherPageContent



class EcoSystemPage(EcoSystemPageLocators):
    
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://pages.gymnetwork.io/ecosystem/"
        self.sl = SeleniumExtended(self.driver)
        self.Header_section = Header(self.driver, self.url)
        self.Footer_section = Footer(self.driver, self.url)
        self.JoinTelegram_section = JoinTelegram(self.driver, self.url)


    def open_Produc_page(self):
        self.driver.get(self.url)


    def verify_all_EcoSystem_Page_elements(self):

        ################### header ####################
        self.Header_section.verify_all_Header_elements()


        #################### landing section ####################
        self.sl.wait_until_element_contains_text(self.LANDING_TITLE_FIELD, EcoSystemPageContent.landing_title_text)
        self.sl.wait_until_element_contains_text(self.LANDING_DESC_FIELD, EcoSystemPageContent.landing_desc_text)
        self.sl.wait_until_element_contains_text(self.LANDING_BTN_FIELD, EcoSystemPageContent.landing_btn_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.LANDING_BTN_FIELD, 'href', EcoSystemPageContent.landing_btn_href, 'Launch APP btn link is not correct')
        self.sl.check_value_of_css_property(self.LANDING_SECTION_FIELD, 'background-image', EcoSystemPageContent.landing_background_img_src, 'landing background image is not correct')
        # Launch APP btn 
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_element_text(self.LANDING_BTN_FIELD, DashboardPageLocators.HEADER_TITLE, DashboarPageContent.header_title_text)
        
        
        #################### gym-network section ####################

        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_TITLE_FIELD, EcoSystemPageContent.gym_network_title_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_DESC_FIELD, EcoSystemPageContent.gym_network_desc_text)

        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD1_NUM_FIELD, EcoSystemPageContent.gym_network_card1_num_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD1_TITLE_FIELD, EcoSystemPageContent.gym_network_card1_title_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD1_DESC_FIELD, EcoSystemPageContent.gym_network_card1_desc_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD1_LINK, EcoSystemPageContent.gym_network_card1_link_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.GYM_NETWORK_CARD1_LINK, 'href', EcoSystemPageContent.gym_network_card1_link_href, f'{EcoSystemPageContent.gym_network_card1_title_text} link href is not correct')

        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD2_NUM_FIELD, EcoSystemPageContent.gym_network_card2_num_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD2_TITLE_FIELD, EcoSystemPageContent.gym_network_card2_title_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD2_DESC_FIELD, EcoSystemPageContent.gym_network_card2_desc_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD2_LINK, EcoSystemPageContent.gym_network_card2_link_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.GYM_NETWORK_CARD2_LINK, 'href', EcoSystemPageContent.gym_network_card2_link_href, f'{EcoSystemPageContent.gym_network_card2_title_text} link href is not correct')

        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD3_NUM_FIELD, EcoSystemPageContent.gym_network_card3_num_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD3_TITLE_FIELD, EcoSystemPageContent.gym_network_card3_title_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD3_DESC_FIELD, EcoSystemPageContent.gym_network_card3_desc_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD3_LINK, EcoSystemPageContent.Coming_Soon)

        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD4_NUM_FIELD, EcoSystemPageContent.gym_network_card4_num_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD4_TITLE_FIELD, EcoSystemPageContent.gym_network_card4_title_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD4_DESC_FIELD, EcoSystemPageContent.gym_network_card4_desc_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD4_LINK, EcoSystemPageContent.Coming_Soon)

        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD5_NUM_FIELD, EcoSystemPageContent.gym_network_card5_num_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD5_TITLE_FIELD, EcoSystemPageContent.gym_network_card5_title_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD5_DESC_FIELD, EcoSystemPageContent.gym_network_card5_desc_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD5_LINK, EcoSystemPageContent.gym_network_card5_link_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.GYM_NETWORK_CARD5_LINK, 'href', EcoSystemPageContent.gym_network_card5_link_href, f'{EcoSystemPageContent.gym_network_card5_title_text} link href is not correct')

        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD6_NUM_FIELD, EcoSystemPageContent.gym_network_card6_num_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD6_TITLE_FIELD, EcoSystemPageContent.gym_network_card6_title_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD6_DESC_FIELD, EcoSystemPageContent.gym_network_card6_desc_text)
        self.sl.wait_until_element_contains_text(self.GYM_NETWORK_CARD6_LINK, EcoSystemPageContent.Coming_Soon)

        # More about Gymstreet link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.GYM_NETWORK_CARD1_LINK, page_name='gymstreet.io', page_title=AtherPageContent.gymstreet_title_page)
        # MetaBlocks link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.GYM_NETWORK_CARD2_LINK, page_name='MetaBlocks.io', page_title=AtherPageContent.MetaBlocks_title_page)
        # Go to Gym DEX link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_element_text(self.GYM_NETWORK_CARD5_LINK , DashboardPageLocators.HEADER_TITLE, DashboarPageContent.header_title_text)


        #################### carousel section ####################
        # carousel_section-menu
        self.sl.wait_until_element_contains_text(self.GYMSTREET_link, EcoSystemPageContent.gymstreet_link_text)
        self.sl.wait_until_element_contains_text(self.METABLOCKS_link, EcoSystemPageContent.metablocks_link_text)
        self.sl.wait_until_element_contains_text(self.CASH_FT_link, EcoSystemPageContent.CashFT_link_text)
        self.sl.wait_until_element_contains_text(self.ZUCKERLAND_link, EcoSystemPageContent.zuckerland_link_text)
        self.sl.wait_until_element_contains_text(self.GYM_DEX_link, EcoSystemPageContent.Gym_Dex_link_text)
        self.sl.wait_until_element_contains_text(self.METAVERSE_link, EcoSystemPageContent.metaverse_link_text)

      
        # gymstreet section 
        self.sl.scrollIntoView_and_click(self.GYMSTREET_link)
        self.sl.wait_until_element_contains_text(self.GYMSTREET_TITLE, EcoSystemPageContent.gymstreet_title_text)
        self.sl.wait_until_element_contains_text(self.GYMSTREET_DESC1, EcoSystemPageContent.gymstreet_desc1_text)
        self.sl.wait_until_element_contains_text(self.GYMSTREET_DESC2, EcoSystemPageContent.gymstreet_desc2_text)
        self.sl.wait_until_element_contains_text(self.GYMSTREET_DESC3, EcoSystemPageContent.gymstreet_desc3_text)
        self.sl.wait_until_element_contains_text(self.GYMSTREET_DESC4, EcoSystemPageContent.gymstreet_desc4_text)
        self.sl.wait_until_element_contains_text(self.GYMSTREET_BTN, EcoSystemPageContent.gymstreet_btn_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.GYMSTREET_BTN, 'href', EcoSystemPageContent.gymstreet_btn_href, 'gymstreet btn href link is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.GYMSTREET_IMG, 'src', EcoSystemPageContent.gymstreet_img_src, 'gymstreet img src is not correct')
        # gymstreet btn
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.GYMSTREET_BTN, page_name='gymstreet.io', page_title=AtherPageContent.gymstreet_title_page)


        # metablocks section
        self.sl.scrollIntoView_and_click(self.METABLOCKS_link)
        self.sl.wait_until_element_contains_text(self.METABLOCKS_TITLE, EcoSystemPageContent.metablocks_title_text)
        self.sl.wait_until_element_contains_text(self.METABLOCKS_DESC1, EcoSystemPageContent.metablocks_desc1_text)
        self.sl.wait_until_element_contains_text(self.METABLOCKS_DESC2, EcoSystemPageContent.metablocks_desc2_text)
        self.sl.wait_until_element_contains_text(self.METABLOCKS_DESC3, EcoSystemPageContent.metablocks_desc3_text)
        self.sl.wait_until_element_contains_text(self.METABLOCKS_BTN, EcoSystemPageContent.Coming_Soon)
        self.sl.wait_and_check_attribute_value_is_correct(self.METABLOCKS_IMG, 'src', EcoSystemPageContent.metablocks_img_src, 'metablocks img src is not correct')
    
        # CashFT section
        self.sl.scrollIntoView_and_click(self.CASH_FT_link)
        self.sl.wait_until_element_contains_text(self.CASH_FT_TITLE, EcoSystemPageContent.CashFT_title_text)
        self.sl.wait_until_element_contains_text(self.CASH_FT_DESC1, EcoSystemPageContent.CashFT_desc1_text)
        self.sl.wait_until_element_contains_text(self.CASH_FT_LI1, EcoSystemPageContent.CashFT_li1_text)
        self.sl.wait_until_element_contains_text(self.CASH_FT_LI2, EcoSystemPageContent.CashFT_li2_text)
        self.sl.wait_until_element_contains_text(self.CASH_FT_LI3, EcoSystemPageContent.CashFT_li3_text)
        self.sl.wait_until_element_contains_text(self.CASH_FT_LI4, EcoSystemPageContent.CashFT_li4_text)
        self.sl.wait_until_element_contains_text(self.CASH_FT_DESC2, EcoSystemPageContent.CashFT_desc2_text)
        self.sl.wait_until_element_contains_text(self.CASH_FT_BTN, EcoSystemPageContent.Coming_Soon)
        self.sl.wait_and_check_attribute_value_is_correct(self.CASH_FT_IMG, 'src', EcoSystemPageContent.CashFT_img_src, 'CashFT img src is not correct')

        # zuckerland section 
        self.sl.scrollIntoView_and_click(self.ZUCKERLAND_link)
        self.sl.wait_until_element_contains_text(self.ZUCKERLAND_TITLE, EcoSystemPageContent.zuckerland_title_text)
        self.sl.wait_until_element_contains_text(self.ZUCKERLAND_DESC1, EcoSystemPageContent.zuckerland_desc1_text)
        self.sl.wait_until_element_contains_text(self.ZUCKERLAND_DESC2, EcoSystemPageContent.zuckerland_desc2_text)
        self.sl.wait_until_element_contains_text(self.ZUCKERLAND_DESC3, EcoSystemPageContent.zuckerland_desc3_text)
        self.sl.wait_until_element_contains_text(self.ZUCKERLAND_BTN, EcoSystemPageContent.Coming_Soon)
        self.sl.wait_and_check_attribute_value_is_correct(self.ZUCKERLAND_IMG, 'src', EcoSystemPageContent.zuckerland_img_src, 'zuckerland img src is not correct')
   
        # Gym Dex section
        self.sl.scrollIntoView_and_click(self.GYM_DEX_link)
        self.sl.wait_until_element_contains_text(self.GYM_DEX_TITLE, EcoSystemPageContent.Gym_Dex_title_text)
        self.sl.wait_until_element_contains_text(self.GYM_DEX_DESC, EcoSystemPageContent.Gym_Dex_desc_text)
        self.sl.wait_until_element_contains_text(self.GYM_DEX_BTN, EcoSystemPageContent.Gym_Dex_btn_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.GYM_DEX_BTN, 'href', EcoSystemPageContent.Gym_Dex_btn_href, 'Gym_Dex btn href link is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.GYM_DEX_IMG, 'src', EcoSystemPageContent.Gym_Dex_img_src, 'Gym_Dex img src is not correct')
        # Gym_Dex limk
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_element_text(self.GYM_DEX_BTN, DashboardPageLocators.HEADER_TITLE, DashboarPageContent.header_title_text)

        # metaverse-campus section 
        self.sl.scrollIntoView_and_click(self.METAVERSE_link)
        self.sl.wait_until_element_contains_text(self.METAVERSE_CAMPUS_TITLE, EcoSystemPageContent.metaverse_title_text)
        self.sl.wait_until_element_contains_text(self.METAVERSE_CAMPUS_DESC1, EcoSystemPageContent.metaverse_desc1_text)
        self.sl.wait_until_element_contains_text(self.METAVERSE_CAMPUS_DESC2, EcoSystemPageContent.metaverse_desc2_text)
        self.sl.wait_until_element_contains_text(self.METAVERSE_CAMPUS_DESC3, EcoSystemPageContent.metaverse_desc3_text)
        self.sl.wait_until_element_contains_text(self.METAVERSE_CAMPUS_BTN, EcoSystemPageContent.Coming_Soon)
        self.sl.wait_and_check_attribute_value_is_correct(self.METAVERSE_CAMPUS_IMG, 'src', EcoSystemPageContent.metaverse_img_src, 'metaverse img src is not correct')

        #################### get started section ####################
        self.sl.wait_until_element_contains_text(self.GET_STARTED_TITLE_FIELD, EcoSystemPageContent.get_started_title_text)

        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD1_NUM_FIELD, EcoSystemPageContent.get_started_card1_num)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD1_TITLE_FIELD, EcoSystemPageContent.get_started_card1_title_text)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD1_DESC_FIELD, EcoSystemPageContent.get_started_card1_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.GET_STARTED_CARD1_IMG_FIELD, 'src', EcoSystemPageContent.get_started_card1_img_src, 'get started card1 img src is not correct')    
        self.sl.wait_and_check_attribute_value_is_correct(self.GET_STARTED_CARD1_LINK, 'href', EcoSystemPageContent.get_started_card1_link_href, 'get started card1 link href is not correct')    

        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD2_NUM_FIELD, EcoSystemPageContent.get_started_card2_num)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD2_TITLE_FIELD, EcoSystemPageContent.get_started_card2_title_text)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD2_DESC_FIELD, EcoSystemPageContent.get_started_card2_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.GET_STARTED_CARD2_LINK, 'href', EcoSystemPageContent.get_started_card2_link_href, 'get started card2 link href is not correct')    

        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD3_NUM_FIELD, EcoSystemPageContent.get_started_card3_num)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD3_TITLE_FIELD, EcoSystemPageContent.get_started_card3_title_text)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD3_DESC_FIELD, EcoSystemPageContent.get_started_card3_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.GET_STARTED_CARD3_LINK, 'href', EcoSystemPageContent.get_started_card3_link_href, 'get started card3 link href is not correct')    

        self.sl.wait_until_element_contains_text(self.START_DIRECTLY_BTN, EcoSystemPageContent.Start_directly)

        # choose a crypto wallet link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.GET_STARTED_CARD1_LINK, page_name='choose_a_crypto_wallet_video', page_title=AtherPageContent.choose_a_crypto_wallet_video_page_title)

        # make your deposit link   
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.GET_STARTED_CARD2_LINK, page_name='make_your_deposit_link_video', page_title=AtherPageContent.make_your_deposit_video_page_title)

        # connect your wallet link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.GET_STARTED_CARD3_LINK, page_name='connect_your_wallet_video', page_title=AtherPageContent.connect_your_wallet_video_page_title)

        # Start directly link
        self.sl.scrollIntoView_and_click(self.START_DIRECTLY_BTN)
        assert self.driver.current_url == 'https://pages.gymnetwork.io/ecosystem/#gymstreet'
        

        ################## join telegram section  ####################
        self.JoinTelegram_section.verify_all_JoinTelegram_section_elements()
        # join telegram btn
        self.sl.click_into_link_Verify_page_by_title( JoinTelegramLocators.JOIN_TELEGRAM_BTN_LINK_FIELD, AtherPageContent.telegram_page_title, page_name='telegram')
        self.driver.get(self.url)


        ################### footer section ####################
        self.Footer_section.verify_all_footer_elements()