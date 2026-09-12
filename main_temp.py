#importaciones
import Cifradores

alfabeto = Cifradores.leer_cadenaCif()
texto = str(input("Escriba su texto: "))
cambio = int(input("Escriba su numero de cambio: "))


cifrado = Cifradores.cifrar_cesar(texto,alfabeto, cambio)
#cifrado = Cifradores.cifrar_atbash(texto, alfabeto)
print(cifrado)
alfabeto = Cifradores.Mayusculas(alfabeto)
valor_cesar = Cifradores.conseguir_descifrado(cifrado, alfabeto)
texto_descf = Cifradores.conseguir_descifrado(cifrado, alfabeto)

if Cifradores.probar_atbash(cifrado, alfabeto, valor_cesar):
    print("Es Atbash")
print(texto_descf)