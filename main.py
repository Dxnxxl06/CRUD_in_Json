from ast import Return
import os
import json


fichero = "contacts.json"
Datos = []
contacto=[]



def crearContacto():
    contacto = {
        "Id": input("Ingrese Id: "),
        "Nombre": input("Ingrese Nombre: "),
        "Telefono": input("Ingrese Telefono: "),
        "E-mail": input("Ingrese E-mail: ")
    }
    # Leer contactos existentes
    try:
        with open(fichero, 'r', encoding='utf-8') as file:
            contactos = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        contactos = []

    contactos.append(contacto)

    with open(fichero, 'w', encoding='utf-8') as file:
        json.dump(contactos, file, indent=2, ensure_ascii=False)

    print("Contacto guardado exitosamente.")

def print_contactos():
    fichero = "contacts.json"  

    try:
        with open(fichero, 'r', encoding='utf-8') as file:
            contactos = json.load(file)  
    except FileNotFoundError:
        print("NO hay contactos aún :(")
        return  

    if not contactos:  
            print("NO hay contactos registrados.")
            return

    print("Contactos:")
    for contacto in contactos:
        print(f"Id: {contacto['Id']}, Nombre: {contacto['Nombre']}, Telefono: {contacto['Telefono']}, E-mail: {contacto['E-mail']}")

def actualizar_contacto():
    fichero = "contacts.json"

    try:
        with open(fichero, 'r', encoding='utf-8') as file:
            contactos = json.load(file)
    except FileNotFoundError:
        print("NO hay contactos aún :(")
        return

    id_contacto = input("Ingrese el Id del contacto a actualizar: ")
    for contacto in contactos:
        if contacto['Id'] == id_contacto:
            contacto['Nombre'] = input("Ingrese nuevo Nombre: ")
            contacto['Telefono'] = input("Ingrese nuevo Telefono: ")
            contacto['E-mail'] = input("Ingrese nuevo E-mail: ")
            break
    else:
        print("Contacto no encontrado.")
        return

    with open(fichero, 'w', encoding='utf-8') as file:
        json.dump(contactos, file, indent=2, ensure_ascii=False)

    print("Contacto actualizado exitosamente.")

def eliminar_contacto():
    fichero = "contacts.json"
    try:
        with open(fichero, 'r', encoding='utf-8') as file:
            contactos = json.load(file)
    except FileNotFoundError:
        print("No hay contactos aun")
        return
    id_contacto = input("Ingrese el numero de id del contacto que quiere eliminar: ")
    for i, contacto in enumerate(contactos):
        if contacto['Id'] == id_contacto:
            del contactos[i]
            with open(fichero, 'w', encoding='utf-8') as file:
                json.dump(contactos, file, indent=2, ensure_ascii=False)
            print("Contacto eliminado exitosamente.")
            break
    else:
        print("Contacto no encontrado.")

menu = '''
▒█▀▄▀█ ▒█▀▀▀ ▒█▀▀▀█ ▀█▀ ▒█▄░▒█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ 
▒█▒█▒█ ▒█▀▀▀ ░▀▀▀▄▄ ▒█  ▒█▒█▒█ ▒█░▄▄ ▒█▀▀▀ ▒█▄▄▀ 
▒█░░▒█ ▒█▄▄▄ ▒█▄▄▄█ ▄█▄ ▒█░░▀█ ▒█▄▄█ ▒█▄▄▄ ▒█░▒█

      1. CREAR CONTACTO
      2. MOSTRAR CONTACTOS
      3. ACTUALIZAR CONTACTOS
      4. ELIMINAR CONTACTOS
      5. SALIR
'''

while True:
    
    def limpiarConsola():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    print(menu)

    opcion = int(input("Ingrese opcion: "))

    if opcion == 1:
        crearContacto()
        input("Continuar...")
        
    elif opcion == 2:
        print_contactos()
        input("Continuar...") 

    elif opcion == 3:
        actualizar_contacto()
        input("Continuar...")

    elif opcion == 4:
        eliminar_contacto()
        input("Continuar...")

    elif opcion == 5:
        input("Presione enter para salir...")
        print("Saliendo del programa...")
        break