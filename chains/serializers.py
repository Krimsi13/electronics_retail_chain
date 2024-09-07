from rest_framework import serializers

from chains.models import Manufacturer, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'product_model', 'release_date', 'manufacturer')


class ManufacturerSerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'email', 'country', 'city', 'street', 'house_number', 'products', 'supplier', 'debt',
                  'creation_time')

        read_only_fields = ('debt',)
