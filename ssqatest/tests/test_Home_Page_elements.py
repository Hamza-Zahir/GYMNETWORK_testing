import pytest
from ssqatest.src.pages.HomePage import HomePage

@pytest.mark.usefixtures("init_driver")
class TestApp:

    @pytest.mark.tcid2
    def test_Home_Page_elements(self):

        Home_Page = HomePage(self.driver)
          
        
        Home_Page.open_home_page_and_verify_title()
        Home_Page.copy_contract_address_and_verify_if_coped_successfully()
        self.driver.switch_to.window(self.driver.window_handles[0])
        Home_Page.verify_all_home_page_elements()


        import pdb; pdb.set_trace()
      
        
      
