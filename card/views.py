from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .serializers import CardSerializer
from .models import Card, Dam
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
import cloudinary.uploader

class CardViewSet(viewsets.ViewSet):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [AllowAny]
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
            response_from_cloudinary = cloudinary.uploader.upload(request.FILES.get('file').read(), folder='udc-dam')
            dam_record = Dam.objects.filter(dam_code=request.data.get('dam_id'))
            serializer.save(
                user=request.user,
                dam=dam_record[0],
                cloudinary_url=response_from_cloudinary['url'],
                published_date=datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
