from rest_framework import serializers
from oscar.core.loading import get_model

Category = get_model('catalogue', 'Category')

class categorie_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "description")
