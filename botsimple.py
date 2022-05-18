#Bot de ayuda para tramites del IMSS
#Definimos el saludo de inicio
def saludo():
    print("Bienvenido al chatbot del IMSS. Puedo ayudarte a resolver tus dudas sobre algún tramite.")
    print("Para empezar quisiera saber a quien esta dirigido su tramite.")
    print("1. Menor de edad")
    print("2. Mayor de edad")
    global entrada
    entrada = input()
    opciones.edad(entrada)

#Definimos una clase con todos los menus
class menus:
    #Definimos las categorias de menor de edad
    def categorias_menor():
        print("¿Qué tipo de tramite desea realizar?")
        print("1. Tramite relacionado con UMF o clinica")
        print("2. Tramite relacionado con guarderias")
        print("3. Tramite relacionado con prótesis, ortesis o ayuda técnica.")
        entrada = input()
        opciones.menor(entrada)
        
    #Definimos las categorias de mayor de edad
    def categorias_mayor():
        print("¿Qué tipo de tramite desea realizar?")
        print("1. Tramite relacionado con UMF o clinica")
        print("2. Tramite relacionado con no derechohabientes")
        print("3. Tramite relacionado con tu trabajo")
        print("4. Tramite relacionado con tu familia")
        print("5. Otros tramites fuera de las categorías anteriores")
        entrada = input()
        opciones.mayor(entrada)
        
    #Definimos los menus de tramites de menor de edad
    #Tramites relacionados con UMF o clinica (tambien servira para mayor de edad ya que tenemos la misma categoria)
    def umf():
        print("Seleccione el tramite deseado")
        print("1. Darse de alta en su UMF ")
        print("2. Darse de baja en su UMF ")
        print("3. Actualizar o cambiar su UMF ")
        entrada = input()
        tramites.umf(entrada)
    
    #Tramites relacionados con guarderias
    def menor_guarderia():
        print("Seleccione el tramite deseado")
        print("1. Inscribir a tu hijo a guarderías IMSS")
        entrada = input()
        tramites.guarderia(entrada)
    
    #Tramites relacionados con prótesis, ortesis o ayuda técnica
    def menor_protesis():
        print("Seleccione el tramite deseado")
        print("1. Solicitar prótesis externa, ortesis o ayuda técnica. ")
        entrada = input()
        tramites.protesis(entrada)

    #Definimos los menus de tramites de mayor de edad
    def mayor_noderecho():
        print("Seleccione el tramite deseado")
        print("1. Constancia de no derechohabiente")
        print("2. Inscripción a cursos representativos IMSS no derechohabiente")
        entrada = input()
        tramites.noDerecho(entrada)

    def mayor_trabajo():
        print("Seleccione el tramite deseado")
        print("1. Aviso de calificación para accidente o enfermedad de trabajo")
        print("2. Dictamen de incapacidad")
        print("3. Certificado de discapacidad con fines de aplicación del artículo 186")
        entrada = input()
        tramites.trabajo(entrada)
    
    def mayor_familia():
        print("Seleccione el tramite deseado")
        print("1. Incorporar a su familia al seguro de salud del IMSS")
        entrada = input()
        tramites.familia(entrada)
    
    def mayor_otros():
        print("Seleccione el tramite deseado")
        print("1. Reposición de credencial para usuarios de prestamos sociales")
        print("2. Solicitar prótesis externa, ortesis o ayuda técnica.")
        print("3. Inscripción a cursos ofrecidos por el IMSS")
        print("4. Regularización o corrección de tus datos personales")
        print("5. Recuperación u obtención de tu NSS")
        print("6. Solicitar la entrega de bienes rematados en una subasta del IMSS")
        entrada = input()
        tramites.otros(entrada)

#Definimos una clase con las acciones de cada opcion
class opciones:
    def edad(entrada):
        if entrada == "1":
            menus.categorias_menor()
        if entrada == "2":
            menus.categorias_mayor()
            
    def menor(entrada):
        if entrada == "1":
            menus.umf()
        if entrada == "2":
            menus.menor_guarderia()
        if entrada == "3":
            menus.menor_protesis()
            
    def mayor(entrada):
        if entrada == "1":
            menus.umf()
        if entrada == "2":
            menus.mayor_noderecho()
        if entrada == "3":
            menus.mayor_trabajo()
        if entrada == "4":
            menus.mayor_familia()
        if entrada == "5":
            menus.mayor_otros()

#Definimos una clase con las instrucciones de cada tramite
class tramites:
    def umf(entrada):
        if entrada == "1":
            print("Para realizar el alta de tu UMF deberas acudir a tu clinica mas cercana a tu domicilio con tu identificación oficial, comprobante de domicilio, NSS, una fotografia infantil y acta de nacimiento")
        if entrada == "2":
            print("Para realizar la baja de un UMF deberas acudir a tu clinica mas cercana a tu domicilio con tu identificación oficial, NSS, CURP y acta de defuncion o acta de divorcio en caso de baja por divorcio")
        if entrada == "3":
            print("Para realizar la actualización de tu UMF deberas acudir a tu clinica mas cercana a tu domicilio con tu identificación oficial, comprobante de domicilio, NSS y una fotografia infantil")

    def guarderia(entrada):
        if entrada == "1":
            print("Para incribir a tu hijo a las guarderias del IMSS deberas acudir a la guarderia de tu interes o entrar al siguiente link:\nhttps://stigi.imss.gob.mx/\nen un horario de lunes a viernes de 7 a 19 horas con los siguientes datos de tu hijo/a: Nombre completo Fecha de nacimiento Acta de nacimiento Cartilla Nacional de Salud Examen Medico requisitado Tambien deberas presentar tu nombre, NSS, domicilio, datos de contacto, UMA, parentesco, CURP, identificación oficial con fotografia, solicitud de inscripción y constancia de platica de nuevo ingreso. Ademas deberas presentar el nombre o razon social, domicilio y telefono con extensiones de tu lugar de trabajo.")

    def protesis(entrada):
        if entrada == "1":
            print("Para solicitar prótesis externa, ortesis o ayuda técnica debera acudir a su clinica asiganada con su identificación oficial, Cartilla Nacional de Salud y orden para la dotación o reparación de prótesis, ortesis o ayudas funcionales en un horario de: 8 a 20 horas de lunes a viernes.")

    def noDerecho(entrada):
        if entrada == "1":
            print("Para obtener tu constancia de no derechohabiente deberas ingresar al siguiente link\nhttp://www.imss.gob.mx/constancia-no-derechohabiencia\n con tu CURP y correo electronico donde se te enviara tu constancia con una validez de un día.")
        if entrada == "2":
            print("Para realizar tu inscripción a cursos para representativos IMSS no derechohabientes deberas acudir a tu clinica mas cercana a tu domicilio con tu identificación oficial, comprobante de domicilio, carta de autorización de padres o tutor en caso de ser menor de edad y contancia firmada por el director de la unidad que lo acredite como representativo. Además deberas presentar un pago de 80.00 pesos en el momento de tu tramite.")

    def trabajo(entrada):
        if entrada == "1":
            print("Para obtener tu aviso para calificación de accidente o enfermedad de trabajo ante el IMSS deberas acudir a tu clinica que te corresponda de acuerdo a tu domicilio con tu identificación oficial, cartilla nacional de salud, aviso de atención médica inicial y calificación de probable accidente de trabajo ST-7 y ST-9. En caso de defunción sera acta de defunción, certificado de necropsia que incluya examen toxicológico copia certificada de la Averiguación Previa del Ministerio Público y resumen medico de atención inicial de servicios en caso de tenerlo")
        if entrada == "2":
            print("Para obtener tu dictamen de incapacidad deberas acudir a tu clinica mas cercana a tu domicilio con tu Cartilla Nacinal de Salud, identificación oficial, solicitud de beneficiario incapacitado ante el Control de Prestaciones de la Unidad de Medicina Familiar y pase del servicio de medicina familiar o de especialista médico de segundo ó tercer nivel de Atención a Salud en el Trabajo")
        if entrada == "3":
            print("Para obtener su certificado de discapacidad con fines de aplicación del artículo 186 de la Ley del Impuesto Sobre la Renta debera acudir a su clinica asignada de lunes a vierns en un horario de 8 a 19 horas con los siguientes documentos: Solicitud de Certificado de Discapacidad que obtendra en el siguiente link: \nhttp://www.imss.gob.mx/sites/all/statics/pdf/tramites-varios/certif-186-solicitud-instructivo.pdf\n Identificación oficial con fotografia y firma Copia del aviso de inscripción al IMSS del trabajador de la liquidación del pago de cuotas obrero-patronales del Sistema Único de Autodeterminación (SUA) o Emisión Mensual Anticipada (EMA)")

    def familia(entrada):
        if entrada == "1":
            print("Para incorporar a su familia al seguro de salud del IMSS sin contar con un esquema de seguridad social podras realizar el tramite tanto en linea como en fisico. Para realizar tu tramite en linea deberas tener a la mano tu NSS y un correo electronico y entrar al siguiente enlace: \nhttps://serviciosdigitales.imss.gob.mx/portal-ciudadano-web-externo/home\n En caso de realizar tu tramite en fisico deberas acudir a tu clinica más cercana con  acta de matrimonio, identificación oficial, CURP, comprobante de pago de anualidad anticipada, Acta de nacimeinto, comprobante de domicilio y cuestionario medico proporcionado por el IMSS.")

    def otros(entrada):
        if entrada == "1":
            print("Para reposición de tu credencial para usuarios de prestamos sociales deberas presentarte en ventanilla y mencionar que deseas reponer tu credencial. Recibiras una ficha de deposito para realizar el pago de tu reposición con un valor de 40.00 pesos  y deberas presentar tu ficha ya pagada nuevamente en ventanilla para recoger tu credencial.")
        if entrada == "2":
            print("Para solicitar prótesis externa, ortesis o ayuda técnica debera acudir a su clinica asiganada con su identificación oficial, Cartilla Nacional de Salud y orden para la dotación o reparación de prótesis, ortesis o ayudas funcionales en un horario de: 8 a 20 horas de lunes a viernes.")
        if entrada == "3":
            print("Para incribirte en alguno de los cursos que ofrece el IMSS deberas acudir a tu clinica más cercano a tu domicilio y presentar identificación oficial, carta de autorización de tutor, ficha de deposito y en caso de ser derechohabiente credencial escolar y comprobante de domicilio. El pago que deberas de realizar sera de un valor de 80.00 pesos.")
        if entrada == "4":
            print("Para realizar la regularización y/o corrección de sus datos acudir a su clinica o presentar su tramite desde internet a travez del siguiente link: \nhttps://serviciosdigitales.imss.gob.mx/correcciondatosasegurado-web-ciudadano/wizard/correccionDatosAsegurado/\n con los siguientes documentos a la mano: CURP, acta de nacimiento, identificación oficial y un documento expedido por el IMSS que contenga su NSS. Además en caso de realizar su tramite en linea debera tener un correo electronico donde se le hara llegar la confirmación del tramite y en caso de tramite presencial debera presentar la solicitud de regularización y/o corrección de datos personales del asegurado que se encuentra en el siguinete link: \nhttp://www.imss.gob.mx/sites/all/statics/pdf/formatos/SolicRegCorreDatosPerso.pdf\n")
        if entrada == "5":
            print("Este tramite cuenta con modalidad tanto presencial como en linea. Para realizar el tramite en linea debera entrar al siguiente link y tener a la mano un correo electronico donde le llegara toda la información y su CURP. \nhttps://serviciosdigitales.imss.gob.mx/gestionAsegurados-web-externo/asignacionNSS;JSESSIONIDASEGEXTERNO=Wmle4dHJBfUuckhnc0tp3p26Yf0mShg7udNAfPlNHRuL28mPSKA4!-1100133577\n Si desea realizar el tramite presencial debera acudir a su clinica más cercana de lunes a viernes de 8 a 15 horas con su acta de nacimeinto identificación oficial, CURP y poder notarial en caso de que el registro de nacimiento se haya realizado por Autoridad Civil (DIF y PGR).")
        if entrada == "6":
            print("Para solicitar la entrega de bienes rematados en una subasta del IMSS deberas presnetarte en la Oficina para Cobros donde se realizo la subasa de lunes a viernes de 8 a 15 con el acta de remates como postor ganador, recibo de pago efectuado del 90% del importe ofrecido en la puja e identificación oficial. En caso de realizar el tramite un representante legal este debera traer poder notarial , carta poder ratificada y su identificación oficial.")

#Al invocar la función saludo, se ejecuta el bot y sigue su camino en base a las selecciones del usuario
saludo()