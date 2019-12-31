from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .serializers import CardSerializer
from .models import Card
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CardViewSet(viewsets.ViewSet):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_class = (FileUploadParser,)
    http_method_names = ['post']

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
            serializer.save(
                user=request.user,
                published_date=datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
