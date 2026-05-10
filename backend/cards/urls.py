from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CustomerViewSet, api_description, card_detail, cards_list

router = DefaultRouter()
router.register("customers", CustomerViewSet, basename="customer")

urlpatterns = [
    path("", api_description, name="api-description"),
    path("cards/", cards_list, name="cards-list"),
    path("cards/<int:pk>/", card_detail, name="card-detail"),
    path("", include(router.urls)),
]
