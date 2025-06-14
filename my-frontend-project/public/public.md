# 📂 Carpeta `public/`

Esta carpeta contiene **archivos estáticos** que se entregan directamente al navegador. En muchos entornos, los archivos dentro de `public/` **no se procesan ni transforman** (por ejemplo, al usar Vite, Parcel, etc.).

## ¿Qué va aquí?

- `favicon.ico`: ícono de la pestaña del navegador.
- `logo192.png`, `logo512.png`: logotipos para PWA o redes sociales.
- `index.html`: el HTML base, útil si no hay compilación.
- Otros recursos como: `robots.txt`, `manifest.json`, etc.

## ❗ Recomendación

No coloques archivos JavaScript o CSS aquí si vas a usar un sistema modular con `src/`, porque no se compilan ni procesan.
