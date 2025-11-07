import flet as ft
import requests, json
from datetime import date

# CONFIGURACIÓN A LA CONEXIÓN DE LAS API's:

# URLs:
URL_API_APOD="https://api.nasa.gov/planetary/apod?"  # URL de la API APOD
URL_API_NEOWS="https://api.nasa.gov/neo/rest/v1/feed?" # URL de la API NeoWs

# key para acceso:
api_key = "c2OYvrWfzSWPDRAburcCkTmIc0iKnAZk88xLwaVq"

# Parametros de busqueda
now= date.today() # Fecha actual tomada del servidor

def apod(): # Conexión a la Api APOD (Astronomy Picture of the Day)
        try:
                # Parámetros de busqueda
                params= {
                    "api_key":api_key,
                    "date":now,
                    }
                # Solicitud GET a la API
                response = requests.get(URL_API_APOD, params= params) 

                if response.status_code == 200:
                    apod_data = response.json()  # Se convierte la respuesta a JSON
                    return apod_data # Retorno resultado

        except requests.exceptions.RequestException as e:
            apod_data=("Error al conectar con la API APOD: {e}")# Error de conexión con la api

        except json.JSONDecodeError as e:
            apod_data=("Error al decodificar JSON: {e}")  # Manejo de errores al decodificar JSON


def neows(): # Conexión a la Api NeoWs (Near Earth Object Web Service)      
        try:
                # Parámetros de busqueda
                params= {
                    "api_key":api_key,
                    "start_date":'2010-09-07',
                    "end_date":'2010-09-08',
                    }
                # Intenta realizar la solicitud GET a la API
                response = requests.get(URL_API_NEOWS, params= params)

                if response.status_code == 200:
                    neows_data = response.json() # Se convierte la respuesta a JSON
                    return neows_data # Retorno resultado

        except requests.exceptions.RequestException as e:
            neows_data=(f"Error al conectar con la API NeoWs: {e}") # Error de conexión con la api

        except json.JSONDecodeError as e:
           neows_data=(f"Error al decodificar JSON: {e}")  # Maneja errores al decodificar JSON