# Vue Fashion

Адаптивный фронтенд-проект на Vue 3 + Vite, сверстанный по Figma-макету (desktop / tablet / iPhone), включая hover-состояния и подключенные изображения из макета.

## Стек

- Vue 3
- Vite
- CSS
- Django + SQLite (backend в каталоге `backend/`)

## Запуск локально

Фронт:

```bash
npm install
npm run dev
```

Отдельно подними Django из каталога `backend/` (см. `backend/README.md`).

При `npm run dev` Vite проксирует запросы `/api/*` на `http://127.0.0.1:8000` — см. `vite.config.js`.

## API endpoints

- `GET /api/` — описание API.
- **`/api/customers/`** — покупатели (полный CRUD, поля в JSON в **camelCase**):
  - `GET /api/customers/` — список
  - `POST /api/customers/` — создать
  - `GET /api/customers/<id>/` — один объект
  - `PUT` / `PATCH /api/customers/<id>/` — изменить
  - `DELETE /api/customers/<id>/` — удалить
- `GET /api/cards/` — карточки в формате JSON:

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

Пример тела запроса `POST /api/customers/` или ответа `GET`:

```json
{
  "id": 1,
  "firstName": "Иван",
  "lastName": "Петров",
  "email": "ivan@example.com",
  "phone": "+79161234567",
  "birthDate": "1990-06-15",
  "purchasedCardIds": [1, 2, 3],
  "purchasedCardsSummary": "ELLERY … (#1), … (#2)"
}
```

`purchasedCardIds` — реальные **id** из `/api/cards/` (что человек «купил»). В ответе дополнительно есть строка **`purchasedCardsSummary`** (только чтение). При `POST` поле `id` не передаётся. `email` уникален.

# Vue 3 + Vite

This template should help get you started developing with Vue 3 in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

Learn more about IDE Support for Vue in the [Vue Docs Scaling up Guide](https://vuejs.org/guide/scaling-up/tooling.html#ide-support).
