import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from main import UrbanRoutesPage
import data
@pytest.fixture(scope="class")
def setup(request):
    """
    Configura el controlador de Selenium para las pruebas.
    - Habilita los registros de red para capturar datos de rendimiento.
    - Abre la página principal de Urban Routes.
    - Cierra el navegador al finalizar las pruebas.
    """
    capabilities = DesiredCapabilities.CHROME
    capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
    driver = webdriver.Chrome(desired_capabilities=capabilities)
    driver.get(data.urban_routes_url)
    request.cls.driver = driver
    yield
    driver.quit()
@pytest.mark.usefixtures("setup")
class TestUrbanRoutes:
    """
    Clase que agrupa todas las pruebas para la aplicación Urban Routes.
    Cada método representa una prueba específica, verificando una funcionalidad clave de la aplicación.
    """
    def test_set_origin(self):
        """
        Verifica que la dirección de origen se pueda ingresar correctamente.
        - Ingresa la dirección de origen y valida que el valor se refleje en el campo correspondiente.
        """
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_origin(data.address_from)
        assert routes_page.driver.find_element(*routes_page.origin_input).get_property('value') == data.address_from
    def test_set_destination(self):
        """
        Verifica que la dirección de destino se pueda ingresar correctamente.
        - Ingresa la dirección de destino y valida que el valor se refleje en el campo correspondiente.
        """
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_destination(data.address_to)
        assert routes_page.driver.find_element(*routes_page.destination_input).get_property('value') == data.address_to
    def test_request_taxi(self):
        """
        Prueba la funcionalidad de solicitud de taxi.
        - Simula el clic en el botón de solicitud de taxi.
        - Verifica que el flujo avance después de la solicitud.
        """
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_taxi()
        assert "Taxi solicitado" in self.driver.page_source  # Ajusta el texto esperado según la aplicación
    def test_select_comfort_option(self):
        """
        Verifica que se pueda seleccionar la opción de tarifa Comfort.
        - Simula el clic en la opción Comfort.
        - Valida que el sistema reconozca la selección.
        """
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort_option()
        assert "Comfort" in self.driver.page_source  # Ajusta el texto esperado según la aplicación
    def test_enter_phone_number(self):
        """
        Prueba la entrada del número de teléfono en el campo correspondiente.
        - Ingresa el número de teléfono y valida que se refleje correctamente en el campo.
        """
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_phone_number(data.phone_number)
        assert routes_page.driver.find_element(*routes_page.phone_number_field).get_property('value') == data.phone_number
    def test_add_credit_card(self):
        """
        Verifica que se pueda agregar una tarjeta de crédito.
        - Ingresa los datos de la tarjeta y confirma la acción.
        - Valida que el sistema reconozca que se ha agregado la tarjeta.
        """
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_credit_card(data.card_number, data.card_code)
        assert "Tarjeta agregada" in self.driver.page_source  # Ajusta el mensaje esperado según la aplicación
    def test_write_message_to_driver(self):
        """
        Verifica que se pueda escribir un mensaje para el conductor.
        - Ingresa un mensaje en el campo correspondiente y valida que el valor sea correcto.
        """
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.write_message_to_driver(data.message_for_driver)
        assert data.message_for_driver in routes_page.driver.find_element(*routes_page.message_for_driver_field).get_property('value')
    def test_request_blanket(self):
        """
        Verifica que se pueda solicitar una manta adicional.
        - Simula el clic en la opción de solicitar manta.
        - Valida que el sistema registre la solicitud.
        """
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_blanket()
        assert "Manta solicitada" in self.driver.page_source  # Ajusta el texto esperado según la aplicación
    def test_increase_ice_cream_order(self):
        """
        Verifica que se pueda incrementar la cantidad de helado solicitado.
        - Simula dos clics para aumentar la cantidad.
        - Valida que el total de helados sea correcto (2 unidades).
        """
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.increase_ice_cream_order()
        # Verifica que la cantidad de helados sea correcta
        ice_cream_count = self.driver.find_element(By.CLASS_NAME, "ice-cream-count").text
        assert ice_cream_count == "2"
    def test_confirm_order(self):
        """
        Verifica la funcionalidad para confirmar el pedido.
        - Simula el clic en el botón Confirmar.
        - Valida que el modal de información del conductor aparezca.
        """
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.confirm_order()
        routes_page.wait_for_driver_info_modal()
        assert routes_page.driver.find_element(*routes_page.order_summary_modal).is_displayed()
