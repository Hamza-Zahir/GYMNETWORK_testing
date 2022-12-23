from ssqatest.src.pages.locators.AboutPageLocators import AboutPageLocators
from ssqatest.src.pages.locators.AtherPageLocators import AtherPageLocators
from ssqatest.src.pages.locators.BlogPageLocators import BlogPageLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpe.AboutPageContent import AboutPageContent 
from ssqatest.src.helpe.BlogPageContent import BlogPageContent 
from ssqatest.src.helpe.DashboarPageContent import DashboarPageContent 
from ssqatest.src.pages.locators.DashboardPageLocators import DashboardPageLocators
from ssqatest.src.pages.components.Footer import Footer
from ssqatest.src.pages.components.Header import Header
from ssqatest.src.helpe.AtherPageContent import AtherPageContent



class AboutPage(AboutPageLocators):
    
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://pages.gymnetwork.io/about/"
        self.sl = SeleniumExtended(self.driver)
        self.Header_section = Header(self.driver, self.url)
        self.Footer_section = Footer(self.driver, self.url)


    def open_About_page(self):
        self.driver.get(self.url)


    def verify_all_About_Page_elements(self):

        ################## header ####################
        self.Header_section.verify_all_Header_elements()


        #################### landing section ####################
        self.sl.wait_until_element_contains_text(self.LANDING_TITLE_FIELD, AboutPageContent.landing_title_text)
        self.sl.wait_until_element_contains_text(self.LANDING_DESC_FIELD, AboutPageContent.landing_desc_text)
        self.sl.wait_until_element_contains_text(self.LANDING_BTN_FIELD, AboutPageContent.landing_btn_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.LANDING_BTN_FIELD, 'href', AboutPageContent.landing_btn_href, 'Launch APP btn link is not correct')
        self.sl.check_value_of_css_property(self.LANDING_SECTION_FIELD, 'background-image', AboutPageContent.landing_section_bg_img, 'header landing background image is not correct')
        # Launch APP btn 
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_element_text(self.LANDING_BTN_FIELD, DashboardPageLocators.HEADER_TITLE, DashboarPageContent.header_title_text)
    

        #################### Appeared on section ####################
        # Appeared on
        self.sl.wait_until_element_contains_text(self.APPEARED_ON_TITLE_FIELD, AboutPageContent.Appeared_on_title_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.APPEARED_ON_BITCOINIST_FIELD, 'href', AboutPageContent.Appeared_on_bitcoinist_href, 'Appeared_on bitcoinist link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.APPEARED_ON_LIVE_BITCOIN_NEWS_FIELD, 'href', AboutPageContent.Appeared_on_live_bitcoin_news_href, 'Appeared_on live_bitcoin link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.APPEARED_ON_NEWSBTC_1_FIELD, 'href', AboutPageContent.Appeared_on_newsbtc_1_href, 'Appeared_on newsbtc_1 link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.APPEARED_ON_DIGITAL_JOURNAL_FIELD, 'href', AboutPageContent.Appeared_on_digital_journal_href, 'Appeared_on digital link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.APPEARED_ON_MARKRT_WATCH_FIELD, 'href', AboutPageContent.Appeared_on_markrt_watch_href, 'Appeared_on markrt_watch link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.APPEARED_ON_INVESTING_LINK_FIELD, 'href', AboutPageContent.Appeared_on_investing_href, 'Appeared_on investing link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.APPEARED_ON_BLOCKONOMI_FIELD, 'href', AboutPageContent.Appeared_on_blockonomi_href, 'Appeared_on blockonomi link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.APPEARED_ON_BENZINGA_FIELD, 'href', AboutPageContent.Appeared_on_benzinga_href, 'Appeared_on link benzinga href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.APPEARED_ON_YAHOO_FINANCE_FIELD, 'href', AboutPageContent.Appeared_on_yahoo_finance_href, 'Appeared_on yahoo_finance link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.APPEARED_ON_CRYPTO_DAILY_FIELD, 'href', AboutPageContent.Appeared_on_crypto_daily_href, 'Appeared_on crypto_daily link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.APPEARED_ON_NEWSBTC_2_FIELD, 'href', AboutPageContent.Appeared_on_newsbtc_2_href, 'Appeared_on newsbtc_2 link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.APPEARED_ON_U_TODAY_FIELD, 'href', AboutPageContent.Appeared_on_Utoday_href, 'Appeared_on Utoday link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.APPEARED_ON_CRYPTO_POTATO_FIELD, 'href', AboutPageContent.Appeared_on_crypto_potato_href, 'Appeared_on crypto_potato link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.APPEARED_ON_CRYPTONEWS_FIELD, 'href', AboutPageContent.Appeared_on_cryptonews_href, 'Appeared_on cryptonews link href is not correct')
       
        # bitcoinist link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.APPEARED_ON_BITCOINIST_FIELD, page_name='Bitcoinist.com', page_title=AtherPageContent.bitcoinist_title_page)
        # livebitcoinnews link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.APPEARED_ON_LIVE_BITCOIN_NEWS_FIELD, page_name='livebitcoinnews.com', page_title=AtherPageContent.livebitcoinnews_title_page)
        # # newsbtc link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.APPEARED_ON_NEWSBTC_1_FIELD, page_name='newsbtc.com', page_title=AtherPageContent.newsbtc_1_title_page)
        # digitaljournal link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.APPEARED_ON_DIGITAL_JOURNAL_FIELD, page_name='digitaljournal.com', page_title=AtherPageContent.digitaljournal_title_page)
        # marketwatch link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_element_text(self.APPEARED_ON_MARKRT_WATCH_FIELD, AtherPageLocators.MARKETWATCH_DESC_FIELD, AtherPageContent.marketwatch_desc_text)
        # investing link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.APPEARED_ON_INVESTING_LINK_FIELD, page_name='investing.com', page_title=AtherPageContent.investing_title_page)
        # blockonomi link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.APPEARED_ON_BLOCKONOMI_FIELD, page_name='blockonomi.com', page_title=AtherPageContent.blockonomi_title_page)
        # benzinga.com page
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_element_text(self.APPEARED_ON_BENZINGA_FIELD, AtherPageLocators.BENZINGA_TITLE_TEXT, AtherPageContent.benzinga_title)
        # finance.yahoo link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.APPEARED_ON_YAHOO_FINANCE_FIELD, page_name='finance.yahoo.com', page_title=AtherPageContent.finance_yahoo_title_page)
        # cryptodaily link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.APPEARED_ON_CRYPTO_DAILY_FIELD, page_name='cryptodaily.co', page_title=AtherPageContent.cryptodaily_title_page)
        # newsbtc link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.APPEARED_ON_NEWSBTC_2_FIELD, page_name='newsbtc.com', page_title=AtherPageContent.newsbtc_2_title_page)
        # u.today link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.APPEARED_ON_U_TODAY_FIELD, page_name='u.today', page_title=AtherPageContent.u_today_title_page)
        # cryptopotato link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.APPEARED_ON_CRYPTO_POTATO_FIELD, page_name='cryptopotato.com', page_title=AtherPageContent.cryptopotato_title_page)
        # crypto.news link
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_element_text(self.APPEARED_ON_CRYPTONEWS_FIELD, AtherPageLocators.CRYPTO_LOGO_TEXT, AtherPageContent.crypto_logo)



        ################### Our mission section ####################
        # Our mission
        self.sl.wait_until_element_contains_text(self.OUR_MISSION_TITLE_FIELD, AboutPageContent.Our_mission_title_text)

        self.sl.wait_until_element_contains_text(self.OUR_MISSION_CARD1_DESC_FIELD, AboutPageContent.Our_mission_card1_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.OUR_MISSION_CARD1_IMG_FIELD, 'src', AboutPageContent.Our_mission_card1_img_src, 'Our mission card1 img is not correct')

        self.sl.wait_until_element_contains_text(self.OUR_MISSION_CARD2_DESC_FIELD, AboutPageContent.Our_mission_card2_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.OUR_MISSION_CARD2_IMG_FIELD, 'src', AboutPageContent.Our_mission_card2_img_src, 'Our mission card2 img is not correct')

        self.sl.wait_until_element_contains_text(self.OUR_MISSION_CARD3_DESC_FIELD, AboutPageContent.Our_mission_card3_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.OUR_MISSION_CARD3_IMG_FIELD, 'src', AboutPageContent.Our_mission_card3_img_src, 'Our mission card3 img is not correct')

        self.sl.wait_until_element_contains_text(self.OUR_MISSION_CARD4_DESC_FIELD, AboutPageContent.Our_mission_card4_desc_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.OUR_MISSION_CARD4_IMG_FIELD, 'src', AboutPageContent.Our_mission_card4_img_src, 'Our mission card4 img is not correct')

        ################### DAO section ####################
        self.sl.wait_until_element_contains_text(self.DAO_TITLE_FIELD, AboutPageContent.DAO_title_text)
        self.sl.wait_until_element_contains_text(self.DAO_DESC1_FIELD, AboutPageContent.DAO_desc1_text)
        self.sl.wait_until_element_contains_text(self.DAO_DESC2_FIELD, AboutPageContent.DAO_desc2_text)
        self.sl.wait_until_element_contains_text(self.DAO_DESC3_FIELD, AboutPageContent.DAO_desc3_text)
        self.sl.check_value_of_css_property(self.DAO_SECTION_FIELD, 'background-image', AboutPageContent.DAO_section_img_bg, 'DAO section background image is not correct')
        
        
        ################### Team section ####################
        self.sl.wait_until_element_contains_text(self.TEAM_TITLE_FIELD, AboutPageContent.Team_title_text)
        self.sl.wait_until_element_contains_text(self.TEAM_DESC_FIELD, AboutPageContent.Team_desc_text)

        self.sl.wait_and_check_attribute_value_is_correct(self.TEAM_CARD1_IMG_FIELD, 'src', AboutPageContent.Team_card1_img_src, 'Team card1 img is not correct')
        self.sl.wait_until_element_contains_text(self.TEAM_CARD1_NAME_FIELD, AboutPageContent.Team_card1_name)
        self.sl.wait_until_element_contains_text(self.TEAM_CARD1_POSITION_FIELD, AboutPageContent.Team_card1_position)
       
        self.sl.wait_and_check_attribute_value_is_correct(self.TEAM_CARD2_IMG_FIELD, 'src', AboutPageContent.Team_card2_img_src, 'Team card2 img is not correct')
        self.sl.wait_until_element_contains_text(self.TEAM_CARD2_NAME_FIELD, AboutPageContent.Team_card2_name)
        self.sl.wait_until_element_contains_text(self.TEAM_CARD2_POSITION_FIELD, AboutPageContent.Team_card2_position)
       
        self.sl.wait_and_check_attribute_value_is_correct(self.TEAM_CARD3_IMG_FIELD, 'src', AboutPageContent.Team_card3_img_src, 'Team card3 img is not correct')
        self.sl.wait_until_element_contains_text(self.TEAM_CARD3_NAME_FIELD, AboutPageContent.Team_card3_name)
        self.sl.wait_until_element_contains_text(self.TEAM_CARD3_POSITION_FIELD, AboutPageContent.Team_card3_position)
       
        self.sl.wait_and_check_attribute_value_is_correct(self.TEAM_CARD4_IMG_FIELD, 'src', AboutPageContent.Team_card4_img_src, 'Team card4 img is not correct')
        self.sl.wait_until_element_contains_text(self.TEAM_CARD4_NAME_FIELD, AboutPageContent.Team_card4_name)
        self.sl.wait_until_element_contains_text(self.TEAM_CARD4_POSITION_FIELD, AboutPageContent.Team_card4_position)
       
        self.sl.scrollIntoView_and_click(self.TEAM_CARD4_FIELD)

        # ux/ui section 
        self.sl.wait_until_element_contains_text(self.UX_UI_TITLE_FIELD, AboutPageContent.UxUi_title_text)

        self.sl.wait_and_check_attribute_value_is_correct(self.UX_UI_CARD1_IMG_FIELD, 'src', AboutPageContent.UxUi_card1_img_src, 'ux/ui card1 img is not correct')
        self.sl.wait_until_element_contains_text(self.UX_UI_CARD1_NAME_FIELD, AboutPageContent.UxUi_card1_name)
        self.sl.wait_until_element_contains_text(self.UX_UI_CARD1_POSITION_FIELD, AboutPageContent.UxUi_card1_position)
        self.sl.wait_until_element_contains_text(self.UX_UI_CARD1_DESC_FIELD, AboutPageContent.UxUi_card1_desc)

        self.sl.wait_and_check_attribute_value_is_correct(self.UX_UI_CARD2_IMG_FIELD, 'src', AboutPageContent.UxUi_card2_img_src, 'ux/ui card2 img is not correct')
        self.sl.wait_until_element_contains_text(self.UX_UI_CARD2_NAME_FIELD, AboutPageContent.UxUi_card2_name)
        self.sl.wait_until_element_contains_text(self.UX_UI_CARD2_POSITION_FIELD, AboutPageContent.UxUi_card2_position)
        self.sl.wait_until_element_contains_text(self.UX_UI_CARD2_DESC_FIELD, AboutPageContent.UxUi_card2_desc)

        self.sl.wait_and_check_attribute_value_is_correct(self.UX_UI_CARD3_IMG_FIELD, 'src', AboutPageContent.UxUi_card3_img_src, 'ux/ui card3 img is not correct')
        self.sl.wait_until_element_contains_text(self.UX_UI_CARD3_NAME_FIELD, AboutPageContent.UxUi_card3_name)
        self.sl.wait_until_element_contains_text(self.UX_UI_CARD3_POSITION_FIELD, AboutPageContent.UxUi_card3_position)
        self.sl.wait_until_element_contains_text(self.UX_UI_CARD3_DESC_FIELD, AboutPageContent.UxUi_card3_desc)

        ################### tokenomics section ####################
        self.sl.wait_until_element_contains_text(self.TOKENOMICS_TITLE_FIELD, AboutPageContent.tokenomics_title_text)
        self.sl.wait_until_element_contains_text(self.TOKENOMICS_DESC_FIELD, AboutPageContent.tokenomics_desc_text)
        self.sl.wait_until_element_contains_text(self.TOKENOMICS_DESC_SPAN_FIELD, AboutPageContent.tokenomics_desc_span_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.TOKENOMICS_LOGO_FIELD, 'src', AboutPageContent.tokenomics_desc_logo_src, 'tokenomics desc logo is not correct')
        self.sl.check_value_of_css_property(self.TOKENOMICS_BG_FIELD, 'background-image', AboutPageContent.tokenomics_bg_img, 'tokenomics section background image is not correct')

        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE1_NUM_FIELD, AboutPageContent.supply_slide1_num)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE1_TITLE_FIELD, AboutPageContent.supply_slide1_title)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE1_PERCENT_FIELD, AboutPageContent.supply_slide1_percent)

        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE2_NUM_FIELD, AboutPageContent.supply_slide2_num)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE2_TITLE_FIELD, AboutPageContent.supply_slide2_title)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE2_PERCENT_FIELD, AboutPageContent.supply_slide2_percent)

        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE3_NUM_FIELD, AboutPageContent.supply_slide3_num)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE3_TITLE_FIELD, AboutPageContent.supply_slide3_title)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE3_PERCENT_FIELD, AboutPageContent.supply_slide3_percent)

        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE4_NUM_FIELD, AboutPageContent.supply_slide4_num)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE4_TITLE_FIELD, AboutPageContent.supply_slide4_title)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE4_PERCENT_FIELD, AboutPageContent.supply_slide4_percent)

        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE5_NUM_FIELD, AboutPageContent.supply_slide5_num)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE5_TITLE_FIELD, AboutPageContent.supply_slide5_title)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE5_PERCENT_FIELD, AboutPageContent.supply_slide5_percent)

        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE6_NUM_FIELD, AboutPageContent.supply_slide6_num)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE6_TITLE_FIELD, AboutPageContent.supply_slide6_title)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE6_PERCENT_FIELD, AboutPageContent.supply_slide6_percent)

        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE7_NUM_FIELD, AboutPageContent.supply_slide7_num)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE7_TITLE_FIELD, AboutPageContent.supply_slide7_title)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE7_PERCENT_FIELD, AboutPageContent.supply_slide7_percent)

        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE8_NUM_FIELD, AboutPageContent.supply_slide8_num)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE8_TITLE_FIELD, AboutPageContent.supply_slide8_title)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE8_PERCENT_FIELD, AboutPageContent.supply_slide8_percent)

        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE9_NUM_FIELD, AboutPageContent.supply_slide9_num)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE9_TITLE_FIELD, AboutPageContent.supply_slide9_title)
        self.sl.wait_until_element_contains_text(self.SUPPLY_SLIDE9_PERCENT_FIELD, AboutPageContent.supply_slide9_percent)

        ################### more section ####################
        self.sl.wait_until_element_contains_text(self.MORE_TITLE_FIELD, AboutPageContent.more_title_text)

        self.sl.wait_until_element_contains_text(self.GUIDE_TITLE_FIELD, AboutPageContent.guide_title_text)
        self.sl.wait_until_element_contains_text(self.GUIDE_DESC_FIELD, AboutPageContent.guide_desc_text)
        self.sl.wait_until_element_contains_text(self.GUIDE_LINK_FIELD, AboutPageContent.guide_link_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.GUIDE_LINK_FIELD, 'href', AboutPageContent.guide_link_href, 'guide link href is not correct')
        # Guide LINK
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.GUIDE_LINK_FIELD, page_name='docs_gymnetwork' , page_title=AtherPageContent.docs_gymnetwork_title_text, timeout=10)

        self.sl.wait_until_element_contains_text(self.TWITTER_TITLE_FIELD, AboutPageContent.twitter_title_text)
        self.sl.wait_until_element_contains_text(self.TWITTER_DESC_FIELD, AboutPageContent.twitter_desc_text)
        self.sl.wait_until_element_contains_text(self.TWITTER_LINK_FIELD, AboutPageContent.twitter_link_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.TWITTER_LINK_FIELD, 'href', AboutPageContent.twitter_link_href, 'twitter link href is not correct')
        # Twitter LINK
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.TWITTER_LINK_FIELD, page_name='Twitter' , page_title=AtherPageContent.Twitter_page_title, timeout=20)

        self.sl.wait_until_element_contains_text(self.TELEGRAM_TITLE_FIELD, AboutPageContent.telegram_title_text)
        self.sl.wait_until_element_contains_text(self.TELEGRAM_DESC_FIELD, AboutPageContent.telegram_desc_text)
        self.sl.wait_until_element_contains_text(self.TELEGRAM_LINK_FIELD, AboutPageContent.telegram_link_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.TELEGRAM_LINK_FIELD, 'href', AboutPageContent.telegram_link_href, 'telegram link href is not correct')
        # telegram LINK
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_title(self.TELEGRAM_LINK_FIELD, page_name='telegram' , page_title=AtherPageContent.telegram_page_title)
       
        self.sl.wait_until_element_contains_text(self.BLOG_TITLE_FIELD, AboutPageContent.blog_title_text)
        self.sl.wait_until_element_contains_text(self.BLOG_DESC_FIELD, AboutPageContent.blog_desc_text)
        self.sl.wait_until_element_contains_text(self.BLOG_LINK_FIELD, AboutPageContent.blog_link_text)
        self.sl.wait_and_check_attribute_value_is_correct(self.BLOG_LINK_FIELD, 'href', AboutPageContent.blog_link_href, 'Blog link href is not correct')
        # Blog & News LINK 
        self.sl.click_into_link_and_Verify_page_by_element_text( self.BLOG_LINK_FIELD, BlogPageLocators.LANDING_TITLE_FIELD, BlogPageContent.landing_title_text)
        self.driver.get(self.url)
        
        self.sl.wait_until_element_contains_text( self.SUPPORT_TITLE_FIELD, AboutPageContent.support_title_text)
        self.sl.wait_until_element_contains_text( self.SUPPORT_DESC_FIELD, AboutPageContent.support_desc_text)
        self.sl.wait_until_element_contains_text( self.SUPPORT_LINK_FIELD, AboutPageContent.support_link_text)
        self.sl.wait_and_check_attribute_value_is_correct( self.SUPPORT_LINK_FIELD, 'href', AboutPageContent.support_link_href, 'support link href is not correct')
        # Support LINK
        self.sl.click_to_link_and_switch_tab_and_Verify_page_by_element_text(self.SUPPORT_LINK_FIELD, AtherPageLocators.CUSTOMER_SUPPORT_PAPER_TITLE, AtherPageContent.customer_support_title_text)


        ################### footer section ####################
        self.Footer_section.verify_all_footer_elements()

