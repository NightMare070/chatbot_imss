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
            print("Categoria A")
        if entrada == "2":
            print("Categoria B")
        if entrada == "3":
            print("Categoria C")
        if entrada == "4":
            print("Categoria D")
        if entrada == "5":
            print("Categoria E")

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

#Al invocar la función saludo, se ejecuta el bot y sigue su camino en base a las selecciones del usuario
saludo()