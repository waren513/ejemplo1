def mostrar_menu():
    print("=======================")
    print("1.- Agregar Mascota  ")
    print("2.- Buscar Mascota ")
    print("3.- Eliminar Mascota  ")
    print("4.- Marcar como Vacunada  ")
    print("5.- Mostar Mascota  ")
    print("6.- Salir")
    print("=======================")
def validar_nombre(name):
    #strip() -> eliminar todos los espacios en blanco al inicio y al final de un string
    #Retorna True si es valido o false si no 
    return name.strip() != ""

def validar_especie(especie):
    especie_validados = ["perro", "gato", "ave"]
    #retorna True si lo consigue o False si no 
    return especie.strip().lower() in especie_validados

def validar_edad(edad):
    return edad.isdigit() and int(edad) > 0


def solicitar_opciones():
    while True:
        try:
            opcion = int(input("Ingrese una opcion:  "))
            if opcion < 1 or opcion > 6:
                print("Debe seleccionar una opcion del 1 al 6")
            else:
                break
        except ValueError:
            print("Debe ingresar un número")
    return opcion

def agregar_mascota(lista_m):
    #solicitamos los datos
    nombre = input("Ingrese el nombre de su mascota: ")
    correcta = validar_nombre(nombre)
    if not correcta: 
        print("El nombre no puede estar en blanco")
        return
    especie = input("Ingrese la especie (perro,gato o ave) ")
    correcta = validar_especie(especie)
    if not correcta: 
        print("La especie solo puede ser perro,gato o ave")
        return
    edad = input("Ingrese la edad de la mascota: ")
    correcta = validar_edad(edad)
    if not correcta: 
        print("La edad debe setr un número entero mayor a cero")
        return
    #agregar los datos al diccionario
    mascota = {
        "nombre": nombre.strip(),
        "especie": especie.strip().lower(),
        "edad": int(edad),
        "vacunada": False
    }
    #agregar a la lista 
    lista_m.append(mascota)
    print("Mascotas agregada correctamente")

#codigo principal
#declarar lista de mascota
datos_mascotas = []
op = 0
while op != 6:
    mostrar_menu()
    op = solicitar_opciones()

    if op == 1:
        agregar_mascota(datos_mascotas)
    elif op == 2:
        print()
    elif op == 3:
        print()
    elif op == 4:
        print()
    elif op == 5:
        print()
    elif op == 6:
        print("Gracias por usar el sitema")
    