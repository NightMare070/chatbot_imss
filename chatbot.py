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
        respuesta('Bienvenid@ al chatbot del IMMS. ??En que puedo ayudarte?', ['hola', 'saludos', 'buenas', 'saludo'], respuesta_simple = True)
        respuesta('Para realizar el alta de tu UMF deberas acudir a tu clinica mas cercana a tu domicilio con tu identificaci??n oficial, comprobante de domicilio, NSS, una fotografia infantil y acta de nacimiento.\n??Hay algo m??s en lo que le pueda ayudar?', ['alta', 'clinica', 'umf', 'resgistrar', 'registrarme', 'dar', 'darme'], palabra_requeridas=['alta'])
        respuesta('Para realizar la baja de un UMF deberas acudir a tu clinica mas cercana a tu domicilio con tu identificaci??n oficial, NSS, CURP y acta de defuncion en caso de muerte o acta de divorcio en caso de baja por divorcio.\n??Hay algo m??s en lo que le pueda ayudar?', ['baja', 'umf', 'clinica', 'dar', 'darme'], palabra_requeridas=['baja'])
        respuesta('Para realizar la actualizaci??n de tu UMF deberas acudir a tu clinica mas cercana a tu domicilio con tu identificaci??n oficial, comprobante de domicilio, NSS y una fotografia infantil.\n??Hay algo m??s en lo que le pueda ayudar?',['actualizar', 'cambiar', 'clinica', 'umf', 'modificar'])
        respuesta('Para obtener tu aviso para calificaci??n de accidente o enfermedad de trabajo ante el IMSS deberas acudir a tu clinica que te corresponda de acuerdo a tu domicilio con tu identificaci??n oficial, cartilla nacional de salud, aviso de atenci??n m??dica inicial y calificaci??n de probable accidente de trabajo ST-7 y ST-9. En caso de defunci??n sera acta de defunci??n, certificado de necropsia que incluya examen toxicol??gico copia certificada de la Averiguaci??n Previa del Ministerio P??blico y resumen medico de atenci??n inicial de servicios en caso de tenerlo.\n??Hay algo m??s en lo que le pueda ayudar?',['trabajo', 'laboral', 'calificacion', 'accidente', 'enfermedad'])
        respuesta('Para incribir a tu hijo a las guarderias del IMSS deberas acudir a la guarderia de tu interes o entrar al siguiente link:\nhttps://stigi.imss.gob.mx/\nen un horario de lunes a viernes de 7 a 19 horas con los siguientes datos de tu hijo/a: Nombre completo Fecha de nacimiento Acta de nacimiento Cartilla Nacional de Salud Examen Medico requisitado Tambien deberas presentar tu nombre, NSS, domicilio, datos de contacto, UMA, parentesco, CURP, identificaci??n oficial con fotografia, solicitud de inscripci??n y constancia de platica de nuevo ingreso. Ademas deberas presentar el nombre o razon social, domicilio y telefono y extensiones de tu lugar de trabajo.\n??Hay algo m??s en lo que le pueda ayudar?',['incripcion', 'inscribir', 'hijo', 'hija', 'guarderia'],palabra_requeridas=['guarderia'])
        respuesta('Para obtener tu constancia de no derechohabiente deberas ingresar al siguiente link http://www.imss.gob.mx/constancia-no-derechohabiencia con tu CURP y correo electronico donde se te enviara tu constancia con una validez de un d??a.\n??Hay algo m??s en lo que le pueda ayudar?', ['obtener', 'constancia', 'no', 'derechohabiente', 'sacar', 'sacarme'], palabra_requeridas=['no'])
        respuesta('Para realizar tu inscripci??n a cursos para representativos IMSS no derechohabientes deberas acudir a tu clinica mas cercana a tu domicilio con tu identificaci??n oficial, comprobante de domicilio, carta de autorizaci??n de padres o tutor en caso de ser menor de edad y contancia firmada por el director de la unidad que lo acredite como representativo. Adem??s deberas presentar un pago de 80.00 pesos en el momento de tu tramite.\n??Hay algo m??s en lo que le pueda ayudar?', ['inscribir', 'incribirme', 'curso', 'cursos', 'representativos', 'inscripcion', 'no', 'derechohabientes', 'derechohabiente'], palabra_requeridas=['no'])
        respuesta('Para reposici??n de tu credencial para usuarios de prestamos sociales deberas presentarte en ventanilla y mencionar que deseas reponer tu credencial. Recibiras una ficha de deposito para realizar el pago de tu reposici??n con un valor de 40.00 pesos  y deberas presentar tu ficha ya pagada nuevamente en ventanilla para recoger tu credencial.\n??Hay algo m??s en lo que le pueda ayudar?', ['reposicion', 'reponer', 'credencial', 'prestamo', 'social', 'usuarios', 'usuario', 'prestamos', 'sociales'], palabra_requeridas=['credencial'])
        respuesta('Para obtener tu dictamen de incapacidad deberas acudir a tu clinica mas cercana a tu domicilio con tu Cartilla Nacinal de Salud, identificaci??n oficial, solicitud de beneficiario incapacitado ante el Control de Prestaciones de la Unidad de Medicina Familiar y pase del servicio de medicina familiar o de especialista m??dico de segundo ?? tercer nivel de Atenci??n a Salud en el Trabajo\n??Hay algo m??s en lo que le pueda ayudar?', ['obtener', 'sacar', 'dictamen', 'incapacidad', 'trabajo'], palabra_requeridas=['incapacidad'])
        respuesta('Para incribirte en alguno de los cursos que ofrece el IMSS deberas acudir a tu clinica m??s cercano a tu domicilio y presentar identificaci??n oficial, carta de autorizaci??n de tutor, ficha de deposito y en caso de ser derechohabiente credencial escolar y comprobante de domicilio. El pago que deberas de realizar sera de un valor de 80.00 pesos.\n??Hay algo m??s en lo que le pueda ayudar?', ['inscribir', 'incribirme', 'curso', 'cursos', 'inscripcion'])
        respuesta('Para realizar la regularizaci??n y/o correcci??n de sus datos acudir a su clinica o presentar su tramite desde internet a travez del siguiente link:\nhttps://serviciosdigitales.imss.gob.mx/correcciondatosasegurado-web-ciudadano/wizard/correccionDatosAsegurado/\n con los siguientes documentos a la mano: CURP, acta de nacimiento, identificaci??n oficial y un documento expedido por el IMSS que contenga su NSS. Adem??s en caso de realizar su tramite en linea debera tener un correo electronico donde se le hara llegar la confirmaci??n del tramite y en caso de tramite presencial debera presentar la solicitud de regularizaci??n y/o correcci??n de datos personales del asegurado que se encuentra en el siguinete link:\nhttp://www.imss.gob.mx/sites/all/statics/pdf/formatos/SolicRegCorreDatosPerso.pdf \n??Hay algo m??s en lo que le pueda ayudar?', ['datos', 'corregir', 'correcion', 'personales', 'regularizar', 'regularizacion', 'cambiar', 'cambio'], palabra_requeridas=['datos'])
        respuesta('Para solicitar pr??tesis externa, ortesis o ayuda t??cnica debera acudir a su clinica asiganada con su identificaci??n oficial, Cartilla Nacional de Salud y orden para la dotaci??n o reparaci??n de pr??tesis, ortesis o ayudas funcionales en un horario de: 8 a 20 horas de lunes a viernes.\n??Hay algo m??s en lo que le pueda ayudar?', ['solucitud', 'solicitar', 'protesis', 'ortesis', 'ayuda', 'tecnica'])
        respuesta('Este tramite cuenta con modalidad tanto presencial como en linea. Para realizar el tramite en linea debera entrar al siguiente link y tener a la mano un correo electronico donde le llegara toda la informaci??n y su CURP.\nhttps://serviciosdigitales.imss.gob.mx/gestionAsegurados-web-externo/asignacionNSS;JSESSIONIDASEGEXTERNO=Wmle4dHJBfUuckhnc0tp3p26Yf0mShg7udNAfPlNHRuL28mPSKA4!-1100133577\n Si desea realizar el tramite presencial debera acudir a su clinica m??s cercana de lunes a viernes de 8 a 15 horas con su acta de nacimeinto identificaci??n oficial, CURP y poder notarial en caso de que el registro de nacimiento se haya realizado por Autoridad Civil (DIF y PGR).\n??Hay algo m??s en lo que le pueda ayudar?', ['asignacion', 'asignar', 'nss', 'localizar', 'obtener', 'saber', 'asignen', 'den', 'pedir', 'localicen', 'numero', 'seguro', 'social'])
        respuesta('Para obetner su certificado de discapacidad con fines de aplicaci??n del art??culo 186 de la Ley del Impuesto Sobre la Renta debera acudir a su clinica asignada de lunes a vierns en un horario de 8 a 19 horas con los siguientes documentos: Solicitud de Certificado de Discapacidad que obtendra en el siguiente link: http://www.imss.gob.mx/sites/all/statics/pdf/tramites-varios/certif-186-solicitud-instructivo.pdf Identificaci??n oficial con fotografia y firma Copia del aviso de inscripci??n al IMSS del trabajador de la liquidaci??n del pago de cuotas obrero-patronales del Sistema ??nico de Autodeterminaci??n (SUA) o Emisi??n Mensual Anticipada (EMA).\n??Hay algo m??s en lo que le pueda ayudar?', ['obtener', 'sacar', 'certificado', 'discapacidad', 'articulo', '186'], palabra_requeridas=['certificado'])
        respuesta('Para solicitar la entrega de bienes rematados en una subasta del IMSS deberas presnetarte en la Oficina para Cobros donde se realizo la subasa de lunes a viernes de 8 a 15 con el acta de remates como postor ganador, recibo de pago efectuado del 90% del importe ofrecido en la puja e identificaci??n oficial. En caso de realizar el tramite un representante legal este debera traer poder notarial , carta poder ratificada y su identificaci??n oficial.\n??Hay algo m??s en lo que le pueda ayudar?', ['solicitar', 'entrega', 'bienes', 'subasta', 'rematados'], palabra_requeridas=['subasta'])
        respuesta('Para incorporar a su familia al seguro de salud del IMSS sin contar con un esquema de seguridad social podras realizar el tramite tanto en linea como en fisico. Para realizar tu tramite en linea deberas tener a la mano tu NSS y un correo electronico y entrar al siguiente enlace: https://serviciosdigitales.imss.gob.mx/portal-ciudadano-web-externo/home En caso de realizar tu tramite en fisico deberas acudir a tu clinica m??s cercana con  acta de matrimonio, identificaci??n oficial, CURP, comprobante de pago de anualidad anticipada, Acta de nacimeinto, comprobante de domicilio y cuestionario medico proporcionado por el IMSS.\n??Hay algo m??s en lo que le pueda ayudar?', ['familia', 'incorporacion', 'incorporar', 'seguro', 'imss'], palabra_requeridas=['familia'])
        respuesta('Estoy para servirle', ['gracias', 'agradezco', 'adios', 'vemos', 'no'], respuesta_simple = True)

        #Definimos que solo una respueta sera la mejor
        mejor_coincidencia = max(prob_alta, key=prob_alta.get)
        #print(prob_alta)

        #Retornamos la respuesta, si no encuentra una buena coincidencia muestra las respuestas por default
        return default() if prob_alta[mejor_coincidencia] < 1 else mejor_coincidencia

#Definimos el metodo para las respuestas por default
def default():
    #Permite mostrar varias respuestas al azar
    respuesta = ['??Puedes volver a repetirlo?', 'No estoy seguro de lo quieres', 'No cuento con la informaci??n que necesitas'][random.randrange(3)]
    return respuesta

#Bucle infinito para que el bot no se cierre y siga habaldno con el usuario
while True:
    print("Bot: " + obtener_respuesta(input('Tu: ')))