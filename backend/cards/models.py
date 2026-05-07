from django.db import models


class Card(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.TextField(help_text="Bitmap encoded as base64.")
    annotation = models.CharField(max_length=255)
    description = models.TextField()
    discount = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"Card #{self.pk}: {self.annotation}"
