````markdown
# 🔐 DARK WEB VIDEO PLAYER v2.0 - ULTIMATE EDITION

Una aplicación YouTube-style con estética cyberpunk/dark web hecha en Python.

```
█ DARK WEB VIDEO SYSTEM v2.0 █
[⚠️ ANONYMOUS MODE ACTIVE ⚠️]
```

---

## ✨ **CARACTERÍSTICAS ULTRA-AVANZADAS**

### 🎬 **REPRODUCCIÓN Y DESCARGA**
- ✅ Streaming directo de videos
- ✅ Descarga de videos en máxima calidad
- ✅ Descarga de playlists completas
- ✅ Extracción de audio (MP3)
- ✅ Descarga con subtítulos automáticos
- ✅ **🚫 BLOQUEO COMPLETO DE ANUNCIOS**

### 🚫 **BLOQUEADOR DE ANUNCIOS**
- ✅ Bloquea 30+ dominios de publicidad
- ✅ Soporte para YouTube, Google Ads, Facebook Ads
- ✅ Integración con SponsorBlock
- ✅ Salta patrocinios automáticamente
- ✅ Salta intros/outros
- ✅ Descarga 100% libre de anuncios
- ✅ Estadísticas de anuncios bloqueados

### 📋 **SISTEMA DE PLAYLISTS**
- ✅ Crear/eliminar playlists
- ✅ Agregar videos a playlists
- ✅ Exportar a JSON y M3U
- ✅ Importar playlists
- ✅ Gestión completa de contenido

### 🔍 **BÚSQUEDA AVANZADA**
- ✅ Búsqueda en tiempo real
- ✅ Historial de búsquedas
- ✅ 15+ resultados por búsqueda
- ✅ Información completa de videos

### 🔒 **PRIVACIDAD Y SEGURIDAD**
- ✅ Modo incógnito (sin guardar historial)
- ✅ Soporte para proxy/VPN
- ✅ Verificación de conexión
- ✅ Datos encriptados localmente

### 🎨 **4 TEMAS INCLUIDOS**
1. **Dark Web** - Original neon green
2. **Matrix** - Tema matrix tradicional
3. **Hacker** - Verde brillante retro
4. **Cyberpunk** - Colores futuristas

### 🎵 **GESTOR DE AUDIO**
- ✅ Conversión a MP3
- ✅ Lista de audios descargados
- ✅ Reproductor integrado
- ✅ Gestor de almacenamiento

### 💾 **IMPORT/EXPORT AVANZADO**
- ✅ Exportar playlists a JSON
- ✅ Exportar playlists a M3U
- ✅ Importar desde archivo
- ✅ Migración fácil de datos

### 💻 **CLI COMPLETA**
```bash
# Descargar video sin anuncios
python cli.py -d "URL"

# Descargar solo audio
python cli.py -d "URL" -a

# Descargar playlist
python cli.py -dp "URL"

# Buscar videos
python cli.py -sq "query"

# Crear playlist
python cli.py -cp "nombre"

# Exportar playlist
python cli.py -ep "nombre" "json"
```

### ⚙️ **CONFIGURACIÓN AVANZADA**
- ✅ 8 colores neon personalizables
- ✅ Temas switchables
- ✅ Proxy/VPN configuration
- ✅ Shortcuts de teclado
- ✅ Modo compacto
- ✅ Auto-refresh

### 📊 **ESTADÍSTICAS**
- ✅ Total de videos descargados
- ✅ Total de audios descargados
- ✅ Tamaño total en GB
- ✅ Contador de playlists
- ✅ Búsquedas realizadas
- ✅ **Anuncios bloqueados**

---

## 📋 **ESTRUCTURA DE ARCHIVOS**

```
dark-web-video-player/
├── main.py              # GUI Principal (700+ líneas)
├── video_manager.py     # Gestor avanzado (600+ líneas)
├── ui_components.py     # Componentes UI (400+ líneas)
├── ad_blocker.py       # Bloqueador de anuncios (400+ líneas)
├── cli.py              # Interfaz CLI (300+ líneas)
├── config.py           # Configuración (200+ líneas)
├── requirements.txt    # Dependencias
├── README.md          # Documentación
├── .gitignore         # Ignorados
├── downloads/         # Videos descargados
├── audio/            # Audios descargados
└── data/
    ├── history.json       # Historial
    ├── favorites.json     # Favoritos
    ├── playlists.json     # Playlists
    ├── searches.json      # Búsquedas
    └── settings.json      # Configuración
```

---

## 🚀 **INSTALACIÓN**

### Requisitos
- Python 3.7+
- FFmpeg (para audio)
- pip

### Pasos

```bash
# 1. Clonar repositorio
git clone https://github.com/Erick-Garcia273/dark-web-video-player.git
cd dark-web-video-player

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\\Scripts\\activate  # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar GUI
python main.py

# O usar CLI
python cli.py --help
```

---

## 🎯 **USO COMPLETO**

### **GUI - 6 PESTAÑAS**

#### 🏠 **HOME**
- Ingresa URL
- Ver info completa del video
- Reproducir en streaming **SIN ANUNCIOS**
- Descargar
- Agregar a favoritos
- Agregar a playlist

#### 🔍 **SEARCH**
- Búsqueda en tiempo real
- Historial de búsquedas
- 15+ resultados
- Selecciona resultado para ir a HOME

#### 📋 **PLAYLISTS**
- Crear nuevas playlists
- Eliminar playlists
- Ver videos en playlist
- Abrir playlist manager

#### ⬇️ **DOWNLOAD**
- URL input
- Barra de progreso
- Log de operaciones
- Descargar video/audio/subtítulos
- **Ver anuncios bloqueados**

#### 📁 **LIBRARY**
- Ver videos descargados
- Ver audios descargados
- Estadísticas en tiempo real
- Reproducir local
- Eliminar archivos

#### ⏱️ **HISTORY**
- Historial completo
- Timestamps
- Limpiar historial
- Búsqueda rápida

---

## 🚫 **BLOQUEO DE ANUNCIOS - CÓMO FUNCIONA**

### **Automáticamente:**
1. Detecta dominios de anuncios (30+)
2. Bloquea Google Ads, Facebook Ads, Doubleclick
3. Integra SponsorBlock para saltar patrocinios
4. Salta intros/outros automáticamente
5. Descarga sin anuncios insertados

### **Dominios Bloqueados:**
```
YouTube/Google:
- ads.google.com
- pagead2.googlesyndication.com
- googleads.g.doubleclick.net
- doubleclick.net
- youtube.com/ads

Facebook:
- ads.facebook.com

Microsoft:
- ads.microsoft.com

Y 20+ más...
```

---

## 💻 **COMANDOS CLI**

```bash
# DESCARGA
python cli.py -d "URL"                    # Descargar video
python cli.py -d "URL" -a                 # Solo audio (MP3)
python cli.py -d "URL" -s                 # Con subtítulos
python cli.py -dp "PLAYLIST_URL"          # Descargar playlist

# BÚSQUEDA
python cli.py -sq "query"                 # Buscar videos

# PLAYLISTS
python cli.py -cp "nombre"                # Crear playlist
python cli.py -lp                         # Listar playlists
python cli.py -ep "nombre" "json"         # Exportar a JSON
python cli.py -ep "nombre" "m3u"          # Exportar a M3U
python cli.py -ip "archivo.json"          # Importar playlist

# BIBLIOTECA
python cli.py -ld                         # Listar descargas
python cli.py -la                         # Listar audios
```

---

## 🎨 **TEMAS DISPONIBLES**

### Dark Web (Default)
```
Colores: Verde neon, rojo, cyan, amarillo
Vibra: Original cyberpunk
```

### Matrix
```
Colores: Verde clásico
Vibra: Efecto matrix retro
```

### Hacker
```
Colores: Verde brillante #39ff14
Vibra: Hacker legítimo 90s
```

### Cyberpunk
```
Colores: Magenta, amarillo, cyan
Vibra: Futuro distópico
```

---

## 🔒 **MODO INCÓGNITO**

Activa desde el botón en la barra:
```
🔐 INCOGNITO MODE [ACTIVE]
```

**Funciona así:**
- No guarda historial
- No guarda búsquedas
- No guarda favoritos
- Datos locales solo en RAM
- Se borra al cerrar la app

---

## 🌐 **PROXY/VPN**

En Settings → Network:
1. Ingresa URL del proxy
2. Click "Test Connection"
3. Click "Save Proxy"
4. Reinicia la app

**Ejemplo:**
```
http://proxy.example.com:8080
socks5://vpn.service.com:1080
```

---

## ⌨️ **SHORTCUTS**

```
<Ctrl+F>    Abrir búsqueda
<Ctrl+D>    Iniciar descarga
<Ctrl+P>    Playlists
<Ctrl+S>    Settings
<Ctrl+H>    Historial
```

---

## 📊 **ESTADÍSTICAS**

La app rastrea:
- Videos descargados (total)
- Audios descargados (total)
- Tamaño total (GB)
- Playlists creadas
- Búsquedas realizadas
- **Anuncios bloqueados**
- Tiempo de uso

---

## 🔐 **PRIVACIDAD**

- **Local First**: Todo se guarda localmente
- **Sin Tracking**: No hay analytics
- **Datos Encriptados**: JSON encriptado
- **Incógnito**: Modo privado disponible
- **Open Source**: Código verificable
- **Sin Anuncios**: Bloqueador completo

---

## 📝 **EJEMPLOS DE USO**

### Descargar una playlist completa sin anuncios
```bash
python cli.py -dp "https://youtube.com/playlist?list=PLxxxxx"
```

### Extraer solo el audio de un video
```bash
python cli.py -d "https://youtube.com/watch?v=xxx" -a
```

### Crear playlist y exportar
```bash
python cli.py -cp "Mi Playlist"
python cli.py -ep "Mi Playlist" "m3u"
```

### Buscar y listar resultados
```bash
python cli.py -sq "Python Tutorials"
```

---

## 🛠️ **DESARROLLO**

### Estructura de código
- **main.py**: 800+ líneas - GUI Principal
- **video_manager.py**: 600+ líneas - Lógica de videos
- **ad_blocker.py**: 400+ líneas - Bloqueador de anuncios
- **ui_components.py**: 400+ líneas - Componentes custom
- **cli.py**: 300+ líneas - Interfaz CLI
- **config.py**: 200+ líneas - Configuración

### Total: 2700+ líneas de código

---

## 📄 **LICENCIA**

MIT License - Libre para usar y modificar

---

## 📞 **SOPORTE**

Para reportar bugs o sugerencias:
- Issues en GitHub
- Pull Requests bienvenidos

---

## 👨‍💻 **AUTOR**

**Erick Garcia**
- GitHub: [@Erick-Garcia273](https://github.com/Erick-Garcia273)
- Email: tu-email@ejemplo.com

---

## ⚖️ **DISCLAIMER**

⚠️ **SOLO PARA FINES EDUCATIVOS**

- Respeta los términos de servicio de los sitios
- No descargues contenido protegido sin permiso
- Los creadores tienen derechos de autor
- Usa responsablemente
- La app es una herramienta, el usuario es responsable
- **El bloqueo de anuncios es legal en la mayoría de países**

---

**Hecho con ⌨️ y 💻 por Erick Garcia**

*"En la era digital, la privacidad es poder"*

---

## 🌟 **FEATURES ROADMAP (v3.0)**

- [ ] Reproductor integrado (VLC)
- [ ] Sincronización en la nube
- [ ] Machine learning para recomendaciones
- [ ] Compresión de video
- [ ] Streaming por P2P
- [ ] Bot de Telegram
- [ ] App móvil (Android/iOS)
- [ ] Descarga de comments
- [ ] Generador de thumbnails
- [ ] Editor de videos

````
