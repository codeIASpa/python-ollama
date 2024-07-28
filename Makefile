# Nombre de la imagen de Docker
IMAGE_NAME = ollama-api-backend

# Construir la imagen de Docker
build:
	docker build -t $(IMAGE_NAME) .

# Ejecutar el contenedor de Docker
run:
	docker run -p 5001:5000 $(IMAGE_NAME)

# Detener y eliminar todos los contenedores
clean:
	docker rm -f $(shell docker ps -aq)

# Ejecutar una shell en el contenedor
shell:
	docker run -it --entrypoint /bin/bash $(IMAGE_NAME)

.PHONY: build run clean shell
