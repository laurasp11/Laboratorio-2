"""Demostración de paso de parámetros (Req. 8) y alcance de variables (Req. 9)."""


def sumar_un_anio(edad):
    """Recibe un número (tipo inmutable): trabaja con una COPIA del dato."""
    edad = edad + 1
    return edad


def agregar_elemento(lista, elemento):
    """Recibe una lista (tipo mutable): modifica la lista ORIGINAL."""
    lista.append(elemento)


def probar_paso_de_parametros():
    """Req. 8: muestra que un número se copia y una lista se modifica al pasarlos a una función."""
    edad = 20
    print(f"Antes de llamar a la función   : edad = {edad}")
    nueva_edad = sumar_un_anio(edad)
    print(f"La función devolvió            : {nueva_edad}")
    print(f"Después de llamar a la función : edad = {edad}   (el original no cambió)")

    solicitudes = ["S1"]
    print(f"\nAntes de llamar a la función   : solicitudes = {solicitudes}")
    agregar_elemento(solicitudes, "S2")
    print(f"Después de llamar a la función : solicitudes = {solicitudes}   (la lista original sí cambió)")


def contar_solicitudes(solicitudes):
    """'cantidad' es una variable LOCAL: solo existe mientras corre esta función."""
    cantidad = len(solicitudes)
    return cantidad


def probar_alcance():
    """Req. 9: muestra que una variable local no existe fuera de su función."""
    solicitudes = ["S1", "S2", "S3"]  # variable local de probar_alcance (hace de "programa principal")
    total = contar_solicitudes(solicitudes)
    print(f"Solicitudes registradas: {total}")
    try:
        print(cantidad)  # 'cantidad' NO existe aquí: pertenece a contar_solicitudes
    except NameError:
        print("cantidad no existe fuera de contar_solicitudes (alcance local)")    


if __name__ == "__main__":
    probar_paso_de_parametros()
    print("\n--- Alcance de variables ---")
    probar_alcance()