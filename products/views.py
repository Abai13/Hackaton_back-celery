from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from products.filters import ProductPriceFilter
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema 
from rest_framework.decorators import action

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter 

from .models import Product, CommentRating, Category, Brand, Like, Favorites #Image
from .serializers import ProductSerializer, ReviewSerializer, BrandSerializer, CategorySerializer, LikeSerializer, FavoritesSerializer #ImageSerializer
from .permissions import IsAuthor

from products.filters import ProductPriceFilter

@swagger_auto_schema(request_body=ProductSerializer)
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description']
    filterset_class = ProductPriceFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ['destroy', 'update', 'partial_update', 'create']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

@swagger_auto_schema(request_body=ReviewSerializer)
class CommentViewSet(ModelViewSet):
    queryset = CommentRating.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAuthor]
        return super().get_permissions()

# @swagger_auto_schema(request_body=ImageSerializer)
# class ImageView(ModelViewSet):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ['destroy', 'update', 'partial_update', 'create']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

@swagger_auto_schema(request_body=CategorySerializer)
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ['destroy', 'update', 'partial_update', 'create']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()


@swagger_auto_schema(request_body=BrandSerializer)
class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ['destroy', 'update', 'partial_update', 'create']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()


@swagger_auto_schema(request_body=ProductSerializer)
class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


@swagger_auto_schema(request_body=ProductSerializer)
class FavoritesViewSet(ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer