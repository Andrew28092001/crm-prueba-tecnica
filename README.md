# CRM - Prueba Técnica (Django)

Este proyecto es una solución tipo CRM desarrollada con Django y PostgreSQL, aplicando principios de Clean Code y una estructura modular (simulando microservicios a través de aplicaciones de Django independientes).

## Características Principales

- **Arquitectura Modular:** Separación de responsabilidades en apps (`clientes`, `oportunidades`).
- **Consumo de API Externa:** Integración con Open-Meteo API (en el patrón Service) para mostrar el clima actual de la ciudad del cliente.
- **Automatización:** Comando personalizado para actualizar el estado de oportunidades antiguas de forma masiva (`actualizar_oportunidades`).
- **Frontend:** Interfaz limpia y responsiva usando Bootstrap 5 y vistas basadas en clases (CBVs).

## Requisitos Previos

- Python 3.8+
- PostgreSQL instalado y corriendo.

## Instalación y Configuración

1. **Clonar el repositorio:**

   ```bash
   git clone <tu_url_de_github_aqui>
   cd crm_prueba
   ```

2. **Crear y activar el entorno virtual:**

   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   # En Mac/Linux:
   source venv/bin/activate
   ```

3. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la Base de Datos:**

   - Abre pgAdmin (o tu cliente de PostgreSQL) y crea una base de datos vacía llamada `crm_db`.
   - Verifica que las credenciales en `crm_backend/settings.py` (usuario y contraseña) coincidan con las de tu entorno local.

5. **Aplicar migraciones:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Ejecutar el servidor de desarrollo:**

   ```bash
   python manage.py runserver
   ```

   Accede a [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en tu navegador.