import pytest
from ssqatest.src.pages.BlogPage import BlogPage

@pytest.mark.usefixtures("init_driver")
class TestApp:

    @pytest.mark.tcid6
    def test_Blog_Page_elements(self):

        Blog_Page = BlogPage(self.driver)

        Blog_Page.open_Blog_page()
        Blog_Page.verify_all_Blog_Page_elements()


        import pdb; pdb.set_trace()
      
        
      
