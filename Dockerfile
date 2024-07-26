#Imagen base 
FROM python:3.9-slim

#Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

##Archivo requirements
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#Copiamos el contenido del proyecto al contenedor
COPY . .

#Puerto en el que se ejecutara el modelo
EXPOSE 8000

#Ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

