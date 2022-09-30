import os

def dias_a_(dias):
    horas = dias * 24
    minutos = horas * 60
    segundos = minutos * 60
    
    return f"{horas} horas, {minutos} minutos, {segundos} segundos."

os.system("cls")

while True:
    try:
        print ("\t.:De días a horas, minutos y segundos:.")
    
        x = int (input ("Introduce la cantidad de días que quieres transformar: "))
        print (f"{x} días equivale a : {dias_a_(x)}\n")

        option = input("¿Desea continuar?(y/n): ")

        if option == "n":
            print ("Gracias por usar la calculadora\n")
            break

        elif option == "y":
            print ("")
            continue
        else: 
            print ("Opción incorrecta.\n")
            option = input("¿Desea continuar?(y/n): ")
            continue

    except:
            print ("Opción inválida.\n")
