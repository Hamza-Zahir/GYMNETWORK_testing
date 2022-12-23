from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.components.Footer import Footer
from ssqatest.src.pages.components.Header import Header

from ssqatest.src.pages.locators.BlogPageLocators import BlogPageLocators
from ssqatest.src.pages.locators.what_is_gymnetworkPageLocators import WhatIsGymnetworkPageLocators
from ssqatest.src.pages.locators.Earn_money_with_gym_networkPageLocators import EarnMoneyWithGymnetworkPageLocators
from ssqatest.src.pages.locators.Gym_Street_And_Ecosystem_PageLocators import GymStreetAndEcosystemPageLocators
from ssqatest.src.pages.locators.Gymstreet_most_innovative_defi_projectPageLocators import GymstreetMostInnovativePageLocators
from ssqatest.src.pages.locators.Metaverse_And_Potential_PageLocators import MetaverseAndPotentialPageLocators
from ssqatest.src.helpe.BlogPageContent import BlogPageContent 
from ssqatest.src.helpe.what_is_gymnetworkPageContent import WhatIsGymnetworkContent 
from ssqatest.src.helpe.Earn_money_with_gym_networkPageContent import EarnMoneyWithGymNetworkContent 
from ssqatest.src.helpe.Gym_street_and_its_ecosystemContent import GymStreetAndEcosystemContent 
from ssqatest.src.helpe.Gymstreet_most_innovative_defi_projectPageContent import GymstreetMostInnovativeDefiProjectContent 
from ssqatest.src.helpe.Metaverse_and_its_potentialPageContent import MetaverseAndPotentialContent 





class BlogPage(BlogPageLocators):
    
    def __init__(self, driver):
        self.driver = driver
        
        self.url = "https://pages.gymnetwork.io/blog/"
        self.sl = SeleniumExtended(self.driver)
        self.Header_section = Header(self.driver, self.url)
        self.Footer_section = Footer(self.driver, self.url)


    def open_Blog_page(self):
        self.driver.get(self.url)


    def verify_all_Blog_Page_elements(self):

        ################## header ####################
        self.Header_section.verify_all_Header_elements()


        #################### landing section ####################
        self.sl.wait_until_element_contains_text(self.LANDING_TITLE_FIELD, BlogPageContent.landing_title_text)
        self.sl.wait_until_element_contains_text(self.LANDING_DESC_FIELD, BlogPageContent.landing_desc_text)

        self.sl.wait_and_check_attribute_value_is_correct(self.LANDING_LINK_FIELD, 'href', BlogPageContent.landing_link_href, 'landing link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.LANDING_LINK_IMG_FIELD, 'src', BlogPageContent.landing_link_img_src, 'landing link img src is not correct')
        self.sl.wait_until_element_contains_text(self.LANDING_LINK_TITLE_FIELD, BlogPageContent.landing_link_title_text)
        self.sl.wait_until_element_contains_text(self.LANDING_LINK_DESC_FIELD, BlogPageContent.landing_link_desc_text)
        self.sl.wait_until_element_contains_text(self.LANDING_LINK_DATE_FIELD, BlogPageContent.landing_link_date_text)
        # landing btn 
        self.sl.click_into_link_and_Verify_page_by_element_text(self.LANDING_LINK_FIELD, EarnMoneyWithGymnetworkPageLocators.TITLE_FIELD, EarnMoneyWithGymNetworkContent.title_tetx, timeout=15)
        assert self.driver.current_url == 'https://pages.gymnetwork.io/blog/how-can-you-earn-money-with-gym-network'
        self.driver.get(self.url)


        # blogs container
        self.sl.wait_until_element_contains_text(self.DROPDOWN_BTN, BlogPageContent.Latest_articles_btn_text)

        self.sl.wait_and_check_attribute_value_is_correct(self.CARD1_LINK_FIELD, 'href', BlogPageContent.what_is_gymnetwork_href, 'what_is_gymnetwork link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.CARD1_LINK_IMG_FIELD, 'src', BlogPageContent.what_is_gymnetwork_img_src, 'what_is_gymnetwork img src is not correct')
        self.sl.wait_until_element_contains_text(self.CARD1_LINK_TITLE_FIELD, BlogPageContent.what_is_gymnetwork_title_text)
        self.sl.wait_until_element_contains_text(self.CARD1_LINK_DESC_FIELD, BlogPageContent.what_is_gymnetwork_desc_text)
        self.sl.wait_until_element_contains_text(self.CARD1_LINK_DATE_FIELD, BlogPageContent.what_is_gymnetwork_date_text)

        self.sl.wait_and_check_attribute_value_is_correct(self.CARD2_LINK_FIELD, 'href', BlogPageContent.metaverse_and_its_potential_href, 'metaverse_and_its_potential link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.CARD2_LINK_IMG_FIELD, 'src', BlogPageContent.metaverse_and_its_potential_img_src, 'metaverse_and_its_potential link img src is not correct')
        self.sl.wait_until_element_contains_text(self.CARD2_LINK_TITLE_FIELD, BlogPageContent.metaverse_and_its_potential_title_text)
        self.sl.wait_until_element_contains_text(self.CARD2_LINK_DESC_FIELD, BlogPageContent.metaverse_and_its_potential_desc_text)
        self.sl.wait_until_element_contains_text(self.CARD2_LINK_DATE_FIELD, BlogPageContent.metaverse_and_its_potential_date_text)

        self.sl.wait_and_check_attribute_value_is_correct(self.CARD3_LINK_FIELD, 'href', BlogPageContent.gym_street_and_its_ecosystem_href, 'gym_street_and_its_ecosystem link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.CARD3_LINK_IMG_FIELD, 'src', BlogPageContent.gym_street_and_its_ecosystem_img_src, 'gym_street_and_its_ecosystem link img src is not correct')
        self.sl.wait_until_element_contains_text(self.CARD3_LINK_TITLE_FIELD, BlogPageContent.gym_street_and_its_ecosystem_title_text)
        self.sl.wait_until_element_contains_text(self.CARD3_LINK_DESC_FIELD, BlogPageContent.gym_street_and_its_ecosystem_desc_text)
        self.sl.wait_until_element_contains_text(self.CARD3_LINK_DATE_FIELD, BlogPageContent.gym_street_and_its_ecosystem_date_text)
         
        self.sl.wait_and_check_attribute_value_is_correct(self.CARD4_LINK_FIELD, 'href', BlogPageContent.earn_money_with_gym_network_href, 'earn_money_with_gym_network link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.CARD4_LINK_IMG_FIELD, 'src', BlogPageContent.earn_money_with_gym_network_img_src, 'earn_money_with_gym_network link img src is not correct')
        self.sl.wait_until_element_contains_text(self.CARD4_LINK_TITLE_FIELD, BlogPageContent.earn_money_with_gym_network_title_text)
        self.sl.wait_until_element_contains_text(self.CARD4_LINK_DESC_FIELD, BlogPageContent.earn_money_with_gym_network_desc_text)
        self.sl.wait_until_element_contains_text(self.CARD4_LINK_DATE_FIELD, BlogPageContent.earn_money_with_gym_network_date_text)
        
        self.sl.wait_and_check_attribute_value_is_correct(self.CARD5_LINK_FIELD, 'href', BlogPageContent.gymstreet_most_innovative_defi_project_href, 'gymstreet_most_innovative_defi_project link href is not correct')
        self.sl.wait_and_check_attribute_value_is_correct(self.CARD5_LINK_IMG_FIELD, 'src', BlogPageContent.gymstreet_most_innovative_defi_project_img_src, 'gymstreet_most_innovative_defi_project link img src is not correct')
        self.sl.wait_until_element_contains_text(self.CARD5_LINK_TITLE_FIELD, BlogPageContent.gymstreet_most_innovative_defi_project_title_text)
        self.sl.wait_until_element_contains_text(self.CARD5_LINK_DESC_FIELD, BlogPageContent.gymstreet_most_innovative_defi_project_desc_text)
        self.sl.wait_until_element_contains_text(self.CARD5_LINK_DATE_FIELD, BlogPageContent.gymstreet_most_innovative_defi_project_date_text)
        

        self.sl.scrollIntoView_and_click(self.DROPDOWN_BTN)
        self.sl.wait_and_click(self.NEWEST_FIRST_BTN)
        self.sl.wait_until_element_contains_text(self.DROPDOWN_BTN, BlogPageContent.Newest_first_btn_text)

        self.sl.wait_until_element_contains_text(self.CARD1_LINK_TITLE_FIELD, BlogPageContent.earn_money_with_gym_network_title_text)
        self.sl.wait_until_element_contains_text(self.CARD2_LINK_TITLE_FIELD, BlogPageContent.what_is_gymnetwork_title_text)
        self.sl.wait_until_element_contains_text(self.CARD3_LINK_TITLE_FIELD, BlogPageContent.metaverse_and_its_potential_title_text)
        self.sl.wait_until_element_contains_text(self.CARD4_LINK_TITLE_FIELD, BlogPageContent.gym_street_and_its_ecosystem_title_text)
        self.sl.wait_until_element_contains_text(self.CARD5_LINK_TITLE_FIELD, BlogPageContent.gymstreet_most_innovative_defi_project_title_text)


        self.sl.scrollIntoView_and_click(self.DROPDOWN_BTN)

        self.sl.wait_and_click(self.LASTES_ARTICLES_BTN)
        self.sl.wait_until_element_contains_text(self.DROPDOWN_BTN, BlogPageContent.Latest_articles_btn_text)

        self.sl.wait_until_element_contains_text(self.CARD1_LINK_TITLE_FIELD, BlogPageContent.gymstreet_most_innovative_defi_project_title_text)
        self.sl.wait_until_element_contains_text(self.CARD2_LINK_TITLE_FIELD, BlogPageContent.what_is_gymnetwork_title_text)
        self.sl.wait_until_element_contains_text(self.CARD3_LINK_TITLE_FIELD, BlogPageContent.metaverse_and_its_potential_title_text)
        self.sl.wait_until_element_contains_text(self.CARD4_LINK_TITLE_FIELD, BlogPageContent.gym_street_and_its_ecosystem_title_text)
        self.sl.wait_until_element_contains_text(self.CARD5_LINK_TITLE_FIELD, BlogPageContent.earn_money_with_gym_network_title_text)

        self.sl.scrollIntoView_and_click(self.DROPDOWN_BTN)
        self.sl.wait_and_click(self.MOST_POPULAR_BTN)
        self.sl.wait_until_element_contains_text(self.DROPDOWN_BTN, BlogPageContent.Most_popular_btn_text)

        self.sl.wait_until_element_contains_text(self.CARD1_LINK_TITLE_FIELD, BlogPageContent.earn_money_with_gym_network_title_text)
        self.sl.wait_until_element_contains_text(self.CARD2_LINK_TITLE_FIELD, BlogPageContent.what_is_gymnetwork_title_text)
        self.sl.wait_until_element_contains_text(self.CARD3_LINK_TITLE_FIELD, BlogPageContent.metaverse_and_its_potential_title_text)
        self.sl.wait_until_element_contains_text(self.CARD4_LINK_TITLE_FIELD, BlogPageContent.gym_street_and_its_ecosystem_title_text)
        self.sl.wait_until_element_contains_text(self.CARD5_LINK_TITLE_FIELD, BlogPageContent.gymstreet_most_innovative_defi_project_title_text)

        self.driver.refresh()
        self.sl.click_into_link_and_Verify_page_by_element_text(self.CARD1_LINK_TITLE_FIELD, WhatIsGymnetworkPageLocators.TITLE_FIELD, WhatIsGymnetworkContent.title_tetx)
        self.driver.get(self.url)

        self.sl.click_into_link_and_Verify_page_by_element_text(self.CARD2_LINK_TITLE_FIELD, MetaverseAndPotentialPageLocators.TITLE_FIELD, MetaverseAndPotentialContent.title_tetx)
        self.driver.get(self.url)

        self.sl.click_into_link_and_Verify_page_by_element_text(self.CARD3_LINK_TITLE_FIELD, GymStreetAndEcosystemPageLocators.TITLE_FIELD, GymStreetAndEcosystemContent.title_tetx)
        self.driver.get(self.url)

        self.sl.click_into_link_and_Verify_page_by_element_text(self.CARD4_LINK_TITLE_FIELD, EarnMoneyWithGymnetworkPageLocators.TITLE_FIELD, EarnMoneyWithGymNetworkContent.title_tetx)
        self.driver.get(self.url)

        self.sl.click_into_link_and_Verify_page_by_element_text(self.CARD5_LINK_TITLE_FIELD, GymstreetMostInnovativePageLocators.TITLE_FIELD, GymstreetMostInnovativeDefiProjectContent.title_tetx)
        self.driver.get(self.url)

    
        ################### footer section ####################
        self.Footer_section.verify_all_footer_elements()

