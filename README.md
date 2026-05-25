# Universidad de El Salvador
## Facultad Multidisciplinaria de Occidente – Ingeniería en Desarrollo de Software

### Objetivo:
Validar la comprensión e implementación práctica de los conceptos fundamentales de la Unidad 3 de Desarrollo de Aplicaciones Web, mediante la creación de un proyecto frontend en React que demuestre el dominio en la arquitectura de componentes, la gestión de estados dinámicos y la integración de servicios externos utilizando Axios en base a los ejemplos desarrollados en clase.

---

## INDICACIONES GENERALES

- **Modalidad:** Esta evaluación es estrictamente individual. Cualquier indicio de plagio, clonación de repositorios o código idéntico entre compañeros resultará en la anulación automática de la prueba (nota 0.0).
- **Tiempo de Entrega:** El proyecto y el reporte en formato PDF deberán ser subidos a la plataforma del campus virtual en la fecha indicada. No se aceptarán entregas tardías.

---

## APIS SUGERIDAS Y SELECCIÓN DEL TEMA

A continuación, se presenta una lista de APIs públicas y de solo lectura (no requieren registrarse ni usar llaves de acceso/API Keys) que puedes utilizar como base de datos para tu proyecto:

1. https://hp-api.onrender.com/
2. https://restcountries.com/
3. https://api.zippopotam.us/
4. https://www.thecocktaildb.com/api.php (Solo utilizar la capa gratuita)
5. https://ghibliapi.dev/
6. https://www.themealdb.com/api.php (Solo utilizar la capa gratuita)

> **Nota importante:** El listado anterior es estrictamente sugerido. Eres completamente libre de elegir cualquier otra API pública diferente que se adapte a tus gustos o intereses, siempre y cuando cumpla con los requisitos del examen: ser de solo lectura, permitir el consumo mediante Axios, y que sus datos te sirvan para estructurar una interfaz con componentes y estados dinámicos en React.

---

## REQUISITOS TÉCNICOS MÍNIMOS

Para el desarrollo de la aplicación, el estudiante deberá cumplir obligatoriamente con el siguiente ecosistema técnico:

- **Entorno de ejecución:** Node.js (Versión LTS recomendada).
- **Herramienta de construcción:** Vite (para inicializar el proyecto de React).
- **Lenguaje:** JavaScript (JSX).
- **Librería Principal:** React JS (utilizando componentes funcionales y Hooks).
- **Consumo de API:** Axios (Instalado mediante npm para realizar las peticiones HTTP de solo lectura).
- **Estilos:** Libre elección (CSS nativo, CSS Modules, Tailwind CSS o Bootstrap).

---

## ESPECIFICACIONES DEL PROYECTO (REACT)

El objetivo de la prueba es demostrar el dominio en la arquitectura de componentes, manejo de estados y el consumo de APIs REST de solo lectura con Axios.

Tu aplicación de React debe cumplir con las siguientes directrices arquitectónicas:

1. **Consumo de Datos con Axios:** Se debe realizar la petición HTTP (GET) a la API seleccionada/asignada utilizando Axios dentro de un Hook `useEffect`.

2. **Manejo de Estados Críticos:** La aplicación debe gestionar correctamente mediante `useState`:
   - El estado de los datos recibidos de la API.
   - Un estado de Carga (`loading`) que muestre un mensaje o spinner mientras se reciben los datos.
   - Un estado de Error (`error`) controlado mediante un bloque `try/catch` por si la petición falla.

3. **Modularidad y Componentes:** El código no debe estar centralizado en un solo archivo. Se evaluará la separación de responsabilidades:
   - Componente contenedor/padre (App o páginas).
   - Componentes hijos reutilizables (Ej: `Card.jsx`, `Grid.jsx`, `Navbar.jsx`, etc.).
   - Paso de información correcto entre componentes a través de Props.

4. **Renderizado Dinámico:** Uso correcto del método `.map()` para recorrer los arreglos de datos devueltos por la API, asegurando la inclusión de la propiedad `key` única para cada elemento.

---

## REQUISITOS DE ENTREGA

La entrega consta de un único archivo en formato PDF que debe subirse al aula virtual y contener los siguientes apartados en orden estricto:

### 1. Portada Formal
- Nombre de la Institución y Facultad.
- Asignatura: [Nombre de la Asignatura].
- Tema: Evaluación Parcial 2.
- Nombre Completo del Estudiante y carnet.
- Nombre del docente.
- Fecha de entrega.

### 2. Introducción del Proyecto
- Una breve explicación redactada por el alumno (mínimo 150 palabras) que describa la solución desarrollada, qué API se consumió, el propósito de la aplicación y la justificación de la estructura de componentes elegida.

### 3. Enlace del Video de Demostración y Defensa (CRUCIAL)
Deberás incluir un enlace web directo a tu video explicativo subido a Google Drive o YouTube.

> **REGLA DE ORO DE CALIFICACIÓN:** El enlace del video debe estar configurado de manera PÚBLICA o con los accesos correctos para que el docente pueda reproducirlo. Si el video no se puede reproducir o el enlace está roto/privado, la calificación automática del examen parcial será de 0.0 (CERO) sin derecho a reclamo.

**Especificaciones obligatorias del video:**
- **Duración máxima:** [15 minutos].
- **Presencia de la cámara:** Es obligatorio que el alumno aparezca en cámara en una esquina de la pantalla o al inicio del video dando la explicación para validar su identidad.
- **Contenido del video:**
  1. **Explicación del Código:** Mostrar el editor de código (VS Code) y explicar detalladamente la estructura del proyecto, cómo se configuró Axios, el uso de los Hooks y cómo se estructuraron los componentes.
  2. **Demostración de la App:** Mostrar el navegador web ejecutando la aplicación de React y demostrar su completo funcionamiento en tiempo real.

---

## RÚBRICA DE EVALUACIÓN

| Criterio de Evaluación | 5 Puntos (Excelente) | 3-4 Puntos (Bueno) | 1-2 Puntos (Regular) | 0 Puntos (No presenta) |
|------------------------|---------------------|-------------------|---------------------|----------------------|
| **1. Consumo de API con Axios** | Usas `axios.get` dentro de un `useEffect` para traer los datos de la API. La aplicación carga la información correctamente. | La API funciona y los datos cargan, pero hay pequeñas alertas (warnings) en la consola del navegador. | Intentaste usar Axios pero la petición falla, o utilizaste el comando `fetch` nativo de JavaScript. | No se conectó la API o el código no funciona. |
| **2. Mensajes de Carga y Errores** | Muestras un mensaje de "Cargando..." mientras descarga la información y manejas errores con `try/catch` por si el internet falla. | Guardas los datos bien, pero olvidaste poner el mensaje de "Cargando..." o el control de errores con `try/catch`. | Solo guardas la información en el estado; ignoras qué pasa si la aplicación tarda en cargar o falla. | No se manejan estados con `useState`. |
| **3. Componentes y Props** | El código está ordenado. Separaste la app en componentes hijos reutilizables (tarjetas, listas) y pasas datos con props. | Creaste componentes separados, pero amontonaste demasiada lógica o pasas la información de forma confusa. | Todo el código del proyecto está metido en un solo archivo (`App.jsx`). No creaste componentes separados. | No hay una estructura de React válida. |
| **4. Video Explicativo** | Te grabas en cámara explicando tu código (Axios y componentes) y muestras tu aplicación funcionando en el navegador. | Te grabas en cámara, pero la explicación es muy rápida, confusa o solo muestras la app sin explicar el código. | El video se reproduce, pero no sales en cámara (solo grabaste pantalla) o no explicaste nada del código. | El enlace no abre, es privado o no pusiste el video. (Aplica la regla de nota automática 0.0). |
| **5. Documento PDF** | Entregas el PDF a tiempo con la portada completa y una introducción clara (mínimo 150 palabras) sobre tu aplicación. | Entregas el PDF a tiempo, pero la introducción es muy corta o copiada de internet sin explicar tu propio proyecto. | El documento está desorganizado, faltan datos importantes de la portada o no incluye la introducción. | No entregaste el archivo PDF. |

---

> 💡 **Tip para README:** Puedes copiar este contenido directamente en tu archivo `README.md`. La tabla de rúbrica ya está en formato Markdown compatible con GitHub/GitLab. Si necesitas ajustar los saltos de línea o encabezados para tu repositorio específico, solo modifica los niveles de `#` según tu estructura de documentación.
