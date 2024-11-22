# Urban Routes - Pruebas Automatizadas
## Descripción del Proyecto
Este proyecto contiene un conjunto de pruebas automatizadas para el flujo de solicitud de un taxi en la plataforma Urban Routes. Las pruebas están diseñadas para validar la funcionalidad completa de la aplicación, desde la configuración de una ruta hasta la confirmación final de la solicitud de taxi, incluyendo validaciones de autenticación de usuario y métodos de pago.
## Tecnologías y Herramientas
- **Lenguaje**: Python
- **Framework de Pruebas**: Pytest
- **Automatización de Navegadores**: Selenium WebDriver
- **Navegador**: Google Chrome
- **Gestión de dependencias**: `requirements.txt` (si se utiliza)
  
Este proyecto también utiliza técnicas de localización avanzadas (ID, XPath, CSS, Class Name, etc.) y métodos de espera explícitos para asegurar la sincronización de elementos en la página.
## Estructura de Archivos
- `main.py`: Contiene la clase `TestUrbanRoutes` con las pruebas automatizadas principales.
- `urban_routes_page.py`: Define la clase `UrbanRoutesPage`, que encapsula la lógica de interacción con la página Urban Routes.
- `data.py`: Archivo de datos donde se configuran las constantes como `address_from`, `address_to`, `phone_number`, `card_number`, `card_code`, y `message_for_driver`.
- `configuration.py`: Configuración de rutas y URL de la aplicación bajo prueba.
- `README.md`: Este archivo, con una guía de uso del proyecto.
- `.gitignore`: Para excluir archivos innecesarios del repositorio de Git.
## Requisitos Previos
- Python 3.7+
- Instalar las dependencias del proyecto con:
  ```bash
  pip install -r requirements.txt
