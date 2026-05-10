import re
from decimal import Decimal, InvalidOperation

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

CARD_PRICE_MIN = Decimal("0.10")
CARD_PRICE_MAX = Decimal("1000.00")

# После нормализации: опциональный +, затем 10–15 цифр (например +79161234567)
PHONE_PATTERN = re.compile(r"^\+?[0-9]{10,15}$")


def normalize_phone(value: str | None) -> str:
    if value is None:
        return ""
    return re.sub(r"[\s\-()]", "", str(value).strip())


def validate_phone_value(value: str | None) -> str:
    """Нормализует телефон или выбрасывает ValidationError."""
    normalized = normalize_phone(value)
    if not normalized:
        raise ValidationError("Укажите номер телефона.")
    if not PHONE_PATTERN.match(normalized):
        raise ValidationError(
            "Телефон: от 10 до 15 цифр, допускается + в начале (например +79161234567)."
        )
    return normalized


def validate_email_value(value: str | None) -> str:
    """Проверка и нормализация email."""
    v = (value or "").strip()
    if not v:
        raise ValidationError("Укажите email.")
    try:
        validate_email(v)
    except ValidationError:
        raise ValidationError("Некорректный формат email.") from None
    return v.lower()


def validate_card_price(value) -> Decimal:
    """Цена карточки в долларах: от $0.10 до $1000, только число."""
    if value is None or value == "":
        raise ValidationError("Укажите цену.")
    try:
        if isinstance(value, Decimal):
            d = value
        else:
            d = Decimal(str(value).strip().replace(",", "."))
    except (InvalidOperation, TypeError, ValueError):
        raise ValidationError("Цена должна быть числом (буквы недопустимы).") from None

    if d != d.quantize(Decimal("0.01")):
        raise ValidationError("Не больше двух знаков после запятой.")

    if d < CARD_PRICE_MIN:
        raise ValidationError("Цена не меньше $0.10.")
    if d > CARD_PRICE_MAX:
        raise ValidationError("Цена не больше $1000.")
    return d
