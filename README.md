# 📘 Agenda de Contactos 📞

![Licencia](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.6+-yellow.svg)
![Versión](https://img.shields.io/badge/versión-1.0.0-green.svg)

## 📋 Tabla de Contenidos

- [🌟 Descripción](#-descripción)
- [✨ Características](#-características)
- [🚀 Instalación](#-instalación)
- [🔧 Requisitos](#-requisitos)
- [💻 Uso](#-uso)
- [📊 Estructura del Proyecto](#-estructura-del-proyecto)
- [🛠️ Funcionalidades Detalladas](#️-funcionalidades-detalladas)
- [🗃️ Estructura de Datos](#️-estructura-de-datos)
- [📝 Ejemplo de JSON](#-ejemplo-de-json)
- [⚙️ Personalización](#️-personalización)
- [❓ Preguntas Frecuentes](#-preguntas-frecuentes)
- [📜 Licencia](#-licencia)

## 🌟 Descripción

**Agenda de Contactos** es una aplicación de consola desarrollada en Python que permite gestionar contactos personales de manera eficiente. La aplicación está diseñada con una interfaz amigable y colorida usando el módulo `colorama`, facilitando la gestión de información como nombres, apellidos, teléfonos, ciudades, edades y correos electrónicos.

## ✨ Características

- 📝 **Registro de contactos** con validación de campos obligatorios
- 🔍 **Búsqueda avanzada** por nombre, ciudad o edad
- 🔤 **Búsqueda insensible a tildes** para una mejor experiencia en español
- 🗑️ **Eliminación de contactos** con confirmación
- 💾 **Guardado y carga** de contactos mediante archivos JSON
- 🎨 **Interfaz colorida** para una mejor experiencia de usuario
- 🔒 **Validación de datos** para garantizar la integridad de la información
- 🖥️ **Archivo ejecutable** disponible para usuarios sin Python instalado

## 🚀 Instalación

### Opción 1: Ejecutable (Windows)

1. Descarga el archivo `agenda_contactos.exe`
2. Ejecuta la aplicación haciendo doble clic en el archivo descargado

### Opción 2: Código Fuente

1. Clona este repositorio:
   ```bash
   git clone https://github.com/usuario/agenda-contactos.git
   cd agenda-contactos
   ```

2. Instala las dependencias:
   ```bash
   pip install colorama
   ```

3. Ejecuta la aplicación:
   ```bash
   python agenda_contactos.py
   ```

## 🔧 Requisitos

Para el ejecutable:
- Sistema operativo Windows

Para el código fuente:
- Python 3.6 o superior
- Módulo colorama (`pip install colorama`)

## 💻 Uso

Al ejecutar la aplicación, se mostrará un menú interactivo con las siguientes opciones:

```
------------------------------------------------------------
                     MENÚ DE AGENDA
------------------------------------------------------------
1. Registrar nuevo contacto 📝
2. Ver todos los contactos 📇
3. Eliminar un contacto ❌
4. Buscar contactos 🔍
5. Guardar contactos en archivo 💾
6. Cargar contactos desde archivo 📂
7. Salir 🚪
```

Selecciona una opción ingresando el número correspondiente y sigue las instrucciones en pantalla.

## 📊 Estructura del Proyecto

```
agenda-contactos/
│
├── agenda_contactos.py      # Archivo principal del programa
├── agenda_contactos.exe     # Ejecutable para Windows
├── agenda_contactos.json    # Archivo donde se guardan los contactos (generado automáticamente)
├── LICENSE                  # Licencia
└── README.md                # Este archivo
```

## 🛠️ Funcionalidades Detalladas

### 1. Registrar Nuevo Contacto 📝

Permite agregar un nuevo contacto a la agenda con la siguiente información:
- Nombre (obligatorio)
- Apellido (obligatorio)
- Teléfono (obligatorio)
- Ciudad (obligatorio)
- Edad (obligatorio, entre 1 y 120 años)
- Email (obligatorio, debe contener '@' y '.')

Ejemplo:
```
REGISTRO DE CONTACTO
--------------------
Nombre: Juan Diego
Apellido: Pinilla
Teléfono: 3156196336
Ciudad: Cali
Edad: 21
Email: juan@gmail.com

[✔] Contacto registrado exitosamente.
```

### 2. Ver Todos los Contactos 📇

Muestra una lista completa de todos los contactos registrados en la agenda con sus detalles.

### 3. Eliminar un Contacto ❌

Permite eliminar un contacto buscándolo por su nombre o apellido. La búsqueda es insensible a mayúsculas/minúsculas y tildes.

Si se encuentran varios contactos que coinciden con el criterio de búsqueda, se mostrará una lista numerada para que selecciones el contacto específico a eliminar.

### 4. Buscar Contactos 🔍

Ofrece tres opciones de búsqueda:
- Buscar por ciudad
- Buscar por edad mínima
- Buscar por nombre o apellido

Todas las búsquedas son insensibles a mayúsculas/minúsculas y tildes.

### 5. Guardar Contactos en Archivo 💾

Guarda la agenda completa en un archivo JSON llamado `agenda_contactos.json`.

### 6. Cargar Contactos desde Archivo 📂

Carga los contactos desde el archivo `agenda_contactos.json`. Si el archivo contiene contactos en formato antiguo (sin separación de nombre y apellido), los adapta automáticamente al nuevo formato.

## 🗃️ Estructura de Datos

Cada contacto se almacena como un diccionario con los siguientes campos:

```python
{
    "nombre": "Juan Diego",
    "apellido": "Pinilla",
    "telefono": "3156196336",
    "ciudad": "Cali",
    "edad": 21,
    "email": "juan@gmail.com"
}
```

## 📝 Ejemplo de JSON

```json
[
    {
        "nombre": "Juan Diego",
        "apellido": "Pinilla",
        "telefono": "3156196336",
        "ciudad": "Cali",
        "edad": 21,
        "email": "juan@gmail.com"
    },
    {
        "nombre": "Carlos",
        "apellido": "Méndez",
        "telefono": "3104457890",
        "ciudad": "Medellín",
        "edad": 35,
        "email": "carlos.mendez@correo.com"
    }
]
```

## ⚙️ Personalización

### Cambiar Colores

El programa utiliza el módulo `colorama` para mostrar texto con color. Puedes personalizar los colores modificando las constantes `Fore` en el código:

```python
# Ejemplo para cambiar el color de los títulos
print(f"{Fore.MAGENTA}{'-'*60}")  # Cambia de CYAN a MAGENTA
```

Colores disponibles: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE

### Agregar Nuevos Campos

Para agregar nuevos campos a cada contacto, debes:

1. Modificar la función de registro para solicitar el nuevo campo
2. Actualizar la estructura del diccionario de contacto
3. Modificar la función `mostrar_contactos` para incluir el nuevo campo en la visualización

## ❓ Preguntas Frecuentes

### ¿Cómo soluciono el problema "No se encontró el archivo" al cargar contactos?

Este error ocurre cuando intentas cargar contactos pero el archivo `agenda_contactos.json` no existe. Primero debes registrar algunos contactos y guardarlos con la opción 5 antes de intentar cargarlos.

### ¿Cómo busco contactos con tildes?

No te preocupes por las tildes. La aplicación está diseñada para ignorar tildes en las búsquedas. Por ejemplo, si buscas "Mendez" encontrará contactos con "Méndez".

### ¿Hay un límite de contactos que puedo guardar?

No hay un límite explícito en el número de contactos que puedes guardar. El límite dependerá de la memoria disponible en tu sistema.

### ¿Por qué usar el ejecutable en lugar del código Python?

El ejecutable (.exe) es conveniente si no tienes Python instalado en tu sistema o prefieres una solución "portátil" que no requiera instalación. Sin embargo, el código fuente te permite personalizar y modificar la aplicación según tus necesidades.

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

⌨️ con ❤️ por [Juan Diego Pinilla](https://github.com/JuanDP10) 😊
