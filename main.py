import os
import json


fichero = "contacts.json"
Datos = []
contacto=()

def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_contactos():
    fichero = "contactos.json"  

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


def crearContanto():
    contacto = {
        "Id": input("Ingrese Id: "),
        "Nombre": input("Ingrese Nombre: "),
        "Telefono": input("Ingrese Telefono: "),
        "E-mail": input("Ingrese E-mail: ")
    }
    with open(fichero, 'w', encoding='utf-8') as file:
        json.dump(contacto, file, indent=2, ensure_ascii=False)

        print("Contacto guardado exitosamente.")


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

    print(menu)

    opcion = int(input("Ingrese opcion: "))

    if opcion == 1:
        crearContanto()
        input("Continuar...")
        
    elif opcion == 2:
        print_contactos()
        input("Continuar...")
        