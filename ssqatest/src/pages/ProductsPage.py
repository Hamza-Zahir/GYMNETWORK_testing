from ssqatest.src.pages.locators.ProductsPageLocators import ProductsPageLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpe.ProductPageContent import ProductPageContent 
from ssqatest.src.helpe.DashboarPageContent import DashboarPageContent 
from ssqatest.src.pages.locators.DashboardPageLocators import DashboardPageLocators
from ssqatest.src.pages.components.Footer import Footer
from ssqatest.src.pages.components.Header import Header
from ssqatest.src.pages.components.JoinTelegramSection import JoinTelegram
from ssqatest.src.pages.locators.global_sections.JoinTelegramLocators import JoinTelegramLocators
from ssqatest.src.helpe.AtherPageContent import AtherPageContent



class ProductPage(ProductsPageLocators):
    
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://pages.gymnetwork.io/products/"
        self.sl = SeleniumExtended(self.driver)
        self.Header_section = Header(self.driver, self.url)
        self.Footer_section = Footer(self.driver, self.url)
        self.JoinTelegram_section = JoinTelegram(self.driver, self.url)


    def open_Produc_page(self):
        self.driver.get(self.url)


    def verify_all_Product_Page_elements(self):

        ################### header ####################
        self.Header_section.verify_all_Header_elements()


        #################### landing section ####################
        self.sl.wait_until_element_contains_text(self.LANDING_TITLE_FIELD, ProductPageContent.landing_title_text)
        self.sl.wait_until_element_contains_text(self.LANDING_DESC_FIELD, ProductPageContent.landing_desc_text)
        self.sl.wait_until_element_contains_text(self.LAUNCH_APP_BTN, ProductPageContent.Launch_APP_btn_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.LAUNCH_APP_BTN, 'href', ProductPageContent.Launch_APP_btn_href, 'Launch APP btn link is not correct')
        self.sl.check_value_of_css_property(self.LANDING_SECTION_FIELD, 'background-image', ProductPageContent.landing_background_img, 'header landing background image is not correct')
        # Launch APP btn 
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_element_text(self.LAUNCH_APP_BTN, DashboardPageLocators.HEADER_TITLE, DashboarPageContent.header_title_text)


        #################### earning section ####################
        self.sl.wait_until_element_contains_text(self.EARNING_TITLE_FIELD, ProductPageContent.earning_title_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.EARNING_IMG_FIELD, 'src', ProductPageContent.earning_img_src, 'earning img src is not correct')


        #################### products section ####################
        self.sl.wait_until_element_contains_text(self.PRODUCTS_TITLE_FIELD, ProductPageContent.products_title_text)

        self.sl.wait_until_element_contains_text(self.PRODUCTS_CARD1_TITLE_FIELD, ProductPageContent.products_card1_title_text)
        self.sl.wait_until_element_contains_text(self.PRODUCTS_CARD1_DESC_FIELD, ProductPageContent.products_card1_desc_text)
        self.sl.wait_until_element_contains_text(self.PRODUCTS_CARD1_BTN_FIELD, ProductPageContent.products_card1_btn_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.PRODUCTS_CARD1_BTN_FIELD, 'href', ProductPageContent.products_card1_btn_href, 'products card1 btn link is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.PRODUCTS_CARD1_IMG_FIELD, 'src', ProductPageContent.products_card1_img_src, 'products card1 img src is not correct')

        self.sl.wait_until_element_contains_text(self.PRODUCTS_CARD2_TITLE_FIELD, ProductPageContent.products_card2_title_text)
        self.sl.wait_until_element_contains_text(self.PRODUCTS_CARD2_DESC_FIELD, ProductPageContent.products_card2_desc_text)
        self.sl.wait_until_element_contains_text(self.PRODUCTS_CARD2_BTN_FIELD, ProductPageContent.products_card2_btn_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.PRODUCTS_CARD2_BTN_FIELD, 'href', ProductPageContent.products_card2_btn_href, 'products card2 btn link is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.PRODUCTS_CARD2_IMG_FIELD, 'src', ProductPageContent.products_card2_img_src, 'products card2 img src is not correct')

        self.sl.wait_until_element_contains_text(self.PRODUCTS_CARD3_TITLE_FIELD, ProductPageContent.products_card3_title_text)
        self.sl.wait_until_element_contains_text(self.PRODUCTS_CARD3_DESC_FIELD, ProductPageContent.products_card3_desc_text)
        self.sl.wait_until_element_contains_text(self.PRODUCTS_CARD3_BTN_FIELD, ProductPageContent.products_card3_btn_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.PRODUCTS_CARD3_BTN_FIELD, 'href', ProductPageContent.products_card3_btn_href, 'products card3 btn link is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.PRODUCTS_CARD3_IMG_FIELD, 'src', ProductPageContent.products_card3_img_src, 'products card3 img src is not correct')

        self.sl.wait_until_element_contains_text(self.PRODUCTS_CARD4_TITLE_FIELD, ProductPageContent.products_card4_title_text)
        self.sl.wait_until_element_contains_text(self.PRODUCTS_CARD4_DESC_FIELD, ProductPageContent.products_card4_desc_text)
        self.sl.wait_until_element_contains_text(self.PRODUCTS_CARD4_BTN_FIELD, ProductPageContent.products_card4_btn_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.PRODUCTS_CARD4_BTN_FIELD, 'href', ProductPageContent.products_card4_btn_href, 'products card4 btn link is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.PRODUCTS_CARD4_IMG_FIELD, 'src', ProductPageContent.products_card4_img_src, 'products card4 img src is not correct')



        #################### vault section ####################
        self.sl.wait_until_element_contains_text(self.VAULT_TITLE_FIELD, ProductPageContent.vault_title_text)
        self.sl.wait_until_element_contains_text(self.VAULT_DESC1_FIELD, ProductPageContent.vault_desc1_text)
        self.sl.wait_until_element_contains_text(self.VAULT_DESC2_FIELD, ProductPageContent.vault_desc2_text)

        #################### vault next section ####################
        self.sl.wait_until_element_contains_text(self.VAULT_NEXT_DESC1_FIELD, ProductPageContent.vault_next_desc1_text)
        self.sl.wait_until_element_contains_text(self.VAULT_NEXT_DESC2_FIELD, ProductPageContent.vault_next_desc2_text)
        self.sl.wait_until_element_contains_text(self.VAULT_NEXT_BTN_FIELD, ProductPageContent.vault_next_btn_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.VAULT_NEXT_BTN_FIELD, 'href', ProductPageContent.vault_next_btn_href, 'vault_next start now btn href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.VAULT_NEXT_IMG_FIELD, 'src', ProductPageContent.vault_next_img_src, 'vault_next img src is not correct')
        self.sl.check_value_of_css_property(self.VAULT_NEXT_SECTION_FIELD, 'background-image', ProductPageContent.vault_next_section_bg_img_src, 'vault_next section background image is not correct')
        # Start now btn 
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_element_text(self.VAULT_NEXT_BTN_FIELD, DashboardPageLocators.HEADER_TITLE, DashboarPageContent.header_title_text)


        #################### Farming section ####################
        self.sl.wait_until_element_contains_text(self.FARMING_BTN_FIELD, ProductPageContent.farming_title_text)
       
        self.sl.wait_until_element_contains_text(self.SINGLE_POOL_TITLE_FIELD, ProductPageContent.sigle_pool_title_text)
        self.sl.wait_until_element_contains_text(self.SINGLE_POOL_DESC_FIELD, ProductPageContent.sigle_pool_desc_text)
        self.sl.wait_until_element_contains_text(self.SINGLE_POOL_START_BTN_FIELD, ProductPageContent.Start_now_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.SINGLE_POOL_START_BTN_FIELD, 'href', ProductPageContent.sigle_pool_btn_href, 'sigle_pool start now btn href is not correct')
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_element_text(self.SINGLE_POOL_START_BTN_FIELD, DashboardPageLocators.HEADER_TITLE, DashboarPageContent.header_title_text)
       
        self.sl.scrollIntoView_and_click(self.FARMING_BTN_FIELD)

        self.sl.wait_until_element_contains_text(self.SINGLE_POOL_BTN_FIELD, ProductPageContent.sigle_pool_title_text)
       
        self.sl.wait_until_element_contains_text(self.FARMING_TITLE_FIELD, ProductPageContent.farming_title_text)
        self.sl.wait_until_element_contains_text(self.FARMING_DESC_FIELD, ProductPageContent.farming_desc_text)
        self.sl.wait_until_element_contains_text(self.FARMING_BTN_START_FIELD, ProductPageContent.Start_now_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.FARMING_BTN_START_FIELD, 'href', ProductPageContent.farming_btn_href, 'farming start now btn href is not correct')
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_element_text(self.FARMING_BTN_START_FIELD, DashboardPageLocators.HEADER_TITLE, DashboarPageContent.header_title_text)
       

        #################### holder section ####################
        self.sl.wait_until_element_contains_text(self.HOLDER_TITLE_FIELD, ProductPageContent.holder_title_text)
        self.sl.wait_until_element_contains_text(self.HOLDER_CARD1_TITLE_FIELD, ProductPageContent.holder_card1_title_text)
        self.sl.wait_until_element_contains_text(self.HOLDER_CARD1_DESC_FIELD, ProductPageContent.holder_card1_desc_text)
        self.sl.wait_until_element_contains_text(self.HOLDER_CARD2_TITLE_FIELD, ProductPageContent.holder_card2_title_text)
        self.sl.wait_until_element_contains_text(self.HOLDER_CARD2_DESC_FIELD, ProductPageContent.holder_card2_desc_text)

        self.sl.wait_until_element_contains_text(self.HOLDER_CARD3_TITLE_FIELD, ProductPageContent.holder_card3_title_text)
        self.sl.wait_until_element_contains_text(self.HOLDER_CARD3_DESC1_FIELD, ProductPageContent.holder_card3_desc1_text)
        self.sl.wait_until_element_contains_text(self.HOLDER_CARD3_DESC2_FIELD, ProductPageContent.holder_card3_desc2_text)

        self.sl.wait_until_element_contains_text(self.HOLDER_CARD4_TITLE_FIELD, ProductPageContent.holder_card4_title_text)
        self.sl.wait_until_element_contains_text(self.HOLDER_CARD4_DESC_FIELD, ProductPageContent.holder_card4_desc_text)



        #################### get started section ####################
        self.sl.wait_until_element_contains_text(self.GET_STARTED_TITLE_FIELD, ProductPageContent.get_started_title_text)

        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD1_NUM_FIELD, ProductPageContent.get_started_card1_num)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD1_TITLE_FIELD, ProductPageContent.get_started_card1_title_text)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD1_DESC_FIELD, ProductPageContent.get_started_card1_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.GET_STARTED_CARD1_IMG_FIELD, 'src', ProductPageContent.get_started_card1_img_src, 'get started card1 img src is not correct')    
        self.sl.wait_and_check_attribute_value_is_correct(self.GET_STARTED_CARD1_LINK, 'href', ProductPageContent.get_started_card1_link_href, 'get started card1 link href is not correct')    

        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD2_NUM_FIELD, ProductPageContent.get_started_card2_num)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD2_TITLE_FIELD, ProductPageContent.get_started_card2_title_text)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD2_DESC_FIELD, ProductPageContent.get_started_card2_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.GET_STARTED_CARD2_IMG_FIELD, 'src', ProductPageContent.get_started_card2_img_src, 'get started card2 img src is not correct')    
        self.sl.wait_and_check_attribute_value_is_correct(self.GET_STARTED_CARD2_LINK, 'href', ProductPageContent.get_started_card2_link_href, 'get started card2 link href is not correct')    

        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD3_NUM_FIELD, ProductPageContent.get_started_card3_num)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD3_TITLE_FIELD, ProductPageContent.get_started_card3_title_text)
        self.sl.wait_until_element_contains_text(self.GET_STARTED_CARD3_DESC_FIELD, ProductPageContent.get_started_card3_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.GET_STARTED_CARD3_IMG_FIELD, 'src', ProductPageContent.get_started_card3_img_src, 'get started card3 img src is not correct')    
        self.sl.wait_and_check_attribute_value_is_correct(self.GET_STARTED_CARD3_LINK, 'href', ProductPageContent.get_started_card3_link_href, 'get started card3 link href is not correct')    

        # choose a crypto wallet link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.GET_STARTED_CARD1_LINK, page_name='choose_a_crypto_wallet_video', page_title=AtherPageContent.choose_a_crypto_wallet_video_page_title)

        # make your deposit link   
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.GET_STARTED_CARD2_LINK, page_name='make_your_deposit_link_video', page_title=AtherPageContent.make_your_deposit_video_page_title)

        # connect your wallet link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.GET_STARTED_CARD3_LINK, page_name='connect_your_wallet_video', page_title=AtherPageContent.connect_your_wallet_video_page_title)


        ################## join telegram section  ####################
        self.JoinTelegram_section.verify_all_JoinTelegram_section_elements()
        # join telegram btn
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(JoinTelegramLocators.JOIN_TELEGRAM_BTN_LINK_FIELD, page_name='telegram' , page_title=AtherPageContent.telegram_page_title)

        ################### footer section ####################
        self.Footer_section.verify_all_footer_elements()