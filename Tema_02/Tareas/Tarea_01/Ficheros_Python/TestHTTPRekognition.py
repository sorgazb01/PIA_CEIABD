#!/usr/bin/env python
# coding: utf-8

# ###  En este ejemplo se explica cómo realizar una solicitud básica a Amazon Rekognition para detectar en una imagen: etiquetas (objetos) o las características de las caras de las personas, de forma similar a lo que hacen servicios como Google Cloud Vision, pero usando AWS Rekognition y la API REST vía HTTP.
# 

# <h1 style="color: red;">Requisitos previos</h1>
# 
# 1. **Cuenta de AWS**: Necesitarás una cuenta de AWS para obtener las credenciales necesarias (Access Key y Secret Access Key).
# 
# 2. **Instalar dependencias**. Para este ejemplo, utilizaremos la biblioteca **requests** para hacer la solicitud HTTP y **boto3** para hacer uso de las credenciales AWS de forma programática.
# 
# 3. **Configurar tus credenciales de AWS**. Ve a la Consola de AWS y crea un usuario de IAM con permisos para Amazon Rekognition.
# Genera un par de credenciales: Access Key ID y Secret Access Key. Anótalos, los necesitarás para firmar tus solicitudes.
# 
# 
# 

# <h3 style="color:blue;">Instalamos las dependencias que necesitamos</h3>

# In[1]:


# <h3 style="color:blue;">Pasos para hacer una solicitud a la API de Amazon Rekognition</h3>
# 
# 1. **Crear el cuerpo de la solicitud**.
# 
# 2. **Adjuntarle todos los datos necesarios a la solicitud en su cabecera**
# 
# 3. **Autenticación (Firma Version 4)**. AWS utiliza un sistema de autenticación llamado Signature Version 4. Esto implica que debes firmar tus solicitudes HTTP con tus credenciales de AWS. No se puede simplemente hacer una solicitud sin firmarla.
# 
# 4. **Hacer la llamada y recibir la respuesta**
# 
# 5. **Procesar la respuesta**
# 
# A continuación, veremos un ejemplo completo en Python de todo el proceso.

# <h4 style="color:orange;">Paso 0 (preparación de los datos y del entorno)</h4>
# 

# In[2]:


# Importamos los módulos necesarios
import hashlib
import hmac
import requests
import datetime
import base64
import json
from urllib.parse import urlencode


# In[3]:


# Especificamos nuestras credenciales de AWS (Access Key y Secret Access Key)
# Si estamos trabajando desde el Learner Lab, necesitaremos también el TOKEN de sesión. Todos estos datos los podemos sacar
# de la opción AWS Details,, una vez que hemos puesto en marcha el laboratorio

AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''
AWS_SESSION_TOKEN = ''
REGION = 'us-east-1'  # Cambia a la región donde tienes habilitado Rekognition


# In[4]:


# URL del servicio Rekognition para la región us-east-1 (cambia si estás usando otra región)
rekognition_url = 'https://rekognition.us-east-1.amazonaws.com/'


# In[5]:


# Leer y codificar la imagen en base64
with open('Tema_02\Tareas\Tarea_01\Imagenes\cara1descarga.jpg', "rb") as image_file:  # Cambiado a modo binario 'rb'
    image_base64 = base64.b64encode(image_file.read()).decode('utf-8')  # Podríamos hacerlo en un único paso


# <h4 style="color:orange;">Paso 1 (crear el cuerpo de la solicitud)</h4>
# 

# In[6]:


# Crear el cuerpo de la solicitud
request_body = {
    "Image": {
        "Bytes": image_base64   # Aquí le proporcinamos la imagen sobre la que vamos a trabajar. Tiene que estar codificada en base64
    },

    "Attributes": ["ALL"], # Especifica que quieres todos los atributos
#   "MaxLabels": 10,       # Si quiero limitar el tamaño de la respuesta, puedo indicarle el número de etiquetas que quiero que me envíe
    "MinConfidence": 75    # Especifico la confianza mínima que debe tener esa características. Cuanto más próxima esté la confianza a 100, más seguro está el modelo de que esa característica es verdadera
}

# Convertir el cuerpo de la petición a JSON
request_payload = json.dumps(request_body)


# <h4 style="color:orange;">Paso 2 (Adjuntar todos los datos en la solicitud en su cabecera)</h4>
# 
# 

# In[7]:


# Parámetros para la cabecera

content_type = 'application/x-amz-json-1.1'                 # tipo de contenido que le vamos a enviar

# Obtener la fecha actual en el formato requerido
t = datetime.datetime.utcnow()
amz_date = t.strftime('%Y%m%dT%H%M%SZ')                     # fecha y hora en que se hace la solictud
date_stamp = t.strftime('%Y%m%d')                           # fecha en la que se hace la solicitud en formato aaaammdd

#amz_target = 'RekognitionService.DetectLabels'             # identificador del tipo de servicio al que quiero acceder. En este caso DetectLabels
amz_target = 'RekognitionService.DetectFaces'               # identificador del tipo de servicio al que quiero acceder. En este caso DetectFaces

host = f'rekognition.{REGION}.amazonaws.com'                # identificación del nodo que da soporte al servicio


# In[8]:


# Creo la cabecera con los parámetros necesarios
headers = {
    'Content-Type': content_type,
    'X-Amz-Date': amz_date,
    'X-Amz-Target': amz_target,
    'Host': host,
    'X-Amz-Security-Token': AWS_SESSION_TOKEN  # Token de sesión. Sólo si trabajamos con AWS_TOKEN_SESSION
}


# <h4 style="color:orange;">Paso 3 (Hacemos la firma autenticada de la solicitud y se la adjuntamos a la cabecera)</h4>

# In[9]:


# Funciones necesarias para la firma de la solicitud
def sign(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

def getSignatureKey(key, dateStamp, regionName, serviceName):
    kDate = sign(('AWS4' + key).encode('utf-8'), dateStamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, 'aws4_request')
    return kSigning


# In[10]:


# Crear el string para firmar

# Si no estamos trabajando con AWS_SESSION_TOKEN
#canonical_headers = f'content-type:{content_type}\nhost:{host}\nx-amz-date:{amz_date}\nx-amz-target:{amz_target}\n'
#signed_headers = 'content-type;host;x-amz-date;x-amz-target'
# Si estamos trabajando con AWS_SESSION_TOKEN

# Componemos un string con los atributos que tiene el header y sus valores, separados por \n
canonical_headers = f'content-type:{content_type}\nhost:{host}\nx-amz-date:{amz_date}\nx-amz-security-token:{AWS_SESSION_TOKEN}\nx-amz-target:{amz_target}\n'

# le indicamos en este string qué atributos van a ser firmados
signed_headers = 'content-type;host;x-amz-date;x-amz-security-token;x-amz-target'

# Obtenemos el hash del cuerpo de la petición que vamos a enviar
payload_hash = hashlib.sha256(request_payload.encode('utf-8')).hexdigest()

# Componemos la canonical_request de la solicitud que se va a enviar
method = 'POST'  # operación HTTP que se quiere hacer
canonical_uri = '/'
canonical_querystring = ''

canonical_request = f'{method}\n{canonical_uri}\n{canonical_querystring}\n{canonical_headers}\n{signed_headers}\n{payload_hash}'


# Una **canonical request** es una representación estandarizada de la solicitud HTTP que se va a enviar a un servicio de AWS. Esta representación sigue un formato específico y es utilizada para generar la firma que se incluye en la cabecera de la solicitud.
# 
# Una **canonical request** incluye los siguientes elementos:
# 
# * **HTTP Method**: El método HTTP utilizado en la solicitud (por ejemplo, GET, POST, PUT, DELETE).
# 
# * **Canonical URI**: La parte del URI de la solicitud que especifica el recurso que estás tratando de acceder (por ejemplo, /my/resource).
# 
# * **Canonical Query String**: La cadena de consulta de la URL, en la que los parámetros están ordenados alfabéticamente y codificados de manera consistente.
# 
# * **Canonical Headers**: Un conjunto de encabezados que se envían con la solicitud, ordenados alfabéticamente. Cada encabezado debe estar en el formato key: value, y debe terminar con un salto de línea.
# 
# * **Signed Headers**: Una lista de los nombres de los encabezados que se han incluido en la solicitud, separados por punto y coma.
# 
# * **Payload Hash**: Un hash (generalmente SHA-256) del cuerpo de la solicitud (payload). Para las solicitudes que no tienen cuerpo (como GET), esto suele ser el hash de una cadena vacía.

# In[11]:


print(canonical_request)


# In[12]:


# Crear la string para la firma
algorithm = 'AWS4-HMAC-SHA256'                                        # algoritmo usado para la firma   
service = 'rekognition'                                               # servicio de AWS al que quiero invocar
credential_scope = f'{date_stamp}/{REGION}/{service}/aws4_request'    
string_to_sign = f'{algorithm}\n{amz_date}\n{credential_scope}\n{hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()}'


# In[13]:


# Firmar la solicitud
signing_key = getSignatureKey(AWS_SECRET_KEY, date_stamp, REGION, service)
signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()


# In[14]:


# Agregar la firma a los encabezados
authorization_header = f'{algorithm} Credential={AWS_ACCESS_KEY}/{credential_scope}, SignedHeaders={signed_headers}, Signature={signature}'
headers['Authorization'] = authorization_header


# <h4 style="color:orange;">Paso 4 (Hacemos la llamada y obtenemos la respuesta)</h4>

# In[15]:


# Hacer la solicitud POST
response = requests.post(rekognition_url, headers=headers, data=request_payload)


# <h4 style="color:orange;">Paso 5 Procesamos la respuesta)</h4>

# In[16]:


# Verificar la respuesta
if response.status_code == 200:
    response_json = response.json()
    print(json.dumps(response_json, indent=2))
else:
    print(f'Error: {response.status_code}')
    print(response.text)


# ### Estructura típica del JSON de respuesta de Amazon Rekognition
# 
# Cuando utilizas el servicio DetectLabels de Amazon Rekognition, el JSON de respuesta incluye información sobre las etiquetas (labels) detectadas en la imagen, junto con detalles como el nivel de confianza en cada etiqueta y las posibles coordenadas de los objetos.
# 
# 
# Cómo interpretar este JSON:
# * **Labels**: Es una lista de objetos. Cada objeto representa una etiqueta que Rekognition ha identificado en la imagen. Cada etiqueta tiene varios campos importantes:
#     - **Name**: El nombre de la etiqueta detectada (por ejemplo, "Person", "Car").
#     - **Confidence**: El nivel de confianza de la etiqueta, es decir, cuán segura está Rekognition de que esa etiqueta es correcta.
#     - **Instances**: Si hay objetos detectados asociados con esta etiqueta, Instances contiene una lista de esos objetos. Cada instancia puede incluir un BoundingBox, que proporciona las coordenadas de la caja delimitadora (para resaltar el objeto en la imagen).
#     - **Parents**: Algunas etiquetas tienen "padres". Por ejemplo, la etiqueta "Car" puede tener "Vehicle" como etiqueta padre, lo que indica que un auto es un tipo de vehículo.
# 

# In[17]:


# Si estoy usando el servicio DetectLabels
if (amz_target=='RekognitionService.DetectLabels'):
    # Recorrer las etiquetas y mostrar el nombre y la confianza
    for label in response_json['Labels']:
        name = label['Name']
        confidence = label['Confidence']
        parents = label['Parents']

        print(f"Etiqueta: {name}, Confianza: {confidence}, Padres : {parents}%")

        # Si hay objetos detectados, mostrar las coordenadas de la BoundingBox
        if 'Instances' in label and label['Instances']:
            for instance in label['Instances']:
                box = instance['BoundingBox']
                print(f"  BoundingBox - Izquierda: {box['Left']}, Superior: {box['Top']}, Ancho: {box['Width']}, Altura: {box['Height']}")


# Amazon Rekognition ofrece varios servicios avanzados además de DetectLabels. Cada uno de estos servicios utiliza el análisis de imágenes o videos basado en inteligencia artificial para resolver distintos problemas relacionados con la visión por computadora. Aquí tienes un resumen de los servicios que puedes utilizar en Amazon Rekognition:
# 
# 1. **DetectLabels (Detección de Etiquetas)**
# Descripción: Detecta objetos, escenas y conceptos dentro de imágenes. Esto incluye cosas como "persona", "auto", "animal", "edificio", etc., junto con una confianza asociada.
# Aplicación: Usado para análisis general de imágenes, etiquetado de contenido visual y búsqueda por etiquetas.
# 
# 2. **DetectFaces (Detección de Rostros)**
# Descripción: Detecta rostros en imágenes y proporciona detalles como las características faciales (ojos, nariz, boca), emociones (felicidad, tristeza, sorpresa), género estimado, y más.
# Aplicación: Útil para análisis facial, reconocimiento de emociones, o para la detección general de rostros en imágenes y videos.
# Datos devueltos: Coordenadas de las características faciales, emociones, edad aproximada, etc.
# 
# 3. **CompareFaces (Comparación de Rostros)**
# Descripción: Compara dos rostros para determinar si pertenecen a la misma persona. Devuelve una similitud basada en un porcentaje de confianza.
# Aplicación: Usado para verificación de identidad, aplicaciones de autenticación o comparación entre rostros en diferentes imágenes.
# Ejemplo: Comparar una foto de pasaporte con una selfie para verificar identidad.
# 
# 4. **RecognizeCelebrities (Reconocimiento de Celebridades)**
# Descripción: Identifica celebridades dentro de una imagen. Devuelve nombres de las personas reconocidas junto con un nivel de confianza.
# Aplicación: Usado en medios, entretenimiento, y aplicaciones que requieren reconocer celebridades en imágenes o videos.
# 
# 5. **DetectText (Detección de Texto)**
# Descripción: Detecta y extrae texto de imágenes. Puede identificar texto impreso o escrito a mano, y también permite localizar la posición del texto dentro de la imagen.
# Aplicación: Reconocimiento óptico de caracteres (OCR) en imágenes, análisis de documentos escaneados, señales, posters o cualquier otra fuente de texto dentro de imágenes.
# Datos devueltos: Frases, palabras, y sus coordenadas dentro de la imagen.
# 
# 6. **DetectModerationLabels (Etiquetas de Moderación de Contenido)**
# Descripción: Detecta contenido potencialmente ofensivo o inapropiado en imágenes, como desnudos, violencia, contenido sugestivo o drogas.
# Aplicación: Moderación automática de contenido para plataformas de redes sociales, sitios de video o cualquier aplicación que necesite filtrar contenido sensible.
# Etiquetas: "Nudity", "Violence", "Explicit Nudity", entre otras.
# 
# 7. **FaceSearch (Búsqueda de Rostros en Colección)**
# Descripción: Busca rostros en una imagen o video en una colección de rostros predefinida. Es útil para identificar personas que ya han sido almacenadas en una base de datos de rostros.
# Aplicación: Reconocimiento facial en tiempo real para seguridad, acceso a sistemas o identificación en grandes multitudes.
# Colecciones: Se pueden crear colecciones de rostros y realizar búsquedas rápidas para encontrar coincidencias.
# 
# 8. **CreateCollection y DeleteCollection (Gestión de Colecciones de Rostros)**
# Descripción: Permite crear y gestionar colecciones de rostros. Una colección de rostros es un conjunto de imágenes de rostros que puede ser utilizado para comparación o búsqueda en otros servicios como FaceSearch.
# Aplicación: Crear una base de datos para reconocimiento facial a nivel empresarial o para aplicaciones como control de acceso.
# 
# 9. **IndexFaces (Indexación de Rostros)**
# Descripción: Indexa los rostros detectados en una imagen y los almacena en una colección. Los rostros indexados pueden ser buscados y comparados usando SearchFaces o SearchFacesByImage.
# Aplicación: Identificación de personas a partir de una base de datos de rostros (por ejemplo, en control de acceso o vigilancia).
# 
# 10. **SearchFaces y SearchFacesByImage (Búsqueda de Rostros)**
# Descripción: Permite buscar rostros similares dentro de una colección de rostros indexados. SearchFacesByImage busca en una colección a partir de una imagen dada.
# Aplicación: Reconocimiento de personas dentro de una colección almacenada, para aplicaciones de control de acceso, seguridad, o verificación de identidad.
# 
# 11. **DetectProtectiveEquipment (Detección de Equipos de Protección Personal)**
# Descripción: Detecta si las personas en una imagen están usando equipo de protección personal (PPE), como cascos, máscaras o chalecos. También identifica si el equipo está siendo utilizado correctamente (por ejemplo, un casco en la cabeza).
# Aplicación: Cumplimiento de seguridad laboral, supervisión en obras de construcción o fábricas para verificar que los empleados usen equipo de seguridad.
# 
# 12. **AnalyzeFaces (Análisis Facial Profundo)**
# Descripción: Proporciona análisis avanzado de características faciales, emociones, género estimado, y edad estimada, además de detalles específicos como si la persona está sonriendo o si tiene los ojos abiertos.
# Aplicación: Publicidad segmentada, análisis de experiencias de usuario, o para cualquier aplicación que necesite analizar cómo se sienten las personas.
# 
# 13. **DetectCustomLabels (Etiquetas Personalizadas)**
# Descripción: Permite a los usuarios entrenar modelos personalizados para detectar objetos o escenarios específicos. Este servicio es útil cuando necesitas etiquetar objetos que no están cubiertos por las etiquetas prediseñadas de Rekognition.
# Aplicación: Reconocimiento personalizado para casos de uso específicos de la industria, como la detección de productos, logotipos, o cualquier otro objeto que no esté cubierto por las etiquetas estándar.
# 
# 14. **DetectTextInVideo (Detección de Texto en Video)**
# Descripción: Similar a DetectText, pero aplicado en secuencias de video, donde se detecta texto impreso o escrito a mano en cada fotograma de video.
# Aplicación: Análisis de videos que contienen señales, subtítulos o cualquier otra forma de texto.
# 
# 15. **Video Segment Analysis (Análisis de Segmentos de Video)**
# Descripción: Análisis de videos para detectar escenas, personas, objetos, rostros y más dentro de un flujo de video.
# Aplicación: Procesamiento de videos para identificar automáticamente personas u objetos a lo largo del tiempo.

# Por ejemplo, prueba a a usar el servicio DetectFaces, en lugar de DetectLabels
# 
# amz_target = 'RekognitionService.DetectLabels'
# 
# se cambia por:
# 
# amz_target = 'RekognitionService.DetectFaces'
# 

# En este caso, cambia el formato del JSON de salida. Podríamos recorrerlo con:

# In[18]:


# Si estoy usando el servicio DetectFaces, puedo acceder a ciertos datos como su edad estimada, género, emociones, etc, de la siguiente forma:
if (amz_target=='RekognitionService.DetectFaces'):
    for face in response_json['FaceDetails']:
        age_range = face['AgeRange']
        gender = face['Gender']['Value']
        smile = face['Smile']['Value']
        emotions = face['Emotions']

        print(f"Rango de edad: {age_range['Low']} - {age_range['High']}")
        print(f"Género: {gender}")
        print(f"Sonrisa: {'Sí' if smile else 'No'}")

        # Emociones
        print("Emociones:")
        for emotion in emotions:
            print(f"  {emotion['Type']}: {emotion['Confidence']}%")


# In[ ]:




