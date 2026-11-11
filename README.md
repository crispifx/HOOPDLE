# 🏀 HOOPDLE

**Juegos de trivia, ingenio y memoria para fanáticos de la NBA.**
Sitio web estático: un solo archivo `index.html`, sin servidor ni base de datos.

---

## Historia

HOOPDLE nació de una idea simple: hacer para la NBA lo que *Fútbol 11* hace para el fútbol, una app con muchos juegos cortos y adictivos para medir cuánto sabés.

1. **Cancha 11 (v1).** Primer prototipo con 5 juegos: Draft del Quinteto, ¿Quién es?, Más o menos, Ordená por puntos y Trivia. Datos cargados a mano.
2. **Datos reales (v2).** Se integró la librería [`nba_api`](https://github.com/swar/nba_api): 30 franquicias (ciudad, estado, año de fundación, sigla) y más de 5.000 jugadores históricos con su estado activo/retirado. Nacieron Wordle NBA, Ahorcado, Franquicias, Más antigua, ¿Sigue activo? y Memoria.
3. **HOOPDLE (v3).** Cambio de nombre y rediseño completo con estética de tablero deportivo: papel crema, tipografía condensada, camisetas y pelotas dibujadas en SVG. Se sumaron **cuentas, XP, niveles, rachas e insignias**.
4. **Fotos y logos (v4).** Un script (`hoopdle_fotos.py`) descarga las imágenes oficiales y las incrusta en el juego (544 jugadores y 30 logos).
5. **Pack de minijuegos (v5).** Llegan NBA Bingo, Bingo Histórico, NBA5, NBA5 Retro, NBA Impostor, NBA Grid, NBA Top 10, NBA Pirámide, NBA Link y Verdadero o Falso. En total, **21 modos**.

---

## Funcionalidad

### Cuenta, XP y rachas
- **Crear cuenta** con apodo, número y color de camiseta. Se pueden tener varias cuentas en el mismo dispositivo.
- **XP y niveles:** cada partida da XP (más si ganás y si tenés racha). Cada 120 XP subís de nivel.
- **Racha de victorias:** cuántas partidas seguidas ganaste, entre cualquier juego. Una derrota la reinicia.
- **Racha diaria:** días consecutivos en los que jugaste, con calendario de los últimos 7 días.
- **Juego del día:** un modo destacado cada día que da **XP doble**.
- **Insignias:** Debut, En llamas (5 victorias seguidas), Imparable (10), Fiel (3 días), Semana perfecta (7 días), Todoterreno (todos los modos), Veterano (50 partidas) y Estrella (nivel 5).
- **Perfil** con estadísticas, efectividad y récords por juego.

### Los 21 juegos

| # | Juego | Cómo se juega |
|---|-------|---------------|
| 1 | **Draft del Quinteto** | Elegí un Base, Escolta, Alero, Ala-pívot y Pívot entre 4 opciones. Suma talento + química por compañeros del mismo equipo. |
| 2 | **¿Quién es?** | Adiviná al jugador con pistas que se revelan de a una. Menos pistas, más puntos. |
| 3 | **Más o menos** | Elegí quién tiene más puntos, anillos o valoración. Racha hasta el primer error. |
| 4 | **Ordená por puntos** | Tocá 4 jugadores de mayor a menor promedio de carrera. |
| 5 | **Trivia NBA** | 12 preguntas de cultura NBA. |
| 6 | **Wordle NBA** | Adiviná el apellido de un jugador activo de 5 letras en 6 intentos. |
| 7 | **Ahorcado** | Descubrí el nombre de un jugador activo antes de perder las 6 vidas. |
| 8 | **Franquicias** | Adiviná el apodo por ciudad/estado/fundación, o el nombre por la sigla. |
| 9 | **Más antigua** | ¿Qué franquicia se fundó primero? Racha hasta fallar. |
| 10 | **¿Sigue activo?** | ¿El jugador está activo o retirado? Datos de `nba_api`. |
| 11 | **Memoria** | Uní cada escudo con su apodo. Menos movimientos, más puntos. |
| 12 | **NBA Bingo** | Tarjeta 3x3 de condiciones (campeón, posición, equipo…). Te toca un jugador por turno: ubicalo donde cumple o saltalo (3 saltos). Líneas = bonus. |
| 13 | **Bingo Histórico** | Igual que el Bingo, pero solo con leyendas retiradas y condiciones por década de debut. |
| 14 | **NBA5** | Adiviná al jugador en 5 intentos. Cada intento marca en verde qué atributos coinciden (equipo, posición, puntos, anillos, debut) y con flechas ↑↓ si el misterioso tiene más o menos. |
| 15 | **NBA5 Retro** | NBA5 con jugadores retirados. |
| 16 | **NBA Impostor** | Entre 4 jugadores, 3 comparten algo (equipo, título, posición…) y uno no. Encontrá al impostor. |
| 17 | **NBA Grid** | Cuadrícula 3x3: en cada cruce de dos equipos, nombrá un jugador que haya pasado por ambos. Un intento por casilla. |
| 18 | **NBA Top 10** | Completá un ranking (puntos, anillos o valoración) escribiendo los nombres. 3 errores y termina. |
| 19 | **NBA Pirámide** | Te muestran 10 jugadores de a uno, sin saber los que vienen. Ubicalos en una pirámide (1-2-3-4): arriba, los de mayor valoración. |
| 20 | **NBA Link** | Conectá dos jugadores con una cadena de jugadores que compartan equipo. Menos eslabones, más puntos. |
| 21 | **Verdadero o Falso** | 10 afirmaciones generadas sobre equipos, anillos y puntos. |

Cada modo tiene un umbral de victoria; ganar suma a la racha y da más XP.

---

## Datos y tecnología

- **HTML + CSS + JavaScript puro**, en un único archivo. Sin dependencias.
- **Datos:** [`nba_api`](https://github.com/swar/nba_api) (franquicias y listado de jugadores). Estadísticas de carrera, anillos, equipos y año de debut de los 42 jugadores del catálogo: cargados a mano (aproximados).
- **Imágenes:** fotos y logos oficiales incrustados como base64 (generados con `hoopdle_fotos.py`). Los escudos de respaldo son SVG propios.
- **Almacenamiento:** cuentas, rachas y récords en `localStorage` del navegador.
- **Tipografías:** Anton y Barlow (Google Fonts).

### Cómo publicarlo
1. Subí la carpeta a Netlify Drop (https://app.netlify.com/drop), Cloudflare Pages, GitHub Pages o Vercel.
2. Listo: no necesita backend.

### Actualizar fotos y logos
```
pip install nba_api pillow requests
python hoopdle_fotos.py
```
Genera `hoopdle_fotos.json`. Dentro del juego, botón **"Cargar fotos reales"** al final del menú.

---

## Limitaciones conocidas
- Las cuentas viven en el navegador de cada persona: no hay ranking compartido ni sincronización entre dispositivos.
- El catálogo de los juegos de jugadores es chico (42 jugadores), por lo que las partidas se repiten con el tiempo.
- Estadísticas, anillos y equipos del catálogo son aproximados y pueden quedar desactualizados.

## Desarrollador
**Santino** — idea, dirección y producto.
Desarrollado con la asistencia de **Claude (Anthropic)**.
Contacto: _[agregá acá tu email / usuario]_

## Créditos y aviso legal
- Datos de franquicias y jugadores: proyecto [`nba_api`](https://github.com/swar/nba_api).
- Fotos y logos: propiedad de la NBA y sus equipos. Se usan para fines personales/educativos. Si publicás el sitio, asegurate de tener los derechos o quitá las imágenes.
- HOOPDLE es un proyecto de fans, sin afiliación oficial con la NBA.
