from rest_framework import viewsets, generics
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .serializers import CardSerializer
from .models import Card
from dam.models import Dam
from user.models import User
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
import cloudinary.uploader


class CardViewSet(viewsets.ViewSet, generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [AllowAny]
    parser_class = (FileUploadParser,)
    queryset = Card.objects.filter()
    serializer_class = CardSerializer

    def list(self, request):
        queryset = Card.objects.all()
        serializer = CardSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Card.objects.filter(pk=pk)
        card = generics.get_object_or_404(queryset, pk=pk)
        serializer = CardSerializer(card)
        return Response(serializer.data)

    def create(self, request):
        context = {
            "request": self.request,
        }
        serializer = CardSerializer(data=request.data, context=context)

        if serializer.is_valid():
            response_from_cloudinary = cloudinary.uploader.upload(request.FILES.get('file').read(), folder='udc-dam')
            current_user = User.objects.get(name=request.data.get('username'))
            dam_record = Dam.objects.get(dam_code=request.data.get('dam_id'))
            serializer.save(
                user=current_user,
                dam=dam_record,
                cloudinary_url=response_from_cloudinary['url'],
                published_date=datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        response_from_cloudinary = cloudinary.uploader.upload(request.FILES.get('file').read(), folder='udc-dam')
        instance.cloudinary_url = response_from_cloudinary['url']
        instance.save()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
