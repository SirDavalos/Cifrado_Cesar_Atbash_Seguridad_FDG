#importaciones
import Cifradores

texto = str(input("Escriba su texto: "))

cifrado = Cifradores.cifrar_atbash(texto)
print(cifrado)