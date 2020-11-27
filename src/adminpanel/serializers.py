from rest_framework import serializers
from .models import Products

class AdminSerializer(serializers.ModelSerializer):
  class Meta:
    model = Products
    fields = ('product_name', 'product_image', 'product_isAvailable', 'product_quantity', 'product_updated')