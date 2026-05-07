from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Card
from .serializers import CardSerializer


@api_view(["GET"])
def api_description(request):
    return Response(
        {
            "message": "Django backend is running.",
            "endpoints": {
                "description": "/api/",
                "cards": "/api/cards/",
            },
        }
    )


@api_view(["GET"])
def cards_list(request):
    cards = Card.objects.all().order_by("id")
    serializer = CardSerializer(cards, many=True)
    return Response({"items": serializer.data})
