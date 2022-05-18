#juego creado para practicar Python scripting
import random

jugador1 = input("Introduzca el nombre del primer jugador: ")
jugador2 = input("Introduzca el nombre del segundo jugador: ")

vocales = ["a", "e", "i", "o", "u"]

#el numero aleatorio va a ser un indice de vocales
v = random.randint(0, 4)

def check_vocales():
    palabraValida1 = False
    palabraValida2 = False

    while palabraValida1 == False:
        print(jugador1)
        pJug1 = input("Escriba una palabra: ")
        for i in pJug1:
            if vocales[v] not in pJug1:
                print("La palabra no es valida, debe contener la vocal indicada")
                pJug1 = input("Escriba una palabra: ")
            else:
                palabraValida1 = True
                while palabraValida2 == False:
                    print(jugador2)
                    pJug2 = input("Escriba una palabra: ")
                    for i in pJug1:
                        if vocales[v] not in pJug1:
                            print("La palabra no es valida, debe contener la vocal indicada")
                            pJug2 = input("Escriba una palabra: ")
                        else:
                            "\n"
                            palabraValida2 = True
    print("Listos para jugar!")

#codigo principal
print("La vocal con la que van a jugar es: ", vocales[v], "\n")
check_vocales()