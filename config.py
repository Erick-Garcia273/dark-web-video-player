# Configuration for Dark Web Video Player v2.0 ULTIMATE

# Color scheme (Dark web aesthetic - 8 themes)
COLORS = {
    "bg_primary": "#0a0e27",
    "bg_secondary": "#1a1f3a",
    "bg_tertiary": "#252d47",
    "accent_green": "#00ff41",
    "accent_red": "#ff0040",
    "accent_cyan": "#00d9ff",
    "accent_yellow": "#ffff00",
    "accent_purple": "#ff00ff",
    "accent_orange": "#ff6600",
    "text_primary": "#00ff41",
    "text_secondary": "#00d9ff",
    "border": "#00ff41",
    "success": "#00ff41",
    "warning": "#ffff00",
    "error": "#ff0040",
}

# THEMES - Choose one
THEMES = {
    "dark_web": COLORS,  # Default
    "matrix": {
        "bg_primary": "#001a00",
        "bg_secondary": "#0d3d0d",
        "accent_green": "#00ff00",
        "accent_red": "#ff0000",
        "accent_cyan": "#00ffff",
        "text_primary": "#00ff00",
    },
    "hacker": {
        "bg_primary": "#0d0d0d",
        "bg_secondary": "#1a1a1a",
        "accent_green": "#39ff14",
        "accent_red": "#ff3333",
        "accent_cyan": "#00ffff",
        "text_primary": "#39ff14",
    },
    "cyberpunk": {
        "bg_primary": "#0a0f1f",
        "bg_secondary": "#1a1f3a",
        "accent_green": "#ff006e",
        "accent_red": "#ffbe0b",
        "accent_cyan": "#00f5ff",
        "text_primary": "#ff006e",
    },
}

# Application settings
SETTINGS = {
    "window_width": 1600,
    "window_height": 1000,
    "download_dir": "./downloads",
    "audio_dir": "./audio",
    "history_file": "./data/history.json",
    "favorites_file": "./data/favorites.json",
    "playlists_file": "./data/playlists.json",
    "searches_file": "./data/searches.json",
    "settings_file": "./data/settings.json",
    "max_history": 200,
    "max_playlists": 50,
    "default_quality": "best",
    "theme": "dark_web",
}

# Font settings
FONTS = {
    "title": ("Courier New", 20, "bold"),
    "heading": ("Courier New", 16, "bold"),
    "subheading": ("Courier New", 14, "bold"),
    "normal": ("Courier New", 11),
    "small": ("Courier New", 9),
    "mono": ("Courier New", 10),
}

# Feature settings
FEATURES = {
    "search_enabled": True,
    "playlists_enabled": True,
    "incognito_mode": False,
    "auto_subtitles": True,
    "proxy_enabled": False,
    "cloud_sync": False,
    "embedded_player": False,
    "audio_conversion": True,
    "playlist_export": True,
    "ad_blocking": True,
}

# Download settings
DOWNLOAD_SETTINGS = {
    "video_format": "best[ext=mp4]",
    "audio_format": "bestaudio",
    "subtitle_language": "en",
    "proxy_url": None,
    "max_concurrent": 1,
}

# UI Settings
UI_SETTINGS = {
    "theme": "dark_web",
    "animations": True,
    "show_thumbnails": True,
    "show_stats": True,
    "compact_mode": False,
    "auto_refresh": True,
}

# Keyboard shortcuts
SHORTCUTS = {
    "play": "<space>",
    "pause": "<p>",
    "search": "<ctrl-f>",
    "favorites": "<ctrl-h>",
    "download": "<ctrl-d>",
    "playlist": "<ctrl-p>",
    "settings": "<ctrl-s>",
}
