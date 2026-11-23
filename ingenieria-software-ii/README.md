# Intervención del componente de autenticación

Esta carpeta contiene la continuación del proyecto para Ingeniería de Software II.

## Objetivo

Separar la forma de validar credenciales mediante el patrón Strategy. El servicio de autenticación recibe una estrategia por dependencia, en lugar de contener directamente cada método de acceso.

## Contenido

- `autenticacion_estrategia.py`: código de referencia.
- `test_autenticacion_estrategia.py`: pruebas unitarias.
- `diagrama-secuencia-autenticacion.puml`: flujo propuesto.
- `analisis-y-diseno.md`: análisis, justificación, alcance y decisiones de seguridad.

## Estado

El proyecto original sigue siendo principalmente documental. Esta carpeta incorpora un ejemplo ejecutable de la lógica de autenticación y pruebas unitarias, pero no una API desplegada ni una conexión con base de datos real. El almacén de sesiones es solo demostrativo y debe reemplazarse antes de producción.

## Pruebas

Ejecutar desde esta carpeta:

```bash
python -m unittest -v
```
