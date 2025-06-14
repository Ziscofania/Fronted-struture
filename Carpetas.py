import os

folders = [
    "my-frontend-project/public",
    "my-frontend-project/src/assets/images",
    "my-frontend-project/src/assets/icons",
    "my-frontend-project/src/assets/fonts",
    "my-frontend-project/src/components/Navbar",
    "my-frontend-project/src/components/Footer",
    "my-frontend-project/src/pages",
    "my-frontend-project/src/css",
    "my-frontend-project/src/js/utils",
    "my-frontend-project/src/test",
]

files = {
    # Public
    "my-frontend-project/public/index.html": "<!-- HTML público base -->",
    "my-frontend-project/public/favicon.ico": "",
    "my-frontend-project/public/logo192.png": "",
    "my-frontend-project/public/logo512.png": "",
    "my-frontend-project/public/public.md": """# 📂 Carpeta `public/`

Esta carpeta contiene archivos estáticos entregados directamente al navegador.
""",

    # Assets (solo .gitkeep para que git los suba vacíos)
    "my-frontend-project/src/assets/fonts/.gitkeep": "",
    "my-frontend-project/src/assets/images/.gitkeep": "",
    "my-frontend-project/src/assets/icons/.gitkeep": "",

    # Componentes
    "my-frontend-project/src/components/Navbar/navbar.html": "<nav>Navbar</nav>",
    "my-frontend-project/src/components/Navbar/navbar.css": "/* estilos navbar */",
    "my-frontend-project/src/components/Navbar/navbar.js": "// lógica navbar",

    "my-frontend-project/src/components/Footer/footer.html": "<footer>Footer</footer>",
    "my-frontend-project/src/components/Footer/footer.css": "/* estilos footer */",
    "my-frontend-project/src/components/Footer/footer.js": "// lógica footer",

    # Páginas
    "my-frontend-project/src/pages/home.html": "<!-- Página Home -->",
    "my-frontend-project/src/pages/about.html": "<!-- Página About -->",
    "my-frontend-project/src/pages/contact.html": "<!-- Página Contact -->",

    # CSS
    "my-frontend-project/src/css/main.css": "body { margin: 0; font-family: sans-serif; }",
    "my-frontend-project/src/css/variables.css": ":root { --primary-color: #6200ea; }",

    # JS
    "my-frontend-project/src/js/app.js": "// JS principal",
    "my-frontend-project/src/js/utils/helpers.js": "// funciones reutilizables",

    # Test
    "my-frontend-project/src/test/sample.test.js": "// Pruebas aquí",

    # Archivos raíz
    "my-frontend-project/.gitignore": "node_modules/\ndist/\n.DS_Store",
    "my-frontend-project/.prettierrc": '{\n  "semi": true,\n  "singleQuote": true\n}',
    "my-frontend-project/README.md": "# Proyecto Frontend\n\nPlantilla base HTML/CSS/JS.",
    "my-frontend-project/LICENSE": "MIT License",
    "my-frontend-project/CONTRIBUTING.md": "## Cómo contribuir\n\n- Haz un fork\n- Trabaja en una rama\n- Abre un Pull Request",
    "my-frontend-project/package.json": '{\n  "name": "frontend-project",\n  "version": "1.0.0",\n  "scripts": {\n    "start": "live-server public"\n  }\n}',
    "my-frontend-project/index.html": "<!-- Copia del index si no se usa servidor -->",
}

# Crear carpetas
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Crear archivos
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Proyecto frontend creado con estructura profesional.")
