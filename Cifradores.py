import re
import math
from collections import Counter

#1
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

#1.1
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

#2
def cifrar_cesar(texto, alfabeto, cambio):

    #2.1
    alfabeto = Mayusculas(alfabeto)

    #2.2
    longitud = len(alfabeto)
    #2.3
    texto = texto.upper()
    texto_cif = ""
    #2.4
    for caracter in texto:
        if caracter in alfabeto:

            index = alfabeto.index(caracter)

            #2.4.1
            nuevo_indice = (index + cambio) % longitud

            char_cambiado = alfabeto[nuevo_indice]
        else:
            #2.4.2
            char_cambiado = caracter

        #2.5
        texto_cif += char_cambiado

    return texto_cif #Cadena cifrada

#3
def descifrar_cesar(texto_cif, alfabeto, desplazamiento):

    alfabeto = Mayusculas(alfabeto)
    texto_decifrado = ""
    #3.1
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

#4
def conseguir_descifrado(texto_cif, alfabeto):

    n = len(alfabeto) #4.1
    resultados = []
    #4.2
    for desplazamiento in range(n):

        texto_decifrado = descifrar_cesar(texto_cif, alfabeto, desplazamiento)

        #4.3
        puntuacion = puntuacion_total(texto_decifrado, alfabeto)

        #4.4
        resultados.append({
            "desplazamiento": desplazamiento,
            "texto": texto_decifrado,
            "puntuacion": puntuacion
        })

    valor_maximo = max(resultados, key=lambda resultados: resultados["puntuacion"])

    return valor_maximo #4.5

#5
def puntuacion_frecuencias(texto, alfabeto):

    count = Counter(texto)
    n = len(alfabeto) if texto else 1

    puntuacion = 0

    # 5.1
    for caracter in texto:
        if caracter.isalpha():
            puntuacion += 5

    #5.2
    for caracter, frecuencias_esperada in frecuencias_esp.items():

        frecuencia_conseguida = (count.get(caracter, 0)) / n

        diferencia = abs(frecuencia_conseguida - frecuencias_esperada)

        puntuacion -= diferencia

    return puntuacion #5.3

def puntuacion_palabras(texto, alfabeto):

    palabras = texto.split()

    puntuacion = 0

    for palabra_cruda in palabras:

        #6
        palabra = re.sub(r"[^A-ZÁÉÍÓÚÜÑ]", "", palabra_cruda)

        if palabra in PALABRAS_ES:
            #6.1
            puntuacion += 10 + len(palabra)

    return puntuacion

def puntuacion_patrones(texto, alfabeto):
    puntuacion = 0

    #7
    for patron, peso in PATRONES_ES.items():
        puntuacion += texto.count(patron) * peso

    return puntuacion

#7.1
def puntuacion_total(texto, alfabeto):

    return puntuacion_frecuencias(texto, alfabeto) + puntuacion_palabras(texto, alfabeto) + puntuacion_patrones(texto, alfabeto)

#8

def cifrar_atbash(texto, alfabeto):
    #8.1
    texto = Mayusculas(texto)
    alfabeto = Mayusculas(alfabeto)
    n = len(alfabeto)
    texto_cif = ""
    #8.2
    for caracter in texto:
        if caracter in alfabeto:
            #8.3
            indice = alfabeto.index(caracter)
            nuevo_indice = n - indice -1
            texto_cif += alfabeto[nuevo_indice]
        else:
            #8.4
            texto_cif += caracter

    #8.5
    return texto_cif

#9
def probar_atbash(texto_cif, alfabeto, valor_cesar):

    alfabeto= Mayusculas(alfabeto)

    n = len(alfabeto)
    resultados = []

    #9.1
    texto_decifrado = cifrar_atbash(texto_cif, alfabeto)

    puntuacion = puntuacion_total(texto_decifrado, alfabeto)

    if puntuacion > valor_cesar["puntuacion"]:
        return True

    #9.2
    return False