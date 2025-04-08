import json
from colorama import init, Fore, Style
init(autoreset=True)

# Tupla de opciones del menú
menu_options = (
    "1. Registrar nuevo contacto",
    "2. Ver todos los contactos",
    "3. Eliminar un contacto",
    "4. Buscar contactos",
    "5. Guardar contactos en archivo",
    "6. Cargar contactos desde archivo",
    "7. Salir"
)

# Lista para almacenar los contactos
agenda = []

# Función para mostrar encabezado
def print_encabezado(titulo):
    print(f"\n{Fore.CYAN}{'-'*60}")
    print(f"{Fore.CYAN}{Style.BRIGHT}{titulo.center(60)}")
    print(f"{Fore.CYAN}{'-'*60}")

# Mostrar todos los contactos
def mostrar_contactos(lista=None):
    if lista is None:
        lista = agenda
    print_encabezado("📇 CONTACTOS REGISTRADOS")
    if not lista:
        print(Fore.YELLOW + "[!] No hay contactos registrados.")
    else:
        for i, contacto in enumerate(lista, start=1):
            print(Fore.GREEN + f"{i}. Nombre: {contacto['nombre']} | Teléfono: {contacto['telefono']} | "
                  f"Ciudad: {contacto['ciudad']} | Edad: {contacto['edad']} | Email: {contacto['email']}")

# Buscar contactos por ciudad o edad
def buscar_contactos():
    print_encabezado("🔍 BÚSQUEDA DE CONTACTOS")
    print("1. Buscar por ciudad")
    print("2. Buscar por edad mínima")
    opcion = input("Seleccione una opción de búsqueda: ").strip()

    if opcion == '1':
        ciudad = input("Ingrese la ciudad: ").strip().lower()
        encontrados = [c for c in agenda if c['ciudad'].lower() == ciudad]
        mostrar_contactos(encontrados)
    elif opcion == '2':
        try:
            edad_min = int(input("Edad mínima: ").strip())
            encontrados = [c for c in agenda if c['edad'] >= edad_min]
            mostrar_contactos(encontrados)
        except ValueError:
            print(Fore.RED + "[!] Edad inválida. Ingrese un número.")
    else:
        print(Fore.RED + "[!] Opción no válida.")

# Guardar contactos en archivo JSON
def guardar_en_archivo():
    try:
        with open("agenda_contactos.json", "w", encoding='utf-8') as f:
            json.dump(agenda, f, indent=4, ensure_ascii=False)
        print(Fore.GREEN + "[✔] Contactos guardados correctamente en 'agenda_contactos.json'.")
    except Exception as e:
        print(Fore.RED + f"[!] Error al guardar: {e}")

# Cargar contactos desde archivo JSON
def cargar_desde_archivo():
    global agenda
    try:
        with open("agenda_contactos.json", "r", encoding='utf-8') as f:
            agenda = json.load(f)
        print(Fore.GREEN + "[✔] Contactos cargados correctamente.")
    except FileNotFoundError:
        print(Fore.RED + "[!] No se encontró el archivo 'agenda_contactos.json'.")
    except Exception as e:
        print(Fore.RED + f"[!] Error al cargar: {e}")

# Bucle principal
while True:
    print_encabezado("📘 MENÚ DE AGENDA")
    for opcion in menu_options:
        print(Fore.BLUE + opcion)

    seleccion = input(Fore.CYAN + "\nSeleccione una opción (1-7): ")

    if seleccion == '1':
        print_encabezado("📝 REGISTRO DE CONTACTO")

        nombre = input("Nombre: ").strip()
        telefono = input("Teléfono: ").strip()
        ciudad = input("Ciudad: ").strip()

        while True:
            try:
                edad = int(input("Edad: ").strip())
                if edad <= 0 or edad > 120:
                    raise ValueError
                break
            except ValueError:
                print(Fore.RED + "[!] Edad inválida. Intente nuevamente.")

        email = input("Email: ").strip()

        contacto = {
            "nombres": nombre,
            "telefono": telefono,
            "ciudad": ciudad,
            "edad": edad,
            "email": email
        }

        agenda.append(contacto)
        print(Fore.GREEN + "[✔] Contacto registrado exitosamente.")

    elif seleccion == '2':
        mostrar_contactos()

    elif seleccion == '3':
        print_encabezado("❌ ELIMINAR CONTACTO")
        nombre_eliminar = input("Nombre del contacto a eliminar: ").strip()
        try:
            encontrado = False
            for contacto in agenda:
                if contacto['nombre'].lower() == nombre_eliminar.lower():
                    agenda.remove(contacto)
                    print(Fore.GREEN + f"[✔] Contacto '{nombre_eliminar}' eliminado correctamente.")
                    encontrado = True
                    break
            if not encontrado:
                raise ValueError
        except ValueError:
            print(Fore.RED + "[!] Contacto no encontrado.")

    elif seleccion == '4':
        buscar_contactos()

    elif seleccion == '5':
        guardar_en_archivo()

    elif seleccion == '6':
        cargar_desde_archivo()

    elif seleccion == '7':
        print_encabezado("👋 SALIENDO DEL SISTEMA")
        print(Fore.MAGENTA + "Gracias por usar la Agenda. ¡Hasta pronto!")
        break

    else:
        print(Fore.RED + "[!] Opción inválida. Intente de nuevo.")

    input(Fore.YELLOW + "\nPresiona Enter para continuar...")
