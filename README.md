# Despliegue de Infraestructura Helpdesk Segura (LAMP + osTicket)

## Descripción del Proyecto
Instalación, configuración y securización de un sistema de ticketing (osTicket) sobre una pila LAMP en un entorno Linux (WSL2), diseñado para simular el enrutamiento de incidentes en un Centro de Operaciones de Seguridad (SOC).

## Tecnologías Utilizadas
*   **SO:** Linux Ubuntu (WSL2)
*   **Servidor Web:** Apache2
*   **Base de Datos:** MySQL
*   **Lenguaje:** PHP 8.x
*   **Aplicación:** osTicket v1.18.1

## Hitos de Seguridad y Configuración
1.  **Aislamiento de Base de Datos:** Implementación del Principio de Mínimo Privilegio. Creación de una BD dedicada gestionada por un usuario exclusivo, evitando el uso del superusuario `root`.
2.  **Securización Post-Instalación:** 
    *   Eliminación del directorio de instalación (`setup/`) para evitar reconfiguraciones no autorizadas.
    *   Restricción de permisos (`chmod 0644`) en el archivo crítico de configuración (`ost-config.php`).
3.  **Lógica de Negocio y Triage:** Configuración de Departamentos y *Help Topics* para enrutar automáticamente las incidencias de los usuarios al equipo técnico correspondiente.
4.  **Control de Acceso (RBAC):** Configuración de permisos de "Need to Know" aislando la visibilidad de los tickets según el departamento del técnico.# Repositorio de Aprendizaje IT

Este es mi repositorio personal para documentar mi entrenamiento desde cero, mi configuración de WSL2 y mi camino hacia ciberseguridad (Blue Team).
