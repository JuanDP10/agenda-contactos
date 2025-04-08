import json  # Módulo para trabajar con archivos JSON
import os  # Módulo para comandos del sistema
import platform  # Módulo para detectar sistema operativo
from colorama import init, Fore, Style  # Módulo para colorear texto en la terminal
import unicodedata  # Módulo para normalizar texto (quitar tildes)

init(autoreset=True)  # Inicializa colorama para que los colores se reinicien automáticamente después de cada impresión

# Función para limpiar la pantalla según el sistema operativo
# Se usa para mantener la interfaz limpia y ordenada entre acciones
def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Función para eliminar tildes y otros caracteres diacríticos
def normalizar_texto(texto):
    # Normaliza texto a forma NFD y elimina caracteres diacríticos
    return ''.join(c for c in unicodedata.normalize('NFD', texto)
                  if unicodedata.category(c) != 'Mn').lower()

# Tupla con las opciones del menú principal. Los emojis hacen que se vea más visual y amigable.
menu_options = (
    "1. Registrar nuevo contacto \U0001F4DD",
    "2. Ver todos los contactos \U0001F4C7",
    "3. Eliminar un contacto \u274C",
    "4. Buscar contactos \U0001F50D",
    "5. Guardar contactos en archivo \U0001F4BE",
    "6. Cargar contactos desde archivo \U0001F4C2",
    "7. Salir \U0001F6AA"
)

agenda = []  # Lista vacía que almacenará los diccionarios con los datos de cada contacto

# Función que imprime un título bonito con líneas y colores
def print_encabezado(titulo):
    print(f"\n{Fore.CYAN}{'-'*60}")
    print(f"{Fore.CYAN}{Style.BRIGHT}{titulo.center(60)}")
    print(f"{Fore.CYAN}{'-'*60}")

# Función para solicitar un campo obligatorio al usuario
def solicitar_campo(mensaje, validacion=None):
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print(Fore.RED + "[!] Este campo es obligatorio. No puede estar vacío.")
            continue
        
        if validacion and not validacion(valor):
            continue
            
        return valor

# Función para validar edad
def validar_edad(valor):
    try:
        edad = int(valor)
        if edad <= 0 or edad > 120:
            print(Fore.RED + "[!] La edad debe estar entre 1 y 120 años.")
            return False
        return True
    except ValueError:
        print(Fore.RED + "[!] La edad debe ser un número entero.")
        return False

# Función para validar email de forma básica
def validar_email(valor):
    if '@' not in valor or '.' not in valor:
        print(Fore.RED + "[!] Email inválido. Debe contener '@' y '.'")
        return False
    return True

# Función para mostrar contactos (todos o los que se pasen por parámetro)
def mostrar_contactos(lista=None):
    if lista is None:
        lista = agenda  # Si no se pasa una lista, se usa la agenda completa
    print_encabezado("\U0001F4C7 CONTACTOS REGISTRADOS")
    if not lista:
        print(Fore.YELLOW + "[!] No hay contactos registrados.")
    else:
        for i, contacto in enumerate(lista, start=1):  # Recorre la lista e imprime cada contacto con índice
            print(Fore.GREEN + f"{i}. Nombres: {contacto['nombre']} | Apellidos: {contacto['apellido']} | Teléfono: {contacto['telefono']} | "
                  f"Ciudad: {contacto['ciudad']} | Edad: {contacto['edad']} | Email: {contacto['email']}")

# Función para buscar contactos por ciudad o edad mínima
def buscar_contactos():
    while True:
        limpiar_pantalla()
        print_encabezado("\U0001F50D BÚSQUEDA DE CONTACTOS")
        print("1. Buscar por ciudad \U0001F3D9️")
        print("2. Buscar por edad mínima \U0001F464")
        print("3. Buscar por nombre o apellido \U0001F464")
        print("0. Volver al menú principal \U0001F519")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            ciudad = solicitar_campo("Ingrese la ciudad: ")
            ciudad_normalizada = normalizar_texto(ciudad)
            encontrados = [c for c in agenda if normalizar_texto(c['ciudad']) == ciudad_normalizada]  # Filtra contactos por ciudad
            mostrar_contactos(encontrados)
        elif opcion == '2':
            edad_min = solicitar_campo("Edad mínima: ", validar_edad)
            encontrados = [c for c in agenda if c['edad'] >= int(edad_min)]  # Filtra por edad mínima
            mostrar_contactos(encontrados)
        elif opcion == '3':
            texto_busqueda = solicitar_campo("Ingrese nombre o apellido: ")
            texto_normalizado = normalizar_texto(texto_busqueda)
            encontrados = [c for c in agenda if texto_normalizado in normalizar_texto(c['nombre']) or 
                           texto_normalizado in normalizar_texto(c['apellido'])]
            mostrar_contactos(encontrados)
        elif opcion == '0':
            return  # Regresa al menú principal
        else:
            print(Fore.RED + "[!] Opción no válida.")
        input(Fore.YELLOW + "\nPresiona Enter para continuar...")

# Función que guarda la lista de contactos en un archivo JSON
def guardar_en_archivo():
    try:
        with open("agenda_contactos.json", "w", encoding='utf-8') as f:
            json.dump(agenda, f, indent=4, ensure_ascii=False)  # Guarda con indentación y caracteres especiales
        print(Fore.GREEN + "[✔] Contactos guardados correctamente.")
    except Exception as e:
        print(Fore.RED + f"[!] Error al guardar: {e}")

# Función que carga contactos desde un archivo JSON
def cargar_desde_archivo():
    global agenda
    try:
        with open("agenda_contactos.json", "r", encoding='utf-8') as f:
            agenda = json.load(f)  # Sobrescribe la agenda con los datos del archivo
        print(Fore.GREEN + "[✔] Contactos cargados correctamente.")
        
        # Compatibilidad con registros anteriores que no tengan nombre y apellido por separado
        for contacto in agenda:
            if 'apellido' not in contacto:
                nombres = contacto['nombre'].split(' ', 1)
                contacto['nombre'] = nombres[0]
                contacto['apellido'] = nombres[1] if len(nombres) > 1 else ""
                
    except FileNotFoundError:
        print(Fore.RED + "[!] No se encontró el archivo.")
    except Exception as e:
        print(Fore.RED + f"[!] Error al cargar: {e}")

# Bucle principal del sistema (menú interactivo)
while True:
    limpiar_pantalla()
    print_encabezado("\U0001F4D8 MENÚ DE AGENDA")
    for opcion in menu_options:
        print(Fore.BLUE + opcion)  # Muestra todas las opciones del menú

    seleccion = input(Fore.CYAN + "\nSeleccione una opción (1-7): ")

    if seleccion == '1':
        while True:
            limpiar_pantalla()
            print_encabezado("\U0001F4DD REGISTRO DE CONTACTO")
            print("1. Ingresar un nuevo contacto")
            print("0. Cancelar y volver al menú principal")
            opcion_registro = input("Seleccione una opción: ").strip()

            if opcion_registro == '0':
                print(Fore.YELLOW + "[i] Registro cancelado. Volviendo al menú principal.")
                break  # Salimos de esta sección y volvemos al menú principal
            
            elif opcion_registro == '1':
                # Solicitar datos obligatorios
                nombre = solicitar_campo("Nombre: ")
                apellido = solicitar_campo("Apellido: ")
                telefono = solicitar_campo("Teléfono: ")
                ciudad = solicitar_campo("Ciudad: ")
                edad = solicitar_campo("Edad: ", validar_edad)
                email = solicitar_campo("Email: ", validar_email)

                # Diccionario con la información del contacto
                contacto = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "telefono": telefono,
                    "ciudad": ciudad,
                    "edad": int(edad),  # Convertir a entero ya que fue validado previamente
                    "email": email
                }

                agenda.append(contacto)  # Agrega el contacto a la agenda
                print(Fore.GREEN + "[✔] Contacto registrado exitosamente.")

    elif seleccion == '2':
        limpiar_pantalla() # Llama a la función para limpiar la pantalla
        mostrar_contactos()  # Llama a la función para mostrar todos los contactos

    elif seleccion == '3':
        limpiar_pantalla()
        print_encabezado("\u274C ELIMINAR CONTACTO")
        if not agenda:
            print(Fore.YELLOW + "[!] No hay contactos registrados.")
            input(Fore.CYAN + "\nPresione Enter para volver al menú...")
            continue
        else:
            busqueda = solicitar_campo("Nombre del contacto a eliminar (0 para cancelar): ")
            if busqueda.strip() == '0':
                print(Fore.YELLOW + "[i] Eliminación cancelada.")
                continue  # Cancela la eliminación si el usuario ingresa '0'
            busqueda_normalizada = normalizar_texto(busqueda)
            try:
                contactos_encontrados = []
                
                # Busca el contacto ignorando tildes
                for i, contacto in enumerate(agenda):
                    nombre_completo = f"{contacto['nombre']} {contacto['apellido']}"
                    if busqueda_normalizada in normalizar_texto(nombre_completo):
                        contactos_encontrados.append((i, contacto))
                
                if not contactos_encontrados:
                    raise ValueError
                    
                # Si hay más de un contacto que coincide, mostrar opciones
                if len(contactos_encontrados) > 1:
                    print(Fore.YELLOW + "Se encontraron varios contactos:")
                    for idx, (i, contacto) in enumerate(contactos_encontrados, 1):
                        nombre_completo = f"{contacto['nombre']} {contacto['apellido']}"
                        print(f"{idx}. {nombre_completo}")
                    
                    while True:
                        try:
                            seleccion_contacto = int(input("\nSeleccione el número del contacto a eliminar (0 para cancelar): "))
                            if seleccion_contacto == 0:
                                print(Fore.YELLOW + "[i] Eliminación cancelada.")
                                break
                            elif 1 <= seleccion_contacto <= len(contactos_encontrados):
                                i, contacto = contactos_encontrados[seleccion_contacto-1]
                                nombre_completo = f"{contacto['nombre']} {contacto['apellido']}"
                                confirmar = input(f"¿Está seguro de eliminar a {nombre_completo}? (s/n): ").strip().lower()
                                if confirmar == 's':
                                    agenda.pop(i)  # Elimina el contacto
                                    print(Fore.GREEN + f"[✔] Contacto '{nombre_completo}' eliminado correctamente.")
                                else:
                                    print(Fore.YELLOW + "[i] Eliminación cancelada.")
                                break
                            else:
                                print(Fore.RED + "[!] Número inválido.")
                        except ValueError:
                            print(Fore.RED + "[!] Ingrese un número válido.")
                # Si solo hay un contacto, preguntar directamente
                elif len(contactos_encontrados) == 1:
                    i, contacto = contactos_encontrados[0]
                    nombre_completo = f"{contacto['nombre']} {contacto['apellido']}"
                    confirmar = input(f"¿Está seguro de eliminar a {nombre_completo}? (s/n): ").strip().lower()
                    if confirmar == 's':
                        agenda.pop(i)  # Elimina el contacto
                        print(Fore.GREEN + f"[✔] Contacto '{nombre_completo}' eliminado correctamente.")
                    else:
                        print(Fore.YELLOW + "[i] Eliminación cancelada.")
                        
            except ValueError:
                print(Fore.RED + "[!] Contacto no encontrado.")

    elif seleccion == '4':
        buscar_contactos()  # Llama a la función de búsqueda

    elif seleccion == '5':
        limpiar_pantalla()
        guardar_en_archivo()  # Llama a la función para guardar la agenda

    elif seleccion == '6':
        limpiar_pantalla()
        cargar_desde_archivo()  # Llama a la función para cargar la agenda

    elif seleccion == '7':
        limpiar_pantalla()
        print_encabezado("\U0001F44B SALIENDO DEL SISTEMA")
        print(Fore.MAGENTA + "Gracias por usar la Agenda. ¡Hasta pronto!")
        break  # Termina el programa

    else:
        print(Fore.RED + "[!] Opción inválida. Intente de nuevo.")

    input(Fore.YELLOW + "\nPresiona Enter para continuar...")  # Pausa entre cada acción