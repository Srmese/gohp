from random import randint
import os


def corregir(correcta):
    entrada = input("Introduzca la respuesta correcta:  ")
    while entrada != correcta:
        print("\n")
        entrada = input("Vuelve a intentarlo:  ")
    print("\nRespuesta correcta: ", correcta)

def preguntas(numero):
    numeroValido = True
    if numero == 4.1:
        print("Analisis DAFO\n")
        print("RECOEMNDACION: RELLENA EL ANALISIS DAFO EN TU PAPEL")
        print("\n\nVARIABLE DE PROCEDENCIA INTERNA:     \nA: AMENAZA  \nB: FUERZA \nC: FORTALEZA\nD: OPORTUNIDAD\n")
        corregir("B")
    
    elif numero == 4.2:
        print("Analisis Interno: cadena de valor\n")
        print("Dibuje la cadena de valor al completo\n")
        entrada = input("Pulse enter para ver la solucion")
        print("\n\n\nINFRAESTRUCTUA: ADMINISTACIONM SISTEMAS INFORMACION, FINANZAS\nGESTION DE RECURSOS HUMANOS: SELECCION, MOTIVACION, FORMACION\n")
        print("DESAROLLO DE LA TECNOLOGIA: I+D, SISTEMAS INFORMATICOS..\nAPROVISIONAMIENTO: FUNCION DE COMPRAS")
        print("\n\n\nLOGISTICA INTERNA: RECEPCION, ALMACENAMIENTO, CONTROL...\n     OPERACIONES: OBTENCION DE PRODUCTOS\n           LOGISTICA EXTERNA:ALMACENAMIENTO Y DISTRIBUCION DISICA\n                MARKETING\n                         SERVICIO: MANTENER CONDICIONES DE USO DEL PDTO\n\n\n MARGEN MARGEN MARGEN MARGEN                                    MARGEN MARGEN MARGEN")

    elif numero == 4.3:
        print("Fijacion de objetivos\n")
        print("Las funciones que deben cumplir los objetivos son:\nA: Guiar, incitar y coordinar las decisiones y acciones en el seno de la empresa\nB: Transmitir al exterior las intenciones de la empresa\nC: Mejorar la imagen de la empresa \nD: la a y b pero no la c \nE: la a y c pero no la b")
        corregir("D")
    
    elif numero == 4.4:
        print("Estrategias competitivs de negocio\n")
        print("Dibuja la tabla\n")  
        entrada = input("Pulse una tecla para continuar...")
        print("\n\n             AMPLIO      1.LIDERAZGO         2. DIFERENCIAZION")
        print("  \nAmbito                     EN COSTES")
        print("  \n             REDUCIDO     .............ENFOQUE...........     ")
        print("  \n             Coste                               Producto     ")
    elif numero == 4.5:
        print("Estategias corporativas\n")
        print("En que escenarios debe seguir una empresa una estrategia de estabilidad?")
        print("\nA: Ante la presencia de oportunidades y amenazas\nB: Ante la presencia de debilidades y fortalezas\nC: Ante la presencia de oportunidades y debilidades\n")
        corregir("C")
    elif numero == 4.6:
        print("ANSOFF")
        print("\nDibuja la tabla de Ansoff\n")
        entrada = input("Pulse para ver la solucion\n")
        print("\n                               Productos existentes                                    Nuevos productos")
        print("\n\nMercados existentes          1.Penetracion de mercado                            3. Desarollo de productos\n")        
        print("\n\nNuevos mercados              2.Desarollo de mercados                             4. Estrategias de diversificacion")
    elif numero == 4.7:
        print("Formas de crecimiento\n")
        print("Que dos formas de crecimiento existen?\n")
        print("A: Crecimiento en mercados y productos\nB: Crecimiento externo e interno\nC: Crecimiento de valor e imagen")
        corregir("A")
    
    elif numero == 5.1:
        print("Dibuja y explica los componenes de la estructura organizativa\n")
        entrada = input("Presiona para ver la respuesta")
        print("\nEsta en el 5.2 pag 13 de 49 en el tema 5 muy largo para ponerlo aqui")

    elif numero == 5.2:
        print("Mecanismos de coordinacion\n")
        print("\nQue mecanismos de coordinacion existen?\n")
        entrada = input("Escribelos a continuacion\n")
        print("El primero de todos es la Ad........:  ") 
        corregir("ADAPTACION MUTUA")
        print("\nEl siguiente es la Su...........:   ") 
        corregir("SUPERVISION DIRECTA")
        print("\nPor ultimo es...................:   ") 
        corregir("NORMALIZACION")
        print("\nEste ultimo se compone ademas de: \n")
        print("De pr.......:    ") 
        corregir("PROCESOS")
        print("De res......:    ") 
        corregir("RESULTADOS")
        print("De .........:    ") 
        corregir("HABILIDADES")

    elif numero == 5.3:
        print("\nTipos de departamentalizacion\n")
        print("Escribe todos los tipos de departamentalizacion a continuacion\n")
        print("El primero es el por fu.....:    ") 
        corregir("FUNCIONES")
        print("El segundo es el de por pro.:    ") 
        corregir("PROCESOS")
        print("El tercero es el de por ter.:    ") 
        corregir("TERRITORIOS")
        print("El cuarto es por prod.......:    ") 
        corregir("PRODUCTOS")
        print("El quinto es por c..........:    ") 
        corregir("CLIENTES")
        print("El sexto es el por mat......:    ") 
        corregir("MATRICIAL")
        print("El ultimo es el de d........:    ") 
        corregir("DIVISIONAL")

    elif numero == 7.1:
        print("Filosofias de la Direccion Comercial\n")
        print("Afirmacion 1: Orientacion Produccion, los consumidores se decantarán por adquirir aquellos productos que estén muy disponibles y sean de bajo coste.\n")
        print("Afirmacion 2: Orientacion Calidad, los consumidores se decantarán por adquirir aquellos productos que ofrezcan la mejor calidad o los mejores resultados\n")
        print("A: es cierta la afirmacion 1\nB: es cierta la afirmacion B\nC: Ambas son ciertas\nD: Ninguna es cierta")
        corregir("A")
        print("\n\n\nPregunta 2\n\n\n")
        print("Aemas de la Orientacion a producion que tres enfoques diferentes existe?\n")
        print("Introduce en mayusculas el endoque P......... :  ")
        corregir("PRODUCTO")
        print("\nAhora el enfoque V....")
        corregir("VENTAS")
        print("\El que queda: ")
        corregir("MARKETING")
    elif numero == 7.2:
        print("\nInvestigacion de los mercados: estrategias marketing\n")
        print("La SEGMENTACIÓN es un proceso de división del mercado\nen subgrupos (segmentos) homogéneos, de acuerdo con\nalgún criterio, para permitir poner en práctica una\nestrategia comercial diferenciada")
        print("\n\Definido lo que son segmentos, existen varias estrategias de marjeting en relacion a ellos, dibujelas en su cuaderno\n")
        entrada = input("Pulse al terminar")
        print("\nIndiferenciada:      Estrategia---->Mercado\n\nDiferenciada------>Estrategia 1,2,3...N ----> Segmento 1,2,3...N\n\nConcertada                Seg.1\n           Estrategia\n                          Seg.2")

    elif numero == 7.3:
        print("\nSegmentacion. Criterios\n")
        print("Indique que dos tipos de criterios existen:  G....O....E") 
        corregir("GENERALES O ESPECIFICOS") 
        print("""Afirmacion 1:    
        Generales. Estos criterios sirven para clasificar cualquier
        población o grupo de personas (sea o no un mercado) con
        independencia de sus pautas de compra y consumo. Los
        criterios o variables más utilizadas son:
        • Variables demográficas: sexo, edad, etc.
        • Variables socioeconómicas: renta, ocupación, etc.
        • Variables geográficas: región, hábitat, etc.
        • Estilos de vida: centros de interés, opiniones, etc.""")

        print("Es cierta?:  ")
        corregir("SI")

        print("""\n\nAfirmacion 2:
        Específicos. Estos criterios están relacionados con el
        producto o el proceso de compra. Suponen
        comportamientos, motivaciones, actitudes, percepciones y
        preferencias hacia el producto, la marca o el punto de venta.
        Los criterios o variables más utilizadas son:
        • Fidelidad/lealtad a la marca/empresa.
        • Tipo de compra: primera o de repetición
        • Preferencias.
        • Ventaja/beneficio buscado""")

        print("\nEs cierta?  ")
        corregir("SI")

    elif numero == 7.4:
        print("\nMarketing Mix\n")
        print("Indica las 4Ps en español")
        print("La primera es la poltica de p...")
        corregir("PRODUCTO")
        print("La segunda es la politica de pr...")
        corregir("PRECIO")
        print("La tercera es la politica de dist...")
        corregir("DISTRIBUCION")
        print("La ultima es la politca de pr...")
        corregir("PROMOCION") 
    else:
        numeroValido = False  
    
    return numeroValido
    

while(True):
    print("\n\nQue tema quieres repasar?   Ponga un numero de 1 al 10, en caso de todos, indiquelo con un 0\n\n")
    entrada = int(input("Introduzca un NUMERO:  "))
    os.system('cls')


    if entrada >= 0 and entrada < 11:
        i = 0
    else:
        i = 11
    while i<10:
        if entrada == 0:
            elegir_preguntas = randint(1, 10) + randint(1, 9)*0.10
        else: 
            elegir_preguntas = entrada + randint(1,9)*0.10
        
        if(preguntas(elegir_preguntas)):
            i += 1
            c = input("\n\n\nPulsa para continuar")
            os.system('cls')

        

