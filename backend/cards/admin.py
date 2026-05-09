from django.contrib import admin

from .models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "annotation", "price", "discount")
    search_fields = ("annotation", "description")
    list_filter = ("discount",)
