"""Sistema de orientación y registro de atenciones - Soporte Académico."""
import unicodedata

def registrar_solicitud(codigo, nombre, tipo, descripcion):
    """Req. 1 y 5: arma la solicitud (con su prioridad) y la devuelve."""
    solicitud = {
        "codigo": codigo.strip(),
        "nombre": nombre.strip(),
        "tipo": normalizar_texto(tipo),
        "descripcion": descripcion.strip(),
        "prioridad": asignar_prioridad(tipo),
    }
    return solicitud


def mostrar_menu():
    """Req. 4: muestra el menú principal (función sin retorno)."""
    print("\n === SOPORTE ACADÉMICO ===")
    print("1. Registrar solicitud")
    print("2. Ver solicitudes registradas")
    print("3. Salir")


def validar_codigo(codigo, longitud_minima):
    """Req. 2: True si el código no está vacío y alcanza la longitud mínima."""
    codigo_limpio = codigo.strip()
    return codigo_limpio != "" and len(codigo_limpio) >= longitud_minima


def normalizar_texto(texto):
    """Apoyo de Req. 3 y 5: minúsculas, sin espacios en los extremos y sin tildes."""
    texto_limpio = texto.strip().lower()
    descompuesto = unicodedata.normalize("NFD", texto_limpio)  # separa la letra de su tilde
    return "".join(letra for letra in descompuesto if unicodedata.category(letra) != "Mn")


def validar_tipo_consulta(tipo, tipos_validos):
    """Req. 3: True si el tipo de consulta pertenece a la lista básica."""
    tipo_normalizado = normalizar_texto(tipo)
    return tipo_normalizado in tipos_validos


def validar_texto_obligatorio(texto):
    """Req. 6: True si el texto tiene contenido (no está vacío ni solo con espacios)."""
    texto_limpio = texto.strip()
    return texto_limpio != ""


def asignar_prioridad(tipo):
    """Req. 5: devuelve "Alta", "Media" o "Baja" según el tipo de consulta."""
    tipo_normalizado = normalizar_texto(tipo)
    if tipo_normalizado in ("plataforma", "matricula"):
        prioridad = "Alta"
    elif tipo_normalizado == "pagos":
        prioridad = "Media"
    else:
        prioridad = "Baja"
    return prioridad


def mostrar_resumen(solicitud):
    """Req. 7: muestra en pantalla el resumen de una solicitud registrada."""
    print("--- Resumen de la solicitud ---")
    print(f"Código      : {solicitud['codigo']}")
    print(f"Nombre      : {solicitud['nombre']}")
    print(f"Tipo        : {solicitud['tipo']}")
    print(f"Descripción : {solicitud['descripcion']}")
    print(f"Prioridad   : {solicitud['prioridad']}")


def pedir_texto_obligatorio(mensaje):
    """Apoyo de Req. 10: pide un dato por teclado hasta que no esté vacío."""
    texto = input(mensaje)
    while not validar_texto_obligatorio(texto):
        print("  Este dato es obligatorio.")
        texto = input(mensaje)
    return texto


def capturar_solicitud(tipos_validos, longitud_minima):
    """Req. 1, 2, 3 y 6: pide los datos, los valida y devuelve la solicitud."""
    # codigo, nombre, tipo y descripcion son variables LOCALES de esta función.
    codigo = input("Código de estudiante: ")
    while not validar_codigo(codigo, longitud_minima):
        print(f"  Código inválido: no puede estar vacío y necesita al menos {longitud_minima} caracteres.")
        codigo = input("Código de estudiante: ")

    nombre = pedir_texto_obligatorio("Nombre: ")

    tipo = input(f"Tipo de consulta ({', '.join(tipos_validos)}): ")
    while not validar_tipo_consulta(tipo, tipos_validos):
        print("  Tipo de consulta no válido.")
        tipo = input(f"Tipo de consulta ({', '.join(tipos_validos)}): ")

    descripcion = pedir_texto_obligatorio("Descripción breve: ")
    return registrar_solicitud(codigo, nombre, tipo, descripcion)


def mostrar_solicitudes(solicitudes):
    """Req. 7 y 10: muestra todas las solicitudes guardadas en la lista."""
    if len(solicitudes) == 0:
        print("Aún no hay solicitudes registradas.")
    else:
        for solicitud in solicitudes:  # 'solicitud' solo existe dentro de este for
            mostrar_resumen(solicitud)
        print(f"Total de solicitudes: {len(solicitudes)}")


def main():
    """Req. 9 y 10: programa principal; guarda varias solicitudes en una lista."""
    # Variables del PROGRAMA PRINCIPAL (locales de main). Se envían a las
    # funciones por parámetro; no se usan variables globales.
    tipos_validos = ["matricula", "pagos", "constancia", "plataforma", "otro"]
    longitud_minima = 6
    solicitudes = []
    opcion = ""

    while opcion != "3":
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            solicitud = capturar_solicitud(tipos_validos, longitud_minima)
            solicitudes.append(solicitud)
            mostrar_resumen(solicitud)
        elif opcion == "2":
            mostrar_solicitudes(solicitudes)
        elif opcion == "3":
            print("Hasta pronto.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()    