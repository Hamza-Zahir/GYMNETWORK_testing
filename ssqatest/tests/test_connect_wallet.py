import pytest
import time
from ssqatest.src.pages.DashboardPage import DashboardPage
from ssqatest.src.pages.MetamaskPage import MetamaskPage

@pytest.mark.usefixtures("init_driver_with_metamask")
class TestApp:

    @pytest.mark.tcid1
    def test_connect_wallet(self):
        Dashboard_Page = DashboardPage(self.driver)
        metamask_page = MetamaskPage(self.driver)

        all_WINDOW = self.driver.window_handles
        METAMASK_WINDOW = all_WINDOW[0]
        GYMNETWORK_WINDOW = all_WINDOW[1]


        # # login to metamask
        self.driver.switch_to.window(METAMASK_WINDOW)
        metamask_page.log_in_metamask()
        metamask_page.add_Binance_Mainnet_Network()

        
        # # open gymnetwork dashboard page  
        self.driver.switch_to.window(GYMNETWORK_WINDOW)
        Dashboard_Page.open_dashboard_page()
        
        
        # connect wallet 
        Dashboard_Page.connect_wallet()

        # switch to metamask and accept connect wallet
        self.driver.switch_to.window(METAMASK_WINDOW)
        self.driver.refresh()
        metamask_page.confirm_connecting_wallet()


        # switch to app and add network
        self.driver.switch_to.window(GYMNETWORK_WINDOW)
        Dashboard_Page.chack_referal_id_text()
       

        # # accept adding network 
        # self.driver.switch_to.window(METAMASK_WINDOW)
        # self.driver.refresh()
        # metamask_page.confirm_swetching_network()

        # # back to amazon page
        # self.driver.switch_to.window(all_WINDOW[1])
        # amazon_page.scroll_to_item_and_add_it_to_cart()

        # #  accept transiction (add item to cart)
        # self.driver.switch_to.window(METAMASK_WINDOW)
        # self.driver.refresh()
        # metamask_page.confirm_transiction()
        
        # # check if transaction confirmed
        # metamask_page.check_if_confirmed()

        # # back to amazon page and check cart item if has one item added
        # self.driver.switch_to.window(all_WINDOW[1])
        # # self.driver.refresh()
        # amazon_page.check_cart_item()
        # amazon_page.change_number_of_item()

        # # confirm transaction (change number of item)
        # self.driver.switch_to.window(METAMASK_WINDOW)
        # self.driver.refresh()
        # metamask_page.confirm_transiction()

        #  # # check if transaction confirmed
        # metamask_page.check_if_confirmed()

        # # back to amazon page
        # self.driver.switch_to.window(all_WINDOW[1])
        import pdb; pdb.set_trace()

