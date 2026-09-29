import re
import math
import unicodedata
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

def extraer_caracteres(texto):
    grafemas = []
    actual = ""
    for ch in texto:
        if unicodedata.combining(ch) or ch in ("\u200d", "\ufe0f"):
            actual += ch
        else:
            if actual:
                grafemas.append(actual)
            actual = ch
    if actual:
        grafemas.append(actual)
    return grafemas

#1.1
def Mayusculas(texto):
    resultados = []
    for caracter in extraer_caracteres(texto):
        if caracter.isalpha():
            mayus = caracter.upper()
            if len(mayus) == 1:
                resultados.append(mayus)
            else:
                resultados.append(caracter)
        else:
            resultados.append(caracter)

    return "".join(resultados)

#1.2
def preparar_alfabeto(alfabeto):

    grafemas = extraer_caracteres(alfabeto)
    indice = {grafema: i for i, grafema in enumerate(grafemas)}
    return grafemas, indice

#2
def cifrar_cesar(texto, alfabeto, cambio):

    grafemas_alfabeto, indice_alfabeto = preparar_alfabeto(alfabeto)

    #2.2
    longitud = len(grafemas_alfabeto)
    resultado = []
    #2.4
    for caracter in extraer_caracteres(texto):

        if caracter in indice_alfabeto:
            index = indice_alfabeto[caracter]
            nuevo_indice = (index + cambio) % longitud
            char_cambiado = grafemas_alfabeto[nuevo_indice]

        elif caracter.isalpha() and Mayusculas(caracter) in indice_alfabeto:
            es_minuscula = caracter.islower()
            clave = Mayusculas(caracter)
            index = indice_alfabeto[clave]

            #2.4.1
            nuevo_indice = (index + cambio) % longitud
            char_cambiado = grafemas_alfabeto[nuevo_indice]

            if es_minuscula:
                char_cambiado = char_cambiado.lower()
        else:
            #2.4.2
            char_cambiado = caracter

        #2.5
        resultado.append(char_cambiado)

    return "".join(resultado)

#3
def descifrar_cesar(texto_cif, alfabeto, desplazamiento):

    grafemas_alfabeto, indice_alfabeto = preparar_alfabeto(alfabeto)
    n = len(grafemas_alfabeto)
    resultado = []
    #3.1

    for caracter in extraer_caracteres(texto_cif):

        if caracter in indice_alfabeto:

            numero = indice_alfabeto[caracter]
            numero = (numero - desplazamiento) % n

            if numero < 0:
                numero = numero + n

            resultado.append(grafemas_alfabeto[numero])

        elif caracter.isalpha() and Mayusculas(caracter) in indice_alfabeto:
            es_minuscula = caracter.islower()
            clave = Mayusculas(caracter)
            numero = indice_alfabeto[clave]
            numero = (numero - desplazamiento) % n

            if numero < 0:
                numero = numero + n

            letra_descifrada = grafemas_alfabeto[numero]

            if es_minuscula:
                letra_descifrada = letra_descifrada.lower()

            resultado.append(letra_descifrada)
        else:
            resultado.append(caracter)

    return "".join(resultado)

#4
def conseguir_descifrado(texto_cif, alfabeto):

    grafemas_alfabeto, _ = preparar_alfabeto(alfabeto)
    n = len(grafemas_alfabeto) #4.1
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
    n = len(extraer_caracteres(alfabeto)) if texto else 1

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

    texto_normalizado = Mayusculas(texto)

    return (puntuacion_frecuencias(texto_normalizado, alfabeto)
            + puntuacion_palabras(texto_normalizado, alfabeto)
            + puntuacion_patrones(texto_normalizado, alfabeto))

#8

def cifrar_atbash(texto, alfabeto):
    #8.1
    grafemas_alfabeto, indice_alfabeto = preparar_alfabeto(alfabeto)
    n = len(grafemas_alfabeto)
    resultado = []
    #8.2
    for caracter in extraer_caracteres(texto):

        if caracter in indice_alfabeto:
            #8.3
            indice = indice_alfabeto[caracter]
            nuevo_indice = n - indice - 1
            resultado.append(grafemas_alfabeto[nuevo_indice])

        elif caracter.isalpha() and Mayusculas(caracter) in indice_alfabeto:
            es_minuscula = caracter.islower()
            clave = Mayusculas(caracter)
            indice = indice_alfabeto[clave]
            nuevo_indice = n - indice - 1
            char_cambiado = grafemas_alfabeto[nuevo_indice]

            if es_minuscula:
                char_cambiado = char_cambiado.lower()

            resultado.append(char_cambiado)
        else:
            #8.4
            resultado.append(caracter)

    #8.5
    return "".join(resultado)

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