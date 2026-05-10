from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Card, Customer
from .serializers import CardSerializer, CustomerSerializer


@api_view(["GET"])
def api_description(request):
    return Response(
        {
            "message": "Django backend is running.",
            "endpoints": {
                "description": "/api/",
                "cards_collection": "/api/cards/",
                "cards_item": "/api/cards/<id>/",
                "customers_collection": "/api/customers/",
                "customers_item": "/api/customers/<id>/",
            },
        }
    )


@api_view(["GET", "POST"])
def cards_list(request):
    if request.method == "POST":
        serializer = CardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    cards = Card.objects.all().order_by("id")
    serializer = CardSerializer(cards, many=True)
    return Response({"items": serializer.data})


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def card_detail(request, pk):
    card = get_object_or_404(Card, pk=pk)

    if request.method == "GET":
        serializer = CardSerializer(card)
        return Response(serializer.data)

    if request.method in ["PUT", "PATCH"]:
        partial = request.method == "PATCH"
        serializer = CardSerializer(card, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    card.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.prefetch_related(
        "card_purchases",
        "card_purchases__card",
    ).all()
    serializer_class = CustomerSerializer
