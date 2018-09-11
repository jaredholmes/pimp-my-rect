from rest_framework.serializers import ModelSerializer

from .models import Rectangle

class RectangleSerializer(ModelSerializer):
    class Meta:
        model = Rectangle
        fields = '__all__'
