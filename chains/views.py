from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from chains.models import Product, Manufacturer

from chains.serializers import ProductSerializer, ManufacturerSerializer
from users.permissions import IsActiveStaff


class ProductCreateApiView(CreateAPIView):
    """Create a new Product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActiveStaff,)


class ProductListApiView(ListAPIView):
    """List of Products"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActiveStaff,)


class ProductRetrieveApiView(RetrieveAPIView):
    """Get one Product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActiveStaff,)


class ProductUpdateApiView(UpdateAPIView):
    """Update Product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActiveStaff,)


class ProductDestroyApiView(DestroyAPIView):
    """Delete Product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActiveStaff,)


class ManufacturerCreateApiView(CreateAPIView):
    """Create a new Manufacturer"""
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = (IsActiveStaff,)


class ManufacturerListApiView(ListAPIView):
    """List of Manufacturers"""
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("country",)
    permission_classes = (IsActiveStaff,)


class ManufacturerRetrieveApiView(RetrieveAPIView):
    """Get one Manufacturer"""
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = (IsActiveStaff,)


class ManufacturerUpdateApiView(UpdateAPIView):
    """Update Manufacturer"""
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = (IsActiveStaff,)


class ManufacturerDestroyApiView(DestroyAPIView):
    """Delete Manufacturer"""
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = (IsActiveStaff,)
