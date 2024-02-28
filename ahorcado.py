import random
import string 

from  palabras import palabras
from ahorcadoDiagrama import vidas_diccionario_visual


def obtener_palabra_valida(palabras):
    #selecciinar una palabra al asaar de la lista de palabras validas
    palabra = random.choice(palabras)

    while '-' in palabra or ' 'in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()



def ahorcado ():

    print("================================")
    print("|| !Bienvenido(a)! al juego   ||")
    print("================================")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas= set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        #mostrar el estado actuyal de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        #mostrar estado de la horca
        print(vidas_diccionario_visual[vidas])
        #mostrar  leras separadas porm espacios
        print(f"palabras: {' '.join(palabra_lista)}")

        letra_usuario = input("escoge una letra: ").upper()


        # si la letra esa en el abecedario y no en el conjunto de letras
        #que se han ingresado se añadira al conjunto de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            #si la letra esta en el conjunto de letras
            #quitar  la letra del conjunto pendiete por adibinar
            #si no quitar una vida al usuario
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas = vidas -1
                print(f"\nTu letra, {letra_usuario} no esta en la palabra.")
        #si la legra ya fue ingresida
        elif letra_usuario in letras_adivinadas :
            print("\nYa escogiste esa letra. Porfavor escoge una letra nueva.")
        else :
            print("\nEsta letra no es válida")

