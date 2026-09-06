#cifrado cesar
def cifrar_cesar(texto, cambio):

    #Convertir el texto en su version de ASCII
    texto_cif = ""
    #Cambiamos los caracteres de lugar
    for caracter in texto:

        if caracter.isalpha():
            #Caso minusculas
            if caracter.isupper():
                inicio = ord('A')
            #Caso mayusculas
            else:
                inicio = ord('a')

            #Desplazamos el caracter
            char_cambiado = chr((ord(caracter) - inicio + cambio) % 26 + inicio)

        else:
            #Mantiene espacios y caracteres especiales
            char_cambiado = caracter

        # agregamos el resultado en la cadena resultante
        texto_cif += char_cambiado

    return texto_cif #Cadena cifrada

#cifrado atbash

#Diccionario para el cifrado
diccionario = {
        'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'
}

def cifrar_atbash(texto):
    #Cambia el texto a mayusculas para poder ver el diccionario
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