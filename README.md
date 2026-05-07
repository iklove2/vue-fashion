# Vue Fashion

Адаптивный фронтенд-проект на Vue 3 + Vite, сверстанный по Figma-макету (desktop / tablet / iPhone), включая hover-состояния и подключенные изображения из макета.

## Стек

- Vue 3
- Vite
- CSS
- Docker + Nginx

## Запуск локально

```bash
npm install
npm run dev
```

## Docker

```bash
docker compose up -d --build
```

## Backend API: Feedback form

### Endpoint

- `POST /api/feedback`

Создает обращение из формы обратной связи.

### Request headers

- `Content-Type: application/json`

### Request body

```json
{
  "name": "Иван",
  "email": "ivan@mail.com",
  "message": "Хочу демо и оценку стоимости."
}
```

### Validation requirements

- `name`
  - required
  - string, trimmed
  - length: 2..60
  - allowed chars: letters (RU/EN), space, hyphen, apostrophe
- `email`
  - required
  - string, trimmed, lowercase
  - length: 5..254
  - valid email format
  - no spaces
- `message`
  - optional
  - string, trimmed
  - length: 0..1000
  - if provided, must not be only spaces

### Responses

- `201 Created`

```json
{
  "ok": true,
  "id": "fb_123",
  "message": "Спасибо! Мы свяжемся с вами."
}
```

- `400 Bad Request` (validation error)

```json
{
  "ok": false,
  "error": "VALIDATION_ERROR",
  "fields": {
    "email": "Invalid email",
    "name": "Name must be 2-60 characters"
  }
}
```

- `429 Too Many Requests` (optional rate limit)

```json
{
  "ok": false,
  "error": "RATE_LIMIT"
}
```

# Vue 3 + Vite

This template should help get you started developing with Vue 3 in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

Learn more about IDE Support for Vue in the [Vue Docs Scaling up Guide](https://vuejs.org/guide/scaling-up/tooling.html#ide-support).
