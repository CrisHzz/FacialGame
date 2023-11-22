# Juego de Supervivencia

¡Bienvenido al Juego de Supervivencia, una experiencia única donde tu habilidad para controlar el destino del jugador y el monstruo se encuentra en tus movimientos faciales! 😮

## Descripción del Juego

### Mapa del Juego
El mapa del juego se representa mediante una matriz NxN, donde el jugador y el monstruo se moverán en busca de comida y armas.

### Jugador y Monstruo
- El jugador aparece en una posición aleatoria con 10 puntos de vida y un inventario vacío.
- Un monstruo con 100 puntos de vida se mueve aleatoriamente, amenazando al jugador si se cruzan en el mismo punto.

### Elementos en el Mapa
- **Comidas:** Proporcionan al jugador 10 puntos de vida cada vez que se consumen.
- **Armas:** Se encuentran dispersas por el mapa y pueden ser recogidas para atacar al monstruo.

### Turnos del Juego
El juego se desarrolla por turnos, donde el jugador puede realizar las siguientes acciones:

- **Moverse:** Avanzar en cualquier dirección (arriba, derecha, izquierda, abajo).
- **Comer:** Consumir comida para recuperar 10 puntos de vida.
- **Agregar a Inventario:** Recolectar armas y almacenarlas en el inventario.
- **Atacar:** Utilizar un arma del inventario para dañar al monstruo.

### Interacción mediante Movimientos Faciales
Los controles del juego se realizan a través de movimientos faciales, como mover la cabeza a la derecha, izquierda, abrir la boca, subir una ceja, etc. ¡Demuestra tus habilidades para sobrevivir!

### Dinámica del Monstruo
El monstruo se mueve aleatoriamente por el mapa. Si se cruza con el jugador, le inflige 25 puntos de daño.

### Fin del Juego
El juego termina cuando la vida del jugador o el monstruo llega a 0. ¡Demuestra tus habilidades tácticas y de expresión facial para sobrevivir!

## Detalles de Implementación
- La lógica del juego se ejecuta a través de la consola.
- Los controles se gestionan mediante movimientos faciales, proporcionando una experiencia de juego única.

# Información para desarrolladores

## Requisitos Funcionales
1. **Movimiento del Jugador:**
   - El jugador puede moverse en las direcciones: arriba, derecha, izquierda, abajo.
   
2. **Interacción con Elementos en el Mapa:**
   - El jugador puede consumir comida para aumentar su vida.
   - El jugador puede recoger armas y agregarlas a su inventario.

3. **Turnos del Juego:**
   - El juego avanza por turnos, alternando entre el jugador y el monstruo.
   - En cada turno del jugador, se deben realizar acciones como moverse, comer, agregar a inventario o atacar.

4. **Ataque y Daño:**
   - El jugador puede atacar al monstruo utilizando armas del inventario.
   - El monstruo ataca al jugador al moverse sobre su posición, infligiendo 25 puntos de daño.

5. **Fin del Juego:**
   - El juego termina cuando la vida del jugador o del monstruo llega a 0.

¡Prepárate para una experiencia de juego emocionante y llena de acción! 😮🎮