# 💻 Proyecto Frontend Base (HTML, CSS, JS)

Este repositorio contiene una plantilla profesional y escalable para el desarrollo frontend usando **HTML, CSS y JavaScript puros**, sin frameworks, ideal para comenzar nuevos proyectos, practicar diseño o estructurar sitios estáticos limpios.

---

## 📂 Estructura de Carpetas

```plaintext
my-frontend-project/
├── public/                  # Archivos estáticos accesibles directamente por el navegador
│   ├── favicon.ico
│   ├── logo192.png
│   ├── logo512.png
│   └── index.html           # HTML base (inicio de la app)
│
├── src/                     # Código fuente del proyecto
│   ├── assets/              # Imágenes, íconos y fuentes
│   │   ├── images/
│   │   ├── icons/
│   │   └── fonts/
│   │
│   ├── components/          # Componentes reutilizables UI
│   │   ├── Navbar/
│   │   └── Footer/
│   │
│   ├── pages/               # Páginas completas del sitio (About, Contact, etc.)
│   ├── css/                 # Estilos globales y variables
│   ├── js/                  # Lógica JS y utilidades
│   │   └── utils/
│   └── test/                # Archivos de prueba JS (opcional)
│
├── .gitignore               # Ignora archivos/carpetas innecesarias para Git
├── .prettierrc              # Configuración de estilos con Prettier
├── LICENSE                  # Tipo de licencia (MIT por defecto)
├── CONTRIBUTING.md          # Guía para contribuir al proyecto
├── README.md                # Este archivo
├── index.html               # HTML de respaldo (sin servidor)
└── package.json             # Configuración base para npm o live-server
```
⚙️ Instalación y uso
🔁 Clonar el repositorio
```
git clone https://github.com/tu-usuario/my-frontend-project.git
cd my-frontend-project
```
🚀 Usar con Live Server (recomendado para desarrollo rápido)

Si ya tienes instalado live-server, puedes iniciar el servidor así:

live-server public

Si no lo tienes, puedes instalarlo con:
```
npm install -g live-server
```
🧩 ¿Qué contiene esta plantilla?

    ✅ HTML5 semántico

    🎨 CSS separado por componentes y variables globales

    🧠 JS modular con carpeta utils/

    🧱 Componentes reutilizables (Navbar, Footer)

    🔍 Carpeta pages/ para páginas separadas (multi-vista)

    🧪 Carpeta test/ para comenzar con pruebas JavaScript

    📦 package.json básico listo para scripts como live-server

    📂 Archivos .gitkeep para subir carpetas vacías a GitHub

🧠 Buenas prácticas recomendadas

    Usa components/ para UI modular y mantenible.

    Mantén tus imágenes en assets/images y fuentes en fonts/.

    Usa variables.css para personalizar colores y temas fácilmente.

    Si creces en complejidad, podrías migrar a Vite, Parcel o Webpack.

🤝 Contribuir

¿Quieres mejorar esta plantilla? ¡Gracias! Revisa el archivo CONTRIBUTING.md para más detalles.
📄 Licencia

Este proyecto está bajo la licencia MIT. Revisa LICENSE para más información.
