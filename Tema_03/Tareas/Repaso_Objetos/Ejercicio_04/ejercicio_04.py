# 4. Crea una clase Estudiante con los atributos nombre, edad y nota_media.
# Añade un método que imprima si el estudiante ha aprobado o suspendido
# según su nota_media.
import estudiante

estudiante1 = estudiante.Estudiante('Sergio', 23, 10)

if estudiante1.aprobado():
    print(f'El estudiante {estudiante1.nombre} ha aprobado con una nota media de {estudiante1.nota_media}')