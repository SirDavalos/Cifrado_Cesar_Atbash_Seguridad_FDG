#Diccionario que incluye las frecuencias de aparicion de las letras en lenguaje español
import re
import math
from collections import Counter

#Elementos globales que se usaran para el descifrado
frecuencias_esp = {
    'A': 0.1218, 'B': 0.0142, 'C': 0.0468, 'D': 0.0586, 'E': 0.1325,
    'F': 0.0069, 'G': 0.0101, 'H': 0.0070, 'I': 0.0553, 'J': 0.0044,
    'K': 0.0002, 'L': 0.0497, 'M': 0.0315, 'N': 0.0671, 'Ñ': 0.0031,
    'O': 0.0841, 'P': 0.0251, 'Q': 0.0088, 'R': 0.0687, 'S': 0.0798,
    'T': 0.0463, 'U': 0.0393, 'V': 0.0090, 'W': 0.0001, 'X': 0.0022,
    'Y': 0.0090, 'Z': 0.0052, 'Á': 0.0050, 'É': 0.0043, 'Í': 0.0073,
    'Ó': 0.0083, 'Ú': 0.0017, 'Ü': 0.0001,
}

PALABRAS_ES = {
    "DE", "LA", "EL", "EN", "QUE", "Y", "A", "LOS", "SE",
    "DEL", "LAS", "UN", "POR", "CON", "NO", "UNA", "SU",
    "PARA", "ES", "AL", "LO", "COMO", "MÁS", "PERO", "SUS",
    "LE", "HA", "ME", "SI", "SIN", "SOBRE", "ESTE", "YA", "ENTRE",
    "CUANDO", "TODO", "ESTA", "SER", "SON", "DOS", "TAMBIÉN",
    "FUE", "HABÍA", "MUY", "AÑOS", "HASTA", "DESDE", "ESTÁ",
    "MI", "PORQUE", "QUÉ", "CÓMO", "DÓNDE", "QUIEN", "QUIÉN",
    "PUEDE", "HAY", "TIENE", "TENGO", "HOLA", "MUNDO", "MENSAJE",
    "CASA", "TIEMPO" }

PATRONES_ES = {
    "QUE": 5,
    "QUI": 3,
    "GUE": 3,
    "GUI": 3,
    "CON": 4,
    "DEL": 4,
    "LOS": 3,
    "LAS": 3,
    "EST": 3,
    "ENT": 3,
    "ION": 2,
    "CIÓN": 5,
    "MENTE": 5,
    "ADO": 2,
    "IDO": 2,
    "ANDO": 3,
    "IENDO": 3,
}

#Cifrado Cesar
#Funcion para cambiar las letras alphas a mayusculas
def Mayusculas(texto):
    resultados = []
    for caracter in texto:
        if caracter.isalpha():
            mayus = caracter.upper()
            if len(mayus) == 1:
                resultados.append(mayus)
            else:
                resultados.append(caracter)
        else:
            resultados.append(caracter)

    return "".join(resultados)

def leer_cadenaCif():
    return str(input("Ingrese cadena de cifrado: "))

def cifrar_cesar(texto, alfabeto, cambio):

    #Cambia el alfabeto a mayusculas
    alfabeto = Mayusculas(alfabeto)

    #Conseguir la longitud del alfabeto para las operaciones
    longitud = len(alfabeto)
    #Convertir el string a mayusculas
    texto = texto.upper()
    texto_cif = ""
    #Cambiamos los caracteres de lugar
    for caracter in texto:
        if caracter in alfabeto:

            index = alfabeto.index(caracter)

            #Desplazamos el caracter
            nuevo_indice = (index + cambio) % longitud

            char_cambiado = alfabeto[nuevo_indice]
        else:
            #Mantiene espacios y caracteres que no estan en la cadena
            char_cambiado = caracter

        # agregamos el resultado en la cadena resultante
        texto_cif += char_cambiado

    return texto_cif #Cadena cifrada

#Descifrado Cesar
def descifrar_cesar(texto_cif, alfabeto, desplazamiento):

    alfabeto = Mayusculas(alfabeto)
    texto_decifrado = ""
    for caracter in texto_cif:
        if caracter in alfabeto:
            numero = alfabeto.find(caracter)
            numero = (numero - desplazamiento) % len(alfabeto)

            if numero < 0:
                numero = numero + len(alfabeto)

            texto_decifrado += alfabeto[numero]
        else:
            texto_decifrado += caracter

    return texto_decifrado

#Funcion para verificar la probabilidad de cifrado correcta
def conseguir_descifrado(texto_cif, alfabeto):

    n = len(alfabeto)
    resultados = []
    for desplazamiento in range(n):

        texto_decifrado = descifrar_cesar(texto_cif, alfabeto, desplazamiento)

        puntuacion = puntuacion_total(texto_decifrado, alfabeto)

        resultados.append({
            "desplazamiento": desplazamiento,
            "texto": texto_decifrado,
            "puntuacion": puntuacion
        })

    valor_maximo = max(resultados, key=lambda resultados: resultados["puntuacion"])

    return valor_maximo

def conseguir_char(texto):
    return "".join(c for c in texto if c.isalpha())

def puntuacion_frecuencias(texto, alfabeto):

    count = Counter(texto)
    n = len(alfabeto) if texto else 1

    puntuacion = 0

    for caracter in texto:
        if caracter.isalpha():
            puntuacion += 5

    for caracter, frecuencias_esperada in frecuencias_esp.items():

        frecuencia_conseguida = (count.get(caracter, 0)) / n

        diferencia = abs(frecuencia_conseguida - frecuencias_esperada)

        puntuacion -= diferencia

    return puntuacion

def puntuacion_palabras(texto, alfabeto):

    palabras = texto.split()

    puntuacion = 0

    for palabra_cruda in palabras:

        palabra = re.sub(r"[^A-ZÁÉÍÓÚÜÑ]", "", palabra_cruda)

        if palabra in PALABRAS_ES:
            #Mientras mas larga la palabra, mas peso tiene
            puntuacion += 10 + len(palabra)

    return puntuacion

def puntuacion_patrones(texto, alfabeto):
    puntuacion = 0

    for patron, peso in PATRONES_ES.items():
        puntuacion += texto.count(patron) * peso

    return puntuacion

def puntuacion_total(texto, alfabeto):

    return puntuacion_frecuencias(texto, alfabeto) + puntuacion_palabras(texto, alfabeto) + puntuacion_patrones(texto, alfabeto)

#Cifrado Atbash

def cifrar_atbash(texto, alfabeto):
    #Cambia el texto a mayusculas para poder ver el diccionario
    texto = Mayusculas(texto)
    alfabeto = Mayusculas(alfabeto)
    n = len(alfabeto)
    texto_cif = ""
    #Invertir la posicion paras el cifrado
    for caracter in texto:
        if caracter in alfabeto:
            #Obtener la posicion inicial y opuesta
            indice = alfabeto.index(caracter)
            nuevo_indice = n - indice -1
            texto_cif += alfabeto[nuevo_indice]
        else:
            #Busca su valor en el diccionario
            texto_cif += caracter

    #Texto invertido
    return texto_cif

#Comprobar si la cadena es Cifrado Atbash
def probar_atbash(texto_cif, alfabeto, valor_cesar):

    alfabeto= Mayusculas(alfabeto)

    n = len(alfabeto)
    resultados = []

    #Cifrar_atbash se puede usar como decifrado
    texto_decifrado = cifrar_atbash(texto_cif, alfabeto)

    puntuacion = puntuacion_total(texto_decifrado, alfabeto)

    if puntuacion > valor_cesar["puntuacion"]:
        return True

    #Si no retorna el if, entonces la funcion retornas falso
    return False