
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time



class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 15

    def wait_and_input(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()
        except StaleElementReferenceException:
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()
    
    
    def scrollIntoView_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
            )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)


    def wait_and_check_attribute_value_is_correct(self, locator, attribute_name, attribute_value, error_messag, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        attribute_value_result = element.get_attribute(attribute_name)
        assert attribute_value_result == attribute_value, error_messag


    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        ) 


    def check_value_of_css_property(self, locator, css_property, value_of_css_property, error_messag, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        value_of_css_property_result = element.value_of_css_property(css_property)
        assert value_of_css_property_result == value_of_css_property, error_messag
   
    def wait_and_pest_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(Keys.CONTROL, 'v')


    def wait_and_enter(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(Keys.ENTER)

    def click_to_link_and_switch_tab_and_Verify_page_by_title(self, link_locator, page_name, page_title, timeout= None):
        
        self.scrollIntoView_and_click(link_locator)
        self.driver.switch_to.window(self.driver.window_handles[1])  
        if timeout:
            time.sleep(timeout)
        assert self.driver.title == page_title, f'{page_name} page is not correct'     
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])


    def click_to_link_and_switch_tab_and_Verify_page_by_element_text(self, link_locator, element_locator, element_text):
        
        self.scrollIntoView_and_click(link_locator)
        self.driver.switch_to.window(self.driver.window_handles[1])  
        self.wait_until_element_contains_text(element_locator, element_text)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])


    def click_to_link_and_switch_tab_and_Verify_page_by_logo(self, link_locator, page_name, logo_locator=None, logo_src=None):
        
        self.scrollIntoView_and_click(link_locator)
        self.driver.switch_to.window(self.driver.window_handles[1])  
        self.wait_and_check_attribute_value_is_correct(logo_locator, 'src', logo_src, f'{page_name} page is not correct')   
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])


    def click_into_link_and_Verify_page_by_element_text(self, link_locator, element_locator, element_text, timeout= None):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.scrollIntoView_and_click(link_locator)
        if timeout:
            time.sleep(timeout)

        self.wait_until_element_contains_text(element_locator, element_text)
        
        
    def click_into_link_Verify_page_by_title(self, link_locator, page_title, page_name, timeout= None):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.scrollIntoView_and_click(link_locator)
        if timeout:
            time.sleep(timeout)

        assert self.driver.title == page_title, f'{page_name} page is not correct'     
       

    def click_into_link_and_Verify_page_by_logo(self, link_locator, page_name, logo_locator=None, logo_src=None):
        self.scrollIntoView_and_click(link_locator)
        self.wait_and_check_attribute_value_is_correct(logo_locator, 'src', logo_src, f'{page_name} page is not correct')   


    def wait_until_invisibility(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )



    # ...................................................................

    
    def wait_to_be_clickable_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            el = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(locator)
                )
            el.click()
        except StaleElementReferenceException:
            time.sleep(2)
            el = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(locator)
                )
            el.click()



    def wait_and_get_attribute_value(self, locator, attribute_name, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        attribute_value = element.get_attribute(attribute_name)
        return attribute_value




    def wait_until_element_is_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

     

    def select_option_from_selector(self, selector_locator, option_value, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        selector_element = WebDriverWait(self.driver, timeout).until(
                                EC.visibility_of_element_located(selector_locator)
                            )
        select = Select(selector_element)
        select.select_by_value(option_value)


    def wait_and_get_elements(self, locator, timeout=None, err=None):
        timeout = timeout if timeout else self.default_timeout
        err = err if err else f"Unable to find elements located by '{locator}'," \
                                f"after timeout of {timeout}"
        try:
            elements =  WebDriverWait(self.driver, timeout).until(
                            EC.visibility_of_all_elements_located(locator)
                        ) 
        except TimeoutException:
            raise TimeoutException(err)
        
        return elements

    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        elm = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
              )
        elment_text = elm.text

        return elment_text
    