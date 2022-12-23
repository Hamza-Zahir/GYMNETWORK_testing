import pytest
from ssqatest.src.pages.ProductsPage import ProductPage
from ssqatest.src.SeleniumExtended import SeleniumExtended

@pytest.mark.usefixtures("init_driver")
class TestApp:

    @pytest.mark.tcid3
    def test_products_Page_elements(self):

        Product_Page = ProductPage(self.driver)
        self.sl = SeleniumExtended(self.driver)  
        
        Product_Page.open_Produc_page()
        Product_Page.verify_all_Product_Page_elements()


        import pdb; pdb.set_trace()
      
        
      
