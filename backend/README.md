# Django backend

## Start

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Если админка без стилей (голый HTML)

При **`DEBUG=false`** Django через `runserver` сам статику админки не раздаёт. Либо запускайте с **`DEBUG=true`** (локально по умолчанию так и есть), либо настройте раздачу статики для продакшена (`collectstatic` + nginx).

Страницы **`/api/…`** — это API и браузерный вид DRF, а не макет из Vue: отдельный дизайн у сайта на **`npm run dev`** в корне проекта.

## Endpoints

- `GET /api/` - API description endpoint.
- **`/api/customers/`** — покупатели в БД (CRUD, JSON camelCase):
  - `GET/POST /api/customers/`
  - `GET/PUT/PATCH/DELETE /api/customers/<id>/`
- `GET /api/cards/` - returns JSON with `items`.

## Customer JSON (`customers`)

Связь с карточками товаров — массив **числовых id** из `/api/cards/`:

```json
{
  "id": 1,
  "firstName": "Иван",
  "lastName": "Петров",
  "email": "ivan@example.com",
  "phone": "+79161234567",
  "birthDate": "1990-06-15",
  "purchasedCardIds": [1, 3],
  "purchasedCardsSummary": "Annotation one (#1), Annotation three (#3)"
}
```

`purchasedCardsSummary` возвращается только при чтении (список/одна запись).

## `GET /api/cards/` response

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
