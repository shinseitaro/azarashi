from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .serializers import CardSerializer
from .models import Card


class CardViewSet(viewsets.ViewSet):
    parser_class = (FileUploadParser,)

    def list(self, request):
        queryset = Card.objects.all()
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        context = {
            "request": self.request,
        }
        serializer = CardSerializer(data=request.data, context=context)

        if serializer.is_valid():
            serializer.save(published_date=datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
