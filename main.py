from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class UrbanRoutesPage:
    # Localizadores con nombres descriptivos
    origin_input = (By.ID, 'from')
    destination_input = (By.ID, 'to')
    request_taxi_button = (By.CLASS_NAME, "button round")
    comfort_option_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    phone_number_field = (By.ID, 'phone')
    next_button = (By.XPATH, '//*[text()="Siguiente"]')
    code_input_field = (By.ID, 'code')
    add_card_button = (By.CLASS_NAME, "pp-plus")
    card_number_field = (By.XPATH, '//*[@id="number"]')
    card_cvv_field = (By.XPATH, '//div[@class="card-code-input"]/input[@id="code"]')
    add_card_confirm_button = (By.XPATH, '//*[text()="Agregar"]')
    message_for_driver_field = (By.CSS_SELECTOR, "#comment")
    blanket_request_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    ice_cream_increase_button = (By.CLASS_NAME, "counter-plus")
    confirm_button = (By.XPATH, '//*[text()="Confirmar"]')
    order_summary_modal = (By.CLASS_NAME, "order-details")
    def __init__(self, driver):
        self.driver = driver
    def set_origin(self, address):
        self.driver.find_element(*self.origin_input).send_keys(address)
    def set_destination(self, address):
        self.driver.find_element(*self.destination_input).send_keys(address)
    def request_taxi(self):
        self.driver.find_element(*self.request_taxi_button).click()
    def select_comfort_option(self):
        self.driver.find_element(*self.comfort_option_button).click()
    def enter_phone_number(self, phone):
        self.driver.find_element(*self.phone_number_field).send_keys(phone)
    def click_next(self):
        self.driver.find_element(*self.next_button).click()
    def add_credit_card(self, card_number, cvv):
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.card_number_field).send_keys(card_number)
        self.driver.find_element(*self.card_cvv_field).send_keys(cvv)
        self.driver.find_element(*self.add_card_confirm_button).click()
    def write_message_to_driver(self, message):
        self.driver.find_element(*self.message_for_driver_field).send_keys(message)
    def request_blanket(self):
        self.driver.find_element(*self.blanket_request_button).click()
    def increase_ice_cream_order(self):
        self.driver.find_element(*self.ice_cream_increase_button).click()
        self.driver.find_element(*self.ice_cream_increase_button).click()
    def confirm_order(self):
        self.driver.find_element(*self.confirm_button).click()
    def wait_for_driver_info_modal(self):
        WebDriverWait(self.driver, 120).until(
            expected_conditions.visibility_of_element_located(self.order_summary_modal)
        )
