# Discord Bot - Selector de Países 🌍

Bot para Discord que permite a los usuarios seleccionar su país reaccionando con una bandera 🇪🇸🇲🇽🇫🇷 y recibir un rol automático.  
Ideal para servidores multicomunidad.

---

## 🚀 Características

✅ Publica mensajes por continentes / subzonas con banderas.  
✅ Asigna automáticamente un rol según la bandera seleccionada.  
✅ Elimina el rol si el usuario quita su reacción.  
✅ Guarda los mensajes publicados para evitar duplicados en reinicios.  
✅ Permite configuración vía archivo `config.json`.

---

## 🛠 Requisitos

- Python 3.11+  
- Discord bot token  
- Permisos de bot en Discord:
  - `Manage Roles`
  - `Read Messages`
  - `Add Reactions`

---

## ⚙ Configuración

1️⃣ Edita `config.json`:
```json
{
    "discord_token": "TU_DISCORD_TOKEN",
    "guild_id": "TU_GUILD_ID",
    "channel_id": "TU_CHANNEL_ID",
    "message": "✨ ¡Selecciona tu país reaccionando con la bandera! ✨"
}
```

2️⃣ Usa el `countries.json` incluido para personalizar los países y emojis.

---

## 🐳 Docker

Construir y ejecutar:
```bash
docker-compose up --build
```

Limitar memoria (opcional, ya incluido en docker-compose):
```yaml
deploy:
  resources:
    limits:
      memory: 300M
```

---

## ✨ Créditos

Bot desarrollado por [Crinlorite](https://github.com/Crinlorite) 💚  
