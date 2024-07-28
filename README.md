# Ollama API Backend

Este proyecto implementa un backend en Flask que interactúa con la API de Ollama para generar texto y gestionar modelos. Incluye soporte para generación de texto con streaming y una interfaz Swagger para documentar y probar los endpoints.

## Requisitos

- Python 3.6+
- pip

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu_usuario/ollama-api-backend.git
   cd ollama-api-backend
   ```
2. Crea y activa un entorno virtual:
   ```bash
   python -m venv ollama-env
   source ollama-env/bin/activate  # En Windows, usa `ollama-env\Scripts\activate`
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Configuración
- Asegúrate de tener las credenciales y configuraciones necesarias para usar la API de Ollama.

### Uso
- Ejecuta el servidor Flask:
   ```bash
   python app.py
   ```
### Endpoints
 ```
/generate_text [POST]
Genera texto usando un modelo.
 ```


- Parámetros
* model: El nombre del modelo a usar.
* prompt: El prompt para generar texto.
- Respuesta
* generated_text: El texto generado por el modelo.
```
/generate_text_stream [POST]
Genera texto usando un modelo con streaming.
```
- Parámetros
* model: El nombre del modelo a usar.
* prompt: El prompt para generar texto.
- Respuesta
* Stream de texto generado por el modelo.
```
/chat [POST]
Crea una conversación usando un modelo.
```

- Parámetros
* model: El nombre del modelo a usar.
* messages: Lista de mensajes para la conversación.
- Respuesta
* response: La respuesta del modelo de chat.
```
/create_model [POST]
Crea un modelo.
```
- Parámetros
* model: El nombre del modelo a crear.
* path: La ruta al archivo del modelo.
* modelfile (opcional): El archivo del modelo.
* quantize (opcional): La opción de cuantización.
- Respuesta
* status: El estado de la creación del modelo.
```
/delete_model/<model> [DELETE]
Elimina un modelo.
```
- Parámetros
* model: El nombre del modelo a eliminar.
* Respuesta
* status: El estado de la eliminación del modelo.
```
/list_models [GET]
Lista todos los modelos.
```
- Respuesta
* models: Lista de nombres de modelos.
## Contribuir
- Haz un fork del repositorio.
- Crea una nueva rama (git checkout -b feature/nueva-caracteristica).
- Realiza tus cambios y haz commit (git commit -am 'Agrega nueva característica').
Sube tus cambios a la rama (git push origin feature/nueva-caracteristica).
Crea un nuevo Pull Request.
### Licencia
Este proyecto está licenciado bajo los términos de la licencia MIT. Para más detalles, consulta el archivo LICENSE.


### Archivos del Proyecto
```
Tu estructura de proyecto debería verse algo así:
```
```
ollama-api-backend/
├── app.py
├── config.py
├── ollama_client.py
├── requirements.txt
└── README.md
```


### Para facilitar la construcción y ejecución de tu proyecto, puedes usar Docker para crear un contenedor y un archivo Makefile para automatizar los comandos.


- Construir la imagen de Docker:

```
make build
```

- Ejecutar el contenedor de Docker:

```
make run
```

Detener y eliminar todos los contenedores:
```
make clean
```

Ejecutar una shell en el contenedor:
```
make shell
```
