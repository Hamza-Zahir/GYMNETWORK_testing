from ssqatest.src.pages.locators.DashboardPageLocators import DashboardPageLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended
import time
class DashboardPage(DashboardPageLocators):
    
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def open_dashboard_page(self):
        self.driver.get('https://gymnetwork.io/dashboard')



    def connect_wallet(self):
        self.sl.scrollIntoView_and_click(self.CONNECT_WALLET_BTN)
        self.sl.wait_and_click(self.METAMASK_BTN)
        time.sleep(2)
    

    def chack_referal_id_text(self):
        time.sleep(4)
        wallet_btn_text = self.sl.wait_and_get_text(self.CONNECT_WALLET_BTN)
        assert wallet_btn_text != 'Connect Wallet', f'{wallet_btn_text} the wallet is not connected yet'
       
        sponsor_id_message = 'Dear visitor, your current sponsor ID is xkyqk. You can still change it by using a new referral link. Make your first deposit in one of the vaults to finalise your registration.'
        sponsor_id_text = self.sl.wait_and_get_text(self.SPONSOR_ID_INFO)
        assert sponsor_id_text == sponsor_id_message, 'SPONSOR ID INFO text not correct'
        
 

   