import pytest
from ssqatest.src.pages.EcoSystemPage import EcoSystemPage

@pytest.mark.usefixtures("init_driver")
class TestApp:

    @pytest.mark.tcid4
    def test_EcoSystem_Page_elements(self):

        EcoSystem_Page = EcoSystemPage(self.driver)
       
        
        EcoSystem_Page.open_Produc_page()
        EcoSystem_Page.verify_all_EcoSystem_Page_elements()


        import pdb; pdb.set_trace()
      
        
      
