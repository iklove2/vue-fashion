# Django backend

## Start

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Endpoints

- `GET /api/` - API description endpoint.
- `GET /api/cards/` - returns JSON with `items`.

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
