# 🗂️ Agenda de Contactos - Mini Sistema Interactivo

# 📌 Tupla de opciones del menú
menu_options = (
    "1. Registrar nuevo contacto",
    "2. Ver todos los contactos",
    "3. Eliminar un contacto",
    "4. Salir"
)

# 📋 Lista para almacenar los contactos
agenda = []

# ✅ Función para mostrar todos los contactos
def mostrar_contactos():
    if not agenda:
        print("\n[!] No hay contactos registrados.")
        return
    print("\n📇 Contactos registrados:")
    for contacto in agenda:
        print(f"Nombre: {contacto['nombre']} | Teléfono: {contacto['telefono']} | "
              f"Ciudad: {contacto['ciudad']} | Edad: {contacto['edad']} | Email: {contacto['email']}")

# 🔁 Bucle principal
while True:
    print("\n--- MENÚ DE AGENDA ---")
    for opcion in menu_options:
        print(opcion)

    seleccion = input("\nSeleccione una opción: ")

    if seleccion == '1':
        print("\n📌 Registro de nuevo contacto")

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
                print("[!] Error: Edad inválida. Ingrese un número entero válido (1-120).")

        email = input("Email: ").strip()

        # Simulación de lista anidada: podemos almacenar múltiples teléfonos
        contacto = {
            "nombre": nombre,
            "telefono": telefono,
            "ciudad": ciudad,
            "edad": edad,
            "email": email
        }

        agenda.append(contacto)
        print("[+] Contacto registrado exitosamente.")

    elif seleccion == '2':
        mostrar_contactos()

    elif seleccion == '3':
        nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ").strip()
        encontrado = False

        try:
            for contacto in agenda:
                if contacto['nombre'].lower() == nombre_eliminar.lower():
                    agenda.remove(contacto)
                    print(f"[+] Contacto '{nombre_eliminar}' eliminado correctamente.")
                    encontrado = True
                    break
            if not encontrado:
                raise ValueError("[!] Contacto no encontrado.")
        except ValueError as e:
            print(e)

    elif seleccion == '4':
        print("👋 Saliendo del sistema. ¡Hasta luego!")
        break

    else:
        print("[!] Opción inválida. Por favor, seleccione una opción válida del 1 al 4.")
