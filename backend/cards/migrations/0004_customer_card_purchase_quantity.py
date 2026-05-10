# Generated manually — строки заказа с количеством вместо простого M2M.

from django.db import migrations, models
import django.db.models.deletion


def copy_m2m_to_purchases(apps, schema_editor):
    Customer = apps.get_model("cards", "Customer")
    CustomerCardPurchase = apps.get_model("cards", "CustomerCardPurchase")
    Through = Customer.purchased_cards.through
    for row in Through.objects.all().values("customer_id", "card_id"):
        CustomerCardPurchase.objects.create(
            customer_id=row["customer_id"],
            card_id=row["card_id"],
            quantity=1,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0003_customer_card_m2m"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomerCardPurchase",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "card",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer_purchases",
                        to="cards.card",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="card_purchases",
                        to="cards.customer",
                    ),
                ),
            ],
            options={
                "ordering": ["card_id"],
            },
        ),
        migrations.AddConstraint(
            model_name="customercardpurchase",
            constraint=models.UniqueConstraint(
                fields=("customer", "card"),
                name="cards_customer_card_purchase_unique",
            ),
        ),
        migrations.RunPython(copy_m2m_to_purchases, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name="customer",
            name="purchased_cards",
        ),
    ]
