#!/usr/bin/env python
# coding: utf-8

# Si en lugar de usar el servicio Detect Faces de Rekognition, quisiéramos usar el de Detect Labels, procederíamos de la misma forma, cambiando únicamente el método a llamar y el procesamiento de la respuesta.

# In[1]:


import boto3


# <h4 style="color:orange;">Paso 1. Creamos el cliente de Rekognition</h4>

# In[2]:


AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''
AWS_SESSION_TOKEN = ''
REGION = 'us-east-1'

# En este caso creamos el cliente haciendo uso del fichero de credenciales
rekognition_client = boto3.client(
    'rekognition',
    region_name=REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    aws_session_token=AWS_SESSION_TOKEN
)


# <h4 style="color:orange;">Paso 2. Leemos el fichero con el que queremos trabajar</h4>

# In[3]:


# Leemos la imagen desde el archivo en formato binario

IMAGE_FILE_PATH = "Tema_02\\Tareas\\Tarea_01\\Imagenes\\prueba2.jpg"
with open(IMAGE_FILE_PATH, 'rb') as image_file:
    image_bytes = image_file.read()


# <h4 style="color:orange;">Paso 3. Realizamos la solicitud a DETECT_LABELS</h4>
# 

# In[4]:


# Realizar la solicitud DetectFaces al servicio de Rekognition. En este caso, cambian ligeramente los parámetros que recibe el método
response = rekognition_client.detect_labels(
    Image={'Bytes': image_bytes},
    MaxLabels=15,            # Mostrar hasta 15 etiquetas
    MinConfidence=95.0       # Solo etiquetas con confianza >= 90%    
)


# <h4 style="color:orange;">Paso 4. Procesamos la respuesta</h4>
# 

# In[5]:


print(response)


# **Estructura de la respuesta**
# 
# La respuesta de detect_labels es un diccionario que contiene información sobre las etiquetas detectadas. Donde: 
# * **Labels**: Contiene las etiquetas detectadas con:
#     1. **Name**: El nombre de la etiqueta (por ejemplo, "Person", "Tree").
#     2. **Confidence**: La confianza de que la etiqueta sea correcta, en porcentaje.
#     3. **Instances**: Si aplica, contiene instancias de los objetos detectados con su BoundingBox (rectángulo de localización).
#     4. **Parents**: Las categorías generales a las que pertenece la etiqueta (por ejemplo, "Person" puede tener "Human" como padre).
# 
# 

# In[6]:


# Mostrar etiquetas detectadas
for label in response['Labels']:
    print(f"Etiqueta: {label['Name']}, Confianza: {label['Confidence']}, Categorías superiores:{label['Parents']}")


# In[ ]:




