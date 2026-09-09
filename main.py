#importaciones
import Cifradores

alfabeto = Cifradores.leer_cadenaCif()
texto = str(input("Escriba su texto: "))
cambio = int(input("Escriba su numero de cambio: "))

cifrado = Cifradores.cifrar_cesar(texto,alfabeto, cambio)


print(cifrado)

print("Texto descifrado: ", Cifradores.descifrar_cesar(cifrado, alfabeto))