#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3


# In[2]:


# Especificamos nuestras credenciales. Hemos de recordar que si estamos usando el **Learner Lab**, tendremos que definir el token de sesión.
AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''
AWS_SESSION_TOKEN = ''
REGION = 'us-east-1'  # Cambia a la región donde tienes habilitado Rekognition

# Crear el cliente de Textract
textract = boto3.client('textract',
    region_name=REGION,  # Cambia esto a la región que estés usando
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    aws_session_token=AWS_SESSION_TOKEN  # Solo si tienes un token de sesión
)

FILE_PATH = "Tema_02\Tareas\Tarea_01\Imagenes\prueba4.png"

# Cargar la imagen del documento (asegúrate de que la imagen esté en el mismo directorio o usa una ruta absoluta)
with open(FILE_PATH, "rb") as document_file:
    document_bytes = document_file.read()

# Llamar a Textract para extraer texto
response = textract.detect_document_text(Document={'Bytes': document_bytes})

# print(response)


# Mostrar el texto detectado
for block in response['Blocks']:
    if block['BlockType'] == 'LINE':
        print(f"Texto detectado: {block['Text']}")


# <h4 style="color:orange"> AWS TRANSLATE </h4> (No está habilitado en el Learner Lab)
# 
# **AWS TRANSLATE** permite hacer traducciones al estilo Google Translator desde cualquier idioma origen a cualquier idioma.

# In[4]:


# Ejemplo de cómo se podría hacer uso del servicio de Amazon translate. (No está permitido desde el Learner Lab)

'''#Crear el cliente de Amazon Translate
translate = boto3.client('translate',
    region_name=REGION,  # Cambia esto a la región que estés usando
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    aws_session_token=AWS_SESSION_TOKEN  # Solo si tienes un token de sesión
)

# Texto que queremos analizar
text = "Este es un día increíble. Me siento muy feliz y emocionado."


# Realizar la traducción
response = translate.translate_text(Text=text, SourceLanguageCode='en', TargetLanguageCode='es')

# Mostrar el resultado
print(f"Texto original: {text}")
print(f"Texto traducido: {response['TranslatedText']}")

'''


# <h4 style="color:orange"> AWS COMPREHEND </h4> (No está habilitado en el Learner Lab)
# 
# **AWS COMPREHEND** es un servicio de procesamiento de lenguaje natural (NLP) en el que se utiliza el machine learning para descubrir información y conexiones valiosas en textos. Permite, entre otras cosas, identificar el sentimiento del texto, obtener palabras clave, descubrir relaciones, etc.
# 

# In[5]:


# Ejemplo de cómo se podría hacer uso del servicio de AWS Comprehend. (No está permitido desde el Learner Lab)

'''
#Crear el cliente de Comprehend
comprehend = boto3.client('comprehend',
    region_name=REGION,  # Cambia esto a la región que estés usando
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    aws_session_token=AWS_SESSION_TOKEN  # Solo si tienes un token de sesión
)


# Texto que queremos analizar
text = "Este es un día increíble. Me siento muy feliz y emocionado."


# Detectar el sentimiento del texto
response = comprehend.detect_sentiment(Text=text, LanguageCode='es')

# Mostrar el resultado
#print(f"Texto: {text}")
#print(f"Sentimiento detectado: {response['Sentiment']}")
#print(f"Detalles del sentimiento: {response['SentimentScore']}")
'''


# <h4 style="color:orange"> AWS POLLY </h4> (No está habilitado en el Learner Lab)
# 
# **AWS POLLY** es un servicio que convierte el texto en audio hablado muy realista.

# In[6]:


# Ejemplo de cómo se podría hacer uso del servicio de AWS Polly. (No está permitido desde el Learner Lab)
'''
import boto3

# Crear el cliente de Polly
polly = boto3.client('polly',
    region_name=REGION,  # Cambia esto a la región que estés usando
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    aws_session_token=AWS_SESSION_TOKEN  # Solo si tienes un token de sesión
)

# Texto a convertir en audio
text = "Hola, este es un ejemplo usando Amazon Polly."

# Realizar la conversión de texto a voz
response = polly.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId='Lucia')

# Guardar el archivo de audio resultante
with open('salida_audio.mp3', 'wb') as audio_file:
    audio_file.write(response['AudioStream'].read())

print("El archivo de audio se ha guardado como salida_audio.mp3")
'''

