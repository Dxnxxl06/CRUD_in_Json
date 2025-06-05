import os
import json


fichero = "contacts.json"
Datos = []
contacto=[]




def crearContacto():
    fichero = "contacts.json"

    nombre = input("Ingrese Nombre: ")
    telefono = input("Ingrese Telefono: ")
    email = input("Ingrese E-mail: ")

    try:
        with open(fichero, 'r', encoding='utf-8') as file:
            contactos = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        contactos = []

    if contactos:
        max_id = max(int(c.get('Id', 0)) for c in contactos if str(c.get('Id', '')).isdigit())
        nuevo_id = str(max_id + 1)
    else:
        nuevo_id = "1"

    contacto = {
        "Id": nuevo_id,
        "Nombre": nombre,
        "Telefono": telefono,
        "E-mail": email
    }

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
        print(f"Id: {contacto.get('Id','N/A')}, Nombre: {contacto.get('Nombre','N/A')}, Telefono: {contacto.get('Telefono','N/A')}, E-mail: {contacto.get('E-mail','N/A')}")
    
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

def reiniciar_contactos():
    with open(fichero, 'w', encoding='utf-8') as file:
        json.dump([], file, indent=2, ensure_ascii=False)
    print("Archivo de contactos reiniciado.")


menu = '''
▒█▀▄▀█ ▒█▀▀▀ ▒█▀▀▀█ ▀█▀ ▒█▄░▒█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ 
▒█▒█▒█ ▒█▀▀▀ ░▀▀▀▄▄ ▒█  ▒█▒█▒█ ▒█░▄▄ ▒█▀▀▀ ▒█▄▄▀ 
▒█░░▒█ ▒█▄▄▄ ▒█▄▄▄█ ▄█▄ ▒█░░▀█ ▒█▄▄█ ▒█▄▄▄ ▒█░▒█

      1. CREAR CONTACTO
      2. MOSTRAR CONTACTOS
      3. ACTUALIZAR CONTACTOS
      4. ELIMINAR CONTACTOS
      5. REINICIAR CONTACTOS
      6.SALIR
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
        reiniciar_contactos()
        print("Contactos reiniciados")

    elif opcion == 6:
        input("Presione enter para salir...")
        print("Saliendo del programa...")
        break

    else: 
        print("Opcion no valida")