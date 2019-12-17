from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime
from .serializers import CardSerializer


class CardViewSet(viewsets.ViewSet):
    parser_class = (FileUploadParser,)

    def create(self, request):
        card_serializer = CardSerializer(data=request.data)

        if card_serializer.is_valid():
            card_serializer.save(published_date=datetime.now())
            return Response(card_serializer.data, status=status.HTTP_201_CREATED)
        return Response(card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
