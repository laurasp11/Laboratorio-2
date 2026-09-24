"""Pruebas de ejecución (Req. 11): muestran esperado vs. obtenido para la Tabla 3."""
import soporte_academico as sa


def mostrar_resultado(caso, esperado, obtenido):
    """Imprime una fila de la Tabla 3."""
    cumple = "SÍ" if esperado == obtenido else "NO"
    print(f"{caso:<22} | esperado: {str(esperado):<16} | obtenido: {str(obtenido):<16} | cumple: {cumple}")


def ejecutar_pruebas():
    """Req. 11: ejecuta los casos de prueba (los 5 obligatorios + 1 extra)."""
    tipos_validos = ["matricula", "pagos", "constancia", "plataforma", "otro"]
    longitud_minima = 6

    # 1. Datos válidos
    solicitud = sa.registrar_solicitud("U2024001", "Estudiante Prueba", "pagos", "Cobro duplicado en mi cuota")
    datos_ok = (
        sa.validar_codigo(solicitud["codigo"], longitud_minima)
        and sa.validar_texto_obligatorio(solicitud["nombre"])
        and sa.validar_tipo_consulta(solicitud["tipo"], tipos_validos)
        and sa.validar_texto_obligatorio(solicitud["descripcion"])
    )
    mostrar_resultado("Datos válidos", (True, "Media"), (datos_ok, solicitud["prioridad"]))

    # 2. Código vacío (y una variante solo con espacios)
    mostrar_resultado("Código vacío", False, sa.validar_codigo("", longitud_minima))
    mostrar_resultado("Código solo espacios", False, sa.validar_codigo("      ", longitud_minima))

    # 3. Tipo de consulta incorrecto
    mostrar_resultado("Tipo incorrecto", False, sa.validar_tipo_consulta("deportes", tipos_validos))

    # 4. Prioridad alta
    mostrar_resultado("Prioridad alta", "Alta", sa.asignar_prioridad("plataforma"))

    # 5. Prioridad baja
    mostrar_resultado("Prioridad baja", "Baja", sa.asignar_prioridad("constancia"))


if __name__ == "__main__":
    ejecutar_pruebas()