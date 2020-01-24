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
from rest_framework.pagination import PageNumberPagination
import cloudinary.uploader
from django_filters import rest_framework as filters


class CardFilter(filters.FilterSet):
    user = filters.CharFilter(field_name='user__name')
    dam = filters.NumberFilter(field_name='dam__dam_code')

    class Meta:
        model = Card
        fields = ('user', 'dam')


class CardPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 12


class CardViewSet(viewsets.ViewSet, generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [AllowAny]
    parser_class = (FileUploadParser,)
    queryset = Card.objects.filter()
    serializer_class = CardSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CardFilter
    pagination_class = CardPagination

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        qs = self.filter_queryset(queryset)
        serializer = CardSerializer(qs, many=True)
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
