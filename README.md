# Vue Fashion

Адаптивный фронтенд-проект на Vue 3 + Vite, сверстанный по Figma-макету (desktop / tablet / iPhone), включая hover-состояния и подключенные изображения из макета.

## Стек

- Vue 3
- Vite
- CSS
- Django + SQLite
- Docker Compose + Nginx

## Запуск локально

```bash
npm install
npm run dev
```

## Docker (frontend + backend)

```bash
# first run only
cp .env.example .env

# start
docker compose up -d --build
```

По умолчанию приложение будет доступно на `http://localhost:8081`.

### Настройка портов и домена

Если на сервере уже крутится другой Django/прокси, просто поменяй порт фронта в `.env`:

```env
WEB_PORT=8081
DEBUG=False
ALLOWED_HOSTS=your-domain.com,localhost,127.0.0.1
```

- `WEB_PORT` - внешний порт контейнера `web` (меняй, чтобы не конфликтовать с другими сервисами).
- `DEBUG` - режим Django.
- `ALLOWED_HOSTS` - разрешенные хосты Django (через запятую).

`backend` не публикуется наружу и доступен только внутри docker-сети, поэтому с другими Django по порту `8000` не конфликтует.

### Полезные команды

```bash
# Остановить контейнеры
docker compose down

# Остановить и удалить volume с SQLite
docker compose down -v

# Логи
docker compose logs -f
```

### Пример для внешнего nginx в docker

Если у тебя уже есть отдельный nginx-контейнер как reverse proxy, проксируй на:

- `http://<host-ip>:WEB_PORT`

Например, при `WEB_PORT=8081`:

```nginx
location / {
    proxy_pass http://host.docker.internal:8081;
}
```

## API endpoints

- `GET /api/` - описание API.
- `GET /api/cards/` - карточки в формате JSON:

```json
{
  "items": [
    {
      "id": 1,
      "price": "52.00",
      "picture": "base64-bitmap-string",
      "annotation": "Card annotation",
      "description": "Card description",
      "discount": 15
    }
  ]
}
```

# Vue 3 + Vite

This template should help get you started developing with Vue 3 in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

Learn more about IDE Support for Vue in the [Vue Docs Scaling up Guide](https://vuejs.org/guide/scaling-up/tooling.html#ide-support).
