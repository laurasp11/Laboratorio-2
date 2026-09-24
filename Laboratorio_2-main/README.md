  # Sistema de orientación y registro de atenciones - Soporte Académico
  Laboratorio Tema 2 - Fundamentos de Programación
  Lenguaje: Python
  Integrante: Vladimir
  
  ## Cómo ejecutar

- `python soporte_academico.py`: programa principal (menú)
- `python pruebas.py`: casos de prueba de la Tabla 3
- `python demo_parametros.py`: paso de parámetros y alcance de variables

## Requerimientos atendidos por función

| Req. | Descripción | Función(es) / archivo |
|------|-------------|------------------------|
| 1 | Registrar datos básicos de la solicitud | `registrar_solicitud`, `capturar_solicitud` |
| 2 | Validar código (no vacío y longitud mínima) | `validar_codigo` |
| 3 | Validar tipo de consulta | `validar_tipo_consulta`, `normalizar_texto` |
| 4 | Menú principal (sin retorno) | `mostrar_menu` |
| 5 | Prioridad de atención (con retorno) | `asignar_prioridad` |
| 6 | Validar texto obligatorio (con retorno) | `validar_texto_obligatorio`, `pedir_texto_obligatorio` |
| 7 | Resumen de la solicitud | `mostrar_resumen`, `mostrar_solicitudes` |
| 8 | Paso de parámetros sin globales innecesarias | Todas las funciones; `demo_parametros.py` (`sumar_un_anio`, `agregar_elemento`, `probar_paso_de_parametros`) |
| 9 | Alcance de variables | Comentarios en `main` y `capturar_solicitud`; `demo_parametros.py` (`contar_solicitudes`, `probar_alcance`) |
| 10 | Al menos tres solicitudes por ejecución | `main` (lista `solicitudes`), `mostrar_solicitudes` |
| 11 | Al menos cinco pruebas | `pruebas.py` (`ejecutar_pruebas`, `mostrar_resultado`) |
| 12 | Documentación por función | Docstrings + esta tabla |