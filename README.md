Juego de Triqui en Python

Aplicación gráfica desarrollada en Python que implementa el clásico juego de Triqui (Tres en Raya) mediante una interfaz interactiva construida con Tkinter.

El sistema permite la participación de dos jugadores, detecta automáticamente victorias y empates, y permite reiniciar la partida.


Funcionalidades

- Juego interactivo para dos jugadores
- Detección automática de ganador
- Detección de empate
- Reinicio automático del tablero
- Interfaz gráfica amigable
- Cambio visual de turnos
- Actualización dinámica del estado del juego

Tecnologías utilizadas

- Python
- Tkinter
- MessageBox
- Programación orientada a eventos
- Lógica de matrices



Estructura del proyecto

```text
juego_triqui.py
README.md
```



Funcionamiento del sistema

El programa:

1. Crea una ventana gráfica
2. Genera un tablero de 3x3
3. Permite turnos alternados entre jugadores
4. Verifica condiciones de victoria
5. Detecta empates
6. Permite reiniciar la partida



Reglas del juego

Dos jugadores alternan turnos:

- Jugador **X**
- Jugador **O**

Gana quien complete:

- Una fila
- Una columna
- Una diagonal

Si se llenan todos los espacios sin ganador, el resultado es empate.


Interfaz gráfica

Incluye:

- Tablero interactivo
- Cambio visual de casillas
- Mensajes emergentes
- Botón de reinicio



Cómo ejecutar

Ejecutar programa

```bash
python juego_triqui.py
```



Conceptos aplicados

Durante este proyecto se aplicaron:

- Interfaces gráficas con Tkinter
- Manejo de eventos
- Validación lógica
- Gestión de estados
- Programación interactiva
- Control de flujo



Ejemplo de uso

```text
Jugador X selecciona casilla
Jugador O selecciona casilla
El sistema verifica ganador
Se muestra resultado
Puede reiniciarse la partida
```



Objetivo del proyecto

Fortalecer habilidades en desarrollo de interfaces gráficas y lógica de programación mediante la implementación de un juego clásico interactivo.



Aprendizajes obtenidos

Este proyecto permitió reforzar:

- Desarrollo con Tkinter
- Diseño de interfaces
- Validación de condiciones
- Manejo de estados globales
- Programación de juegos básicos

Autor

Nicolas

Desarrollador en formación enfocado en Python, desarrollo de software y construcción de proyectos interactivos.
