from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers

from .models import Card, Customer, CustomerCardPurchase
from .validators import (
    validate_card_price,
    validate_email_value,
    validate_phone_value,
)


class CustomerPurchaseSerializer(serializers.ModelSerializer):
    cardId = serializers.PrimaryKeyRelatedField(
        queryset=Card.objects.all(),
        source="card",
    )
    quantity = serializers.IntegerField(min_value=1, max_value=9999)

    class Meta:
        model = CustomerCardPurchase
        fields = ["cardId", "quantity"]


class CustomerSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source="first_name", max_length=100)
    lastName = serializers.CharField(source="last_name", max_length=100)
    birthDate = serializers.DateField(source="birth_date")
    purchases = CustomerPurchaseSerializer(
        many=True,
        write_only=True,
        required=False,
        allow_empty=True,
    )
    purchasedCardsSummary = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Customer
        fields = [
            "id",
            "firstName",
            "lastName",
            "email",
            "phone",
            "birthDate",
            "purchases",
            "purchasedCardsSummary",
        ]

    def get_purchasedCardsSummary(self, obj):
        lines = (
            obj.card_purchases.select_related("card")
            .all()
            .order_by("card_id")
        )
        if not lines:
            return ""
        return ", ".join(
            f"{line.card.annotation} (#{line.card.id}) × {line.quantity}"
            for line in lines
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["purchases"] = [
            {"cardId": line.card_id, "quantity": line.quantity}
            for line in instance.card_purchases.all().order_by("card_id")
        ]
        return ret

    def validate_phone(self, value):
        try:
            return validate_phone_value(value)
        except DjangoValidationError as exc:
            raise serializers.ValidationError(exc.messages)

    def validate_email(self, value):
        try:
            return validate_email_value(value)
        except DjangoValidationError as exc:
            raise serializers.ValidationError(exc.messages)

    def validate(self, attrs):
        raw = attrs.get("purchases")
        if raw is None:
            return attrs
        merged = {}
        for item in raw:
            card = item["card"]
            qty = item["quantity"]
            merged[card.pk] = merged.get(card.pk, 0) + qty
        attrs["purchases"] = [
            {"card": Card.objects.get(pk=pk), "quantity": q}
            for pk, q in merged.items()
        ]
        return attrs

    def create(self, validated_data):
        purchases_data = validated_data.pop("purchases", [])
        customer = Customer.objects.create(**validated_data)
        self._sync_purchases(customer, purchases_data)
        return customer

    def update(self, instance, validated_data):
        sentinel = object()
        purchases_data = validated_data.pop("purchases", sentinel)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if purchases_data is not sentinel:
            self._sync_purchases(instance, purchases_data)
        return instance

    def _sync_purchases(self, customer, purchases_data):
        customer.card_purchases.all().delete()
        for item in purchases_data:
            CustomerCardPurchase.objects.create(
                customer=customer,
                card=item["card"],
                quantity=item["quantity"],
            )


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["id", "price", "picture", "annotation", "description", "discount"]

    def validate_price(self, value):
        try:
            return validate_card_price(value)
        except DjangoValidationError as exc:
            raise serializers.ValidationError(exc.messages)
