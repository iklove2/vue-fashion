from django.urls import path

from .views import api_description, cards_list

urlpatterns = [
    path("", api_description, name="api-description"),
    path("cards/", cards_list, name="cards-list"),
]
