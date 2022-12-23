import pytest
from ssqatest.src.pages.AboutPage import AboutPage

@pytest.mark.usefixtures("init_driver")
class TestApp:

    @pytest.mark.tcid5
    def test_About_Page_elements(self):

        About_Page = AboutPage(self.driver)

        About_Page.open_About_page()
        About_Page.verify_all_About_Page_elements()


        import pdb; pdb.set_trace()
      
        
      
