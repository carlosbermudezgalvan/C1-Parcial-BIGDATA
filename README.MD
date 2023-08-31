# Proyecto C1-Parcial-BIGDATA

Este proyecto forma parte de un parcial de la materia BIGDATA. Consiste en la creación de funciones Lambda en AWS utilizando Zappa, pruebas unitarias con pytest y GitHub Actions para el despliegue continuo.

## Estructura del Proyecto

C1-Parcial-BIGDATA/
download_wpage.py
extract_data/
init.py
extract_data.py
tests/
test_download_wpage.py
test_extract_data.py


- `download_wpage.py`: Contiene la función `lambda_handler` para descargar páginas web y guardarlas en S3.
- `extract_data/`: Carpeta que contiene el módulo `extract_data` con la función `lambda_handler_processing`.
- `tests/`: Carpeta con pruebas unitarias para los módulos.

## Configuración

1. Asegúrate de tener las credenciales de AWS configuradas en tu entorno.
2. Instala las dependencias utilizando `pip install -r requirements.txt`.

## Ejecución de Pruebas

1. Configura el `PYTHONPATH` para que Python pueda encontrar los módulos:

   ```sh
   export PYTHONPATH=$PYTHONPATH:$(pwd)

Despliegue Continuo
Las pruebas y el despliegue continuo se gestionan mediante GitHub Actions. El flujo de trabajo se define en .github/workflows/worflou.yml.

Contribuciones
Las contribuciones son bienvenidas. Si encuentras problemas o mejoras, siéntete libre de abrir un issue o enviar un pull request.