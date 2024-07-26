# API de Predicción de ML con FastAPI

Este proyecto es una API construida con FastAPI para predecir la clase (`Alpha` o `Betha`). La predicción se realiza utilizando un modelo de ML previamente entrenado. La API recibe datos de entrada a través de una solicitud POST en formato JSON y devolver la predicción de clase.

## Contenido

- [Características](#características)
- [Configuración](#configuración)
- [Uso](#uso)
- [Puntos de Acceso (Endpoints)](#puntos-de-acceso-endpoints)
- [Información del Modelo](#información-del-modelo)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

## Características

- **Integración de Modelo de ML**: Utiliza un modelo de RandomForest para la predicción de clases.
- **API JSON**: Acepta y devuelve datos en formato JSON.
- **Fácil Despliegue**: Construida con FastAPI, lo que facilita su despliegue y escalabilidad.

### Requisitos
fastapi==0.111.1
joblib==1.4.2
numpy==1.24.3
pandas==1.5.2
pydantic==2.8.2
scikit-learn==1.3.2
typing-extensions==4.12.2


### Instalación

1. **Clonar el Repositorio**

   ```bash
   git clone https://github.com/JuanManuelSanchez05/ml-api.git
   cd ml-api
