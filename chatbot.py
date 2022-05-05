#Importamos re para usar expresiones regulares(evita caracteres especiales y signos de puntuacion)
import re
import random

#Definimos el metodo de respuestas del chatbot con la entrada del usuario
def obtener_respuesta(entrada_usuario):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', entrada_usuario.lower())
    respuesta = checar_mensajes(split_message)
    return respuesta

"""
mensaje_usuario: mensaje del usuario
palabras_reconocidas: lista de palabras reconocidas
respuestas_sencillas:
palabra_requerida: En caso de que en una respuesta se requiera una palabra especifica
"""
#Definimos metodo para calcular la probabilidad de una respuesta 
def probabilidad_mensaje(mensaje_usuario, palabras_reconozidas, respuesta_simple=False, palabra_requerida=[]):
    mensaje_certero = 0
    tiene_palabra_requeridas = True

    #Recorremos las palabras del mensaje del usuario en busca de las palabras reconocidas
    for palabra in mensaje_usuario:
        if palabra in palabras_reconozidas:
            mensaje_certero +=1

    #Obtenemos el porcentaje de seguridad del mensaje
    porcentaje = float(mensaje_certero) / float (len(palabras_reconozidas))

    #Buscamos si el mensaje contiene la palabra requerida y si lo la tiene rompemos el ciclo
    for palabra in palabra_requerida:
        if palabra not in mensaje_usuario:
            tiene_palabra_requeridas = False
            break
    #En caso de si tenerla o tener una respuesta sencilla retornamos la de mayor probabilidad
    if tiene_palabra_requeridas or respuesta_simple:
        return int(porcentaje * 100)
    else:
        return 0

#Definimos metodo para checar los mensajes
def checar_mensajes(mensaje):
        prob_alta = {}

        #Definimos metodo de la respuesta del bot
        def respuesta(respuesta_bot, lista_palabras, respuesta_simple = False, palabra_requeridas = []):
            nonlocal prob_alta
            #Calculamos la probabilidad del mensaje del bot
            prob_alta[respuesta_bot] = probabilidad_mensaje(mensaje, lista_palabras, respuesta_simple, palabra_requeridas)

        #Definimos las respuestas del bot
        respuesta('Bienvenid@ al chatbot del IMMS. ¿En que puedo ayudarte?', ['hola', 'saludos', 'buenas', 'saludo'], respuesta_simple = True)
        respuesta('Para realizar el alta de tu UMF deberas acudir a tu clinica mas cercana a tu domicilio con tu identificación oficial, comprobante de domicilio, NSS, una fotografia infantil y acta de nacimiento.\n¿Hay algo más en lo que le pueda ayudar?', ['alta', 'clinica', 'umf', 'resgistrar', 'registrarme', 'dar', 'darme'], palabra_requeridas=['alta'])
        respuesta('Para realizar la baja de un UMF deberas acudir a tu clinica mas cercana a tu domicilio con tu identificación oficial, NSS, CURP y acta de defuncion en caso de muerte o acta de divorcio en caso de baja por divorcio.\n¿Hay algo más en lo que le pueda ayudar?', ['baja', 'umf', 'clinica', 'dar', 'darme'], palabra_requeridas=['baja'])
        respuesta('Para realizar la actualización de tu UMF deberas acudir a tu clinica mas cercana a tu domicilio con tu identificación oficial, comprobante de domicilio, NSS y una fotografia infantil.\n¿Hay algo más en lo que le pueda ayudar?',['actualizar', 'cambiar', 'clinica', 'umf', 'modificar'])
        respuesta('Para obtener tu aviso para calificación de accidente o enfermedad de trabajo ante el IMSS deberas acudir a tu clinica que te corresponda de acuerdo a tu domicilio con tu identificación oficial, cartilla nacional de salud, aviso de atención médica inicial y calificación de probable accidente de trabajo ST-7 y ST-9. En caso de defunción sera acta de defunción, certificado de necropsia que incluya examen toxicológico copia certificada de la Averiguación Previa del Ministerio Público y resumen medico de atención inicial de servicios en caso de tenerlo.\n¿Hay algo más en lo que le pueda ayudar?',['trabajo', 'laboral', 'calificacion', 'accidente', 'enfermedad'])
        respuesta('Para incribir a tu hijo a las guarderias del IMSS deberas acudir a la guarderia de tu interes o entrar al siguiente link:\nhttps://stigi.imss.gob.mx/\nen un horario de lunes a viernes de 7 a 19 horas con los siguientes datos de tu hijo/a: Nombre completo Fecha de nacimiento Acta de nacimiento Cartilla Nacional de Salud Examen Medico requisitado Tambien deberas presentar tu nombre, NSS, domicilio, datos de contacto, UMA, parentesco, CURP, identificación oficial con fotografia, solicitud de inscripción y constancia de platica de nuevo ingreso. Ademas deberas presentar el nombre o razon social, domicilio y telefono y extensiones de tu lugar de trabajo.\n¿Hay algo más en lo que le pueda ayudar?',['incripcion', 'inscribir', 'hijo', 'hija', 'guarderia'],palabra_requeridas=['guarderia'])
        respuesta('Estoy para servirle', ['gracias', 'te lo agradezco', 'adios', 'nos vemos'], respuesta_simple = True)

        #Definimos que solo una respueta sera la mejor
        mejor_coincidencia = max(prob_alta, key=prob_alta.get)
        #print(prob_alta)

        #Retornamos la respuesta, si no encuentra una buena coincidencia muestra las respuestas por default
        return default() if prob_alta[mejor_coincidencia] < 1 else mejor_coincidencia

#Definimos el metodo para las respuestas por default
def default():
    #Permite mostrar varias respuestas al azar
    respuesta = ['¿Puedes volver a repetirlo?', 'No estoy seguro de lo quieres', 'No cuento con la información que necesitas'][random.randrange(3)]
    return respuesta

#Bucle infinito para que el bot no se cierre y siga habaldno con el usuario
while True:
    print("Bot: " + obtener_respuesta(input('Tu: ')))