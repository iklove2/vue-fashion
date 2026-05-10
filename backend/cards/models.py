from django.core.exceptions import ValidationError
from django.db import models

from .validators import (
    validate_card_price,
    validate_email_value,
    validate_phone_value,
)


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=32)
    birth_date = models.DateField()

    class Meta:
        ordering = ["id"]

    def clean(self):
        super().clean()
        errors = {}
        try:
            self.phone = validate_phone_value(self.phone)
        except ValidationError as e:
            errors["phone"] = e.messages
        try:
            self.email = validate_email_value(self.email)
        except ValidationError as e:
            errors["email"] = e.messages
        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class CustomerCardPurchase(models.Model):
    """Строка заказа: карточка и количество (одна позиция на тип карточки)."""

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="card_purchases",
    )
    card = models.ForeignKey(
        "Card",
        on_delete=models.CASCADE,
        related_name="customer_purchases",
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["customer", "card"],
                name="cards_customer_card_purchase_unique",
            ),
        ]
        ordering = ["card_id"]

    def __str__(self):
        return f"{self.customer_id}: card {self.card_id} × {self.quantity}"


class Card(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.TextField(help_text="Bitmap encoded as base64.")
    annotation = models.CharField(max_length=255)
    description = models.TextField()
    discount = models.PositiveSmallIntegerField(default=0)

    def clean(self):
        super().clean()
        errors = {}
        try:
            self.price = validate_card_price(self.price)
        except ValidationError as e:
            errors["price"] = e.messages
        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return f"Card #{self.pk}: {self.annotation}"
