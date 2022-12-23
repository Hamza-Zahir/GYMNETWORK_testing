from ssqatest.src.pages.locators.MetamaskPageLocators import MetamaskPageLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.configs.generic_configs import GeneticConfigs
from selenium.webdriver.common.by import By
import time

class MetamaskPage(MetamaskPageLocators):
    
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)


    def set_secret_recover_pharse(self):

        secret_wrds = GeneticConfigs.SECRET_RECOVERY_PHRASE
        password = GeneticConfigs.NEW_PASSWORD

        for X in range(12):
            inputId = f"import-srp__srp-word-{X}"
            self.sl.wait_and_input((By.ID, inputId),secret_wrds[X])

        self.sl.wait_and_input(self.PASSWORD_FIELD, password)
        self.sl.wait_and_input(self.CONFIRM_PASSWORD_FIELD, password)


    def log_in_metamask(self):

        self.sl.wait_and_click(self.GET_STARTED_BTN)
        self.sl.wait_and_click(self.IMPORT_WALLET_BTN)
        self.sl.wait_and_click(self.NO_THANKS_BTN)
        self.set_secret_recover_pharse()
        self.sl.wait_and_click(self.AGREE_CHECKBOX_FIELD)
        self.sl.wait_and_click(self.IMPOER_BTN)
        self.sl.wait_and_click(self.ALL_DONE_BTN)
        self.sl.wait_and_click(self.CLOSE_CARD_BTN)
        
    
    def add_Binance_Mainnet_Network(self):
        Network_nam = 'Binance Smart Chain Mainnet'
        New_RPC_URL = 'https://bsc-dataseed.binance.org/'
        Chain_ID = 56
        Currency_symbol = 'BNB'
     
        self.sl.wait_and_click(self.ACCOUNT_MENU_BTN)
        self.sl.wait_and_click(self.SETTINGS_BTN)
        self.sl.wait_and_click(self.NETWORKS_BTN)
        self.sl.wait_and_click(self.ADD_NETWORK_BTN)
        self.sl.wait_and_input(self.NETWORK_NAME_INPUT, Network_nam)
        self.sl.wait_and_input(self.EPC_URL_INPUT, New_RPC_URL)
        self.sl.wait_and_input(self.CHAIN_ID_INPUT, Chain_ID)
        self.sl.wait_and_input(self.SYMPOL_INPUT, Currency_symbol)
        self.sl.wait_and_click(self.SAVE_NETWORK_BTN)




    def confirm_connecting_wallet(self):
        self.sl.wait_and_click(self.CONFERM_NEXT_BTN)
        self.sl.wait_and_click(self.CONFERM_CONNECT_BTN)

    # def confirm_swetching_network(self):
    #     self.sl.wait_and_click(self.CONFERM_APPROVE_BTN)
    #     self.sl.wait_and_click(self.CONFERM_SWETCH_NETWORK_BTN)

    # def confirm_transiction(self):
    #     self.sl.wait_and_click(self.CONFERM_TRANSICTION_BTN)
    #     time.sleep(4)

    # def check_if_confirmed(self):
    #     # self.sl.wait_until_element_is_visible(self.PENDING_TRANSACTIONS_LIST)
    #     self.sl.wait_until_invisibility(self.PENDING_TRANSACTIONS_LIST)
    #     self.sl.wait_and_click(self.TRANSACTION_COMPLETED)
    #     time.sleep(2)
    #     self.sl.wait_until_element_contains_text(self.STATUS_OF_TRANSACTION, 'Confirmed')
        