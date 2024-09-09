from rest_framework import serializers

from chains.models import Manufacturer, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'product_model', 'release_date', 'manufacturer')


class ManufacturerSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    level_chains = serializers.IntegerField(source='get_level_chains')

    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'email', 'country', 'city', 'street', 'house_number', 'product', 'supplier', 'debt',
                  'creation_time', 'type', 'level_chains')

        read_only_fields = ('debt',)
