
from operator import index

#Diccionario que incluye las frecuencias de aparicion de las letras en lenguaje español
frecuencias_esp = {
    'A' : 0.1172, 'Á' : 0.044, 'B' : 0.015, 'C' : 0.0387, 'D' : 0.0467, 'E' : 0.1372, 'É' : 0.0036 ,'F' : 0.0069, 'G' : 0.01,
    'H' : 0.0118, 'I' : 0.0528, 'Í' : 0.007, 'J' : 0.0052, 'K' : 0.0011, 'L' : 0.0524, 'M' : 0.0308, 'N': 0.0683,
    'Ñ' : 0.0017, 'O' : 0.0844, 'Ó' : 0.076, 'P' : 0.0289, 'Q' : 0.0111, 'R' : 0.0641, 'S' : 0.072, 'T' : 0.046,
    'U' : 0.0455, 'Ü' : 0.0002, 'Ú' : 0.0012, 'V' : 0.0105, 'W' : 0.0004, 'X' : 0.0014, 'Y' : 0.0109, 'Z' : 0.0047
}

#cadena que se usara para el cifrado y descifrado
def leer_cadenaCif():
    return str(input("Ingrese cadena de cifrado: ")).upper()

#cifrado cesar
def cifrar_cesar(texto, alfabeto, cambio):

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
            nuevo_indice = (index + cambio) % len(alfabeto)

            char_cambiado = alfabeto[nuevo_indice]
        else:
            #Mantiene espacios y caracteres que no estan en la cadena
            char_cambiado = caracter

        # agregamos el resultado en la cadena resultante
        texto_cif += char_cambiado

    return texto_cif #Cadena cifrada

def imprimir_diccionario():
    print(frecuencias_esp)

#Funcion para contar la frecuencia de aparicion
def conseguir_frecuencias(texto, alfabeto):
    #Se usara un diccionario para guardar la información
    texto = texto.upper()
    alfabeto = alfabeto.upper()
    contador = {letra: 0 for letra in alfabeto}
    total = 0

    for caracter in texto:
        if caracter in contador:
            contador[caracter] += 1
            total +=1

    if total == 0:
        return contador
    #Retorna un diccionario con los valores
    return {letra: (contador[letra] / total) for letra in alfabeto}

    diccionario_ord = sorted(diccionario.items(), key=operator.itemgetter(1), reverse=True)
    return
#Chi cuadrada, usado para facilitar la busqueda de frecuencias
def chi_cuadrado(frecuencias_texto, frecuencias_referencia = frecuencias_esp):
    total = 0
    #Mientras mas bajo sea "total", mas probable es que sea el valor real
    for letra, freq_esperada in frecuencias_referencia.items():
        freq_obtenida = frecuencias_texto.get(letra, 0)
        if freq_esperada > 0:
            total += ((freq_obtenida - freq_esperada) ** 2) / freq_esperada
    return total

#Desplazamiento
def buscar_desplazamiento(texto_cif, alfabeto):

    n = len(alfabeto)
    mejor_desplazamiento = 0
    mejor_puntuacion = float('inf') #Valor infinito para poder comparar
    puntuaciones = {}

    for desplazamiento in range(n):
        frecuencia_texto = conseguir_frecuencias(texto_cif, alfabeto)
        puntuacion_temp = chi_cuadrado(frecuencia_texto, frecuencias_esp) #Aqui se consigue el valor mas cercano
        puntuaciones[desplazamiento] = puntuacion_temp

        #Aqui se guardan los mejores valores, tanto de puntuacion como desplazamiento
        if puntuacion_temp < mejor_puntuacion:
            mejor_puntuacion = puntuacion_temp
            mejor_desplazamiento = desplazamiento

    return mejor_desplazamiento

#Descifrado Cesar
def descifrar_cesar(texto_cif, alfabeto):

    cambio = buscar_desplazamiento(texto_cif, alfabeto)
    print("Cambio calculado: ", cambio)
    tam = len(alfabeto)
    indice = {letra: i for i, letra in enumerate(alfabeto)}
    texto_decf = []

    for caracter in texto_cif:
        #Crear la cadena descifrada
        if caracter in alfabeto:
            posicion = (alfabeto[caracter] - cambio) % len(alfabeto) % tam
            texto_decf.append(letras[posicion])
        else:
            texto_decf.append(caracter)

    return "".join(texto_decf)

# cifrado atbash

def cifrar_atbash(texto):
    #Cambia el texto a mayusculas para poder ver el diccionario
    #Crea un diccionario que relaciona una letra con la letra inversa inverso
    diccionario = dict(zip(alfabeto, alfabeto[::-1]))
    #alfabeto_inv = {'A': 'Z', 'B':'Y',..., 'Z' : 'A'}
    texto = texto.upper()
    texto_cif = ""
    for caracter in texto:
        if caracter == ' ':
            #Agrega espacios al texto cifrado
            texto_cif += " "
        else:
            #Busca su valor en el diccionario
            texto_cif += diccionario[caracter]

    return texto_cif