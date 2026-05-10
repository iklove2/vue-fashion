from django.contrib import admin

from .models import Card, Customer, CustomerCardPurchase


class CustomerCardPurchaseInline(admin.TabularInline):
    model = CustomerCardPurchase
    extra = 0


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "phone")
    search_fields = ("first_name", "last_name", "email", "phone")
    inlines = (CustomerCardPurchaseInline,)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "annotation", "price", "discount")
    search_fields = ("annotation", "description")
    list_filter = ("discount",)
