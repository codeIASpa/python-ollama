from flask import Flask, request, jsonify, Response
from flasgger import Swagger
from flask_cors import CORS
from ollama_client import OllamaClient
import json

app = Flask(__name__)
swagger = Swagger(app)
CORS(app, resources={r"/*": {"origins": "http://localhost:4000"}})
ollama_client = OllamaClient()

@app.route('/generate_text', methods=['POST'])
def generate_text():
    """
    Generar texto usando un modelo.
    ---
    parameters:
      - name: body
        in: body
        required: True
        schema:
          type: object
          required:
            - model
            - prompt
          properties:
            model:
              type: string
              description: El nombre del modelo a usar.
            prompt:
              type: string
              description: El prompt para generar texto.
    responses:
      200:
        description: Texto generado
        schema:
          type: object
          properties:
            generated_text:
              type: string
              description: El texto generado por el modelo.
    """
    data = request.json
    model = data.get('model')
    prompt = data.get('prompt')
    response = ollama_client.generate_text(model, prompt)
    return jsonify(response)

@app.route('/generate_text_stream', methods=['POST'])
def generate_text_stream():
    """
    Generar texto usando un modelo con streaming.
    ---
    parameters:
      - name: body
        in: body
        required: True
        schema:
          type: object
          required:
            - model
            - prompt
          properties:
            model:
              type: string
              description: El nombre del modelo a usar.
            prompt:
              type: string
              description: El prompt para generar texto.
    responses:
      200:
        description: Texto generado
        schema:
          type: object
          properties:
            generated_text:
              type: string
              description: El texto generado por el modelo.
    """
    data = request.json
    model = data.get('model')
    prompt = data.get('prompt')

    def generate():
        for response in ollama_client.generate_text_stream(model, prompt):
            yield json.dumps(response) + '\n'

    return Response(generate(), content_type='application/json')

@app.route('/generate_places', methods=['POST'])
def generate_places():
    """
    Generar lugares turísticos y devolver JSON.
    ---
    parameters:
      - name: body
        in: body
        required: True
        schema:
          type: object
          required:
            - model
            - prompt
          properties:
            model:
              type: string
              description: El nombre del modelo a usar.
            prompt:
              type: string
              description: El prompt para generar lugares turísticos.
    responses:
      200:
        description: Lugares turísticos generados
        schema:
          type: object
          properties:
            lugaresTuristico:
              type: array
              items:
                type: object
                properties:
                  nombre:
                    type: string
                    description: Nombre del lugar turístico.
                  coordenadas:
                    type: array
                    items:
                      type: string
                      description: Coordenadas del lugar turístico.
    """
    data = request.json
    model = data.get('model')
    prompt = data.get('prompt')

    def generate_json():
        for response in ollama_client.generate_text_stream_json(model, prompt):
            yield json.dumps(response) + '\n'

    return Response(generate_json(), content_type='application/json')

@app.route('/chat', methods=['POST'])
def chat():
    """
    Crear una conversación usando un modelo.
    ---
    parameters:
      - name: body
        in: body
        required: True
        schema:
          type: object
          required:
            - model
            - messages
          properties:
            model:
              type: string
              description: El nombre del modelo a usar.
            messages:
              type: array
              items:
                type: object
                properties:
                  role:
                    type: string
                    description: El rol del mensaje (e.g., user, assistant).
                  content:
                    type: string
                    description: El contenido del mensaje.
    responses:
      200:
        description: Respuesta de chat
        schema:
          type: object
          properties:
            response:
              type: object
              description: La respuesta del modelo de chat.
    """
    data = request.json
    model = data.get('model')
    messages = data.get('messages')
    response = ollama_client.chat(model, messages)
    return jsonify(response)

@app.route('/create_model', methods=['POST'])
def create_model():
    """
    Crear un modelo.
    ---
    parameters:
      - name: body
        in: body
        required: True
        schema:
          type: object
          required:
            - model
            - path
          properties:
            model:
              type: string
              description: El nombre del modelo a crear.
            path:
              type: string
              description: La ruta al archivo del modelo.
            modelfile:
              type: string
              description: El archivo del modelo (opcional).
            quantize:
              type: string
              description: La opción de cuantización (opcional).
    responses:
      200:
        description: Modelo creado
        schema:
          type: object
          properties:
            status:
              type: string
              description: El estado de la creación del modelo.
    """
    data = request.json
    model = data.get('model')
    path = data.get('path')
    modelfile = data.get('modelfile')
    quantize = data.get('quantize')
    response = ollama_client.create_model(model, path, modelfile, quantize)
    return jsonify(response)

@app.route('/delete_model/<model>', methods=['DELETE'])
def delete_model(model):
    """
    Eliminar un modelo.
    ---
    parameters:
      - name: model
        in: path
        type: string
        required: True
        description: El nombre del modelo a eliminar.
    responses:
      200:
        description: Modelo eliminado
        schema:
          type: object
          properties:
            status:
              type: string
              description: El estado de la eliminación del modelo.
    """
    response = ollama_client.delete_model(model)
    return jsonify(response)

@app.route('/list_models', methods=['GET'])
def list_models():
    """
    Listar todos los modelos.
    ---
    responses:
      200:
        description: Lista de modelos
        schema:
          type: object
          properties:
            models:
              type: array
              items:
                type: string
                description: Los nombres de los modelos.
    """
    response = ollama_client.list_models()
    return jsonify(response)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5001, debug=True)
