from colorama import init, Fore, Style
init(autoreset=True)

# Tupla de opciones del menú
menu_options = (
    "1. Registrar nuevo contacto",
    "2. Ver todos los contactos",
    "3. Eliminar un contacto",
    "4. Salir"
)

# Lista para almacenar los contactos
agenda = []

# Función para mostrar encabezado con estilo
def print_encabezado(titulo):
    print(f"\n{Fore.CYAN}{'-'*50}")
    print(f"{Fore.CYAN}{Style.BRIGHT}{titulo.center(50)}")
    print(f"{Fore.CYAN}{'-'*50}")

# Función para mostrar todos los contactos
def mostrar_contactos():
    print_encabezado("📇 CONTACTOS REGISTRADOS")
    if not agenda:
        print(Fore.YELLOW + "[!] No hay contactos registrados.")
    else:
        for i, contacto in enumerate(agenda, start=1):
            print(Fore.GREEN + f"{i}. Nombre: {contacto['nombre']} | Teléfono: {contacto['telefono']} | "
                  f"Ciudad: {contacto['ciudad']} | Edad: {contacto['edad']} | Email: {contacto['email']}")

# Bucle principal
while True:
    print_encabezado("📘 MENÚ DE AGENDA")
    for opcion in menu_options:
        print(Fore.BLUE + opcion)

    seleccion = input(Fore.CYAN + "\nSeleccione una opción (1-4): ")

    if seleccion == '1':
        print_encabezado("📝 REGISTRO DE CONTACTO")

        nombre = input("Nombre: ").strip()
        telefono = input("Teléfono: ").strip()
        ciudad = input("Ciudad: ").strip()

        # Validación de edad
        while True:
            edad_input = input("Edad: ").strip()
            try:
                edad = int(edad_input)
                if edad <= 0 or edad > 120:
                    raise ValueError
                break
            except ValueError:
                print(Fore.RED + "[!] Error: Edad inválida. Ingrese un número entero válido (1-120).")

        email = input("Email: ").strip()

        contacto = {
            "nombre": nombre,
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
        nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ").strip()
        encontrado = False

        try:
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
        print_encabezado("👋 SALIENDO DEL SISTEMA")
        print(Fore.MAGENTA + "Gracias por usar la Agenda. ¡Hasta pronto!")
        break

    else:
        print(Fore.RED + "[!] Opción inválida. Por favor, seleccione una opción del 1 al 4.")

    input(Fore.YELLOW + "\nPresiona Enter para continuar...")
