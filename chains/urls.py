from django.urls import path

from chains.apps import ChainsConfig
from chains.views import (ProductListApiView, ProductRetrieveApiView, ProductCreateApiView, ProductUpdateApiView,
                          ProductDestroyApiView, ManufacturerListApiView, ManufacturerRetrieveApiView,
                          ManufacturerCreateApiView, ManufacturerUpdateApiView, ManufacturerDestroyApiView)

app_name = ChainsConfig.name

urlpatterns = [
    # CRUD Product
    path("products/", ProductListApiView.as_view(), name="products_list"),
    path("products/<int:pk>/", ProductRetrieveApiView.as_view(), name="product_retrieve"),
    path("products/create/", ProductCreateApiView.as_view(), name="product_create"),
    path("products/<int:pk>/update/", ProductUpdateApiView.as_view(), name="product_update"),
    path("products/<int:pk>/delete/", ProductDestroyApiView.as_view(), name="product_delete"),

    # CRUD Manufacturer
    path("manufacturers/", ManufacturerListApiView.as_view(), name="manufacturers_list"),
    path("manufacturers/<int:pk>/", ManufacturerRetrieveApiView.as_view(), name="manufacturer_retrieve"),
    path("manufacturers/create/", ManufacturerCreateApiView.as_view(), name="manufacturer_create"),
    path("manufacturers/<int:pk>/update/", ManufacturerUpdateApiView.as_view(), name="manufacturer_update"),
    path("manufacturers/<int:pk>/delete/", ManufacturerDestroyApiView.as_view(), name="manufacturer_delete"),
]
