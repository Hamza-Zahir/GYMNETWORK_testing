from selenium.webdriver.common.by import By


class MetamaskPageLocators:
    GET_STARTED_BTN = (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/button') 
    IMPORT_WALLET_BTN = (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button')
    NO_THANKS_BTN = (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]') 
    PASSWORD_FIELD = (By.ID, 'password') 
    CONFIRM_PASSWORD_FIELD = (By.ID, 'confirm-password') 
    AGREE_CHECKBOX_FIELD = (By.XPATH, '//*[@id="create-new-vault__terms-checkbox"]')
    IMPOER_BTN = (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/form/button')
    ALL_DONE_BTN = (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/button')
    CONFERM_NEXT_BTN = (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]')
    CONFERM_CONNECT_BTN = (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]')
    CONFERM_APPROVE_BTN = (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/button[2]')
    CONFERM_SWETCH_NETWORK_BTN = (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/button[2]')
    CONFERM_TRANSICTION_BTN = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[5]/div[3]/footer/button[2]')
    TRANSACTION_COMPLETED = (By.CSS_SELECTOR, '.transaction-list__completed-transactions .list-item')
    PENDING_TRANSACTIONS_LIST = (By.CLASS_NAME, 'transaction-list__pending-transactions')
    STATUS_OF_TRANSACTION = (By.XPATH, '//*[@id="popover-content"]/div/div/section/div[2]/div/div[2]/div[1]/div[2]/div')
    CLOSE_CARD_BTN = (By.XPATH, '//*[@id="popover-content"]/div/div/section/div[1]/div/button')
    ACCOUNT_MENU_BTN = (By.XPATH, '//*[@id="app-content"]/div/div[1]/div/div[2]/div[2]')
    SETTINGS_BTN = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div[11]')
    NETWORKS_BTN = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[1]/div/button[6]/div')
    ADD_NETWORK_BTN = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/button')
    NETWORK_NAME_INPUT = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input')
    EPC_URL_INPUT = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input')
    CHAIN_ID_INPUT = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input')
    SYMPOL_INPUT = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/label/input')
    SAVE_NETWORK_BTN = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]')

    

