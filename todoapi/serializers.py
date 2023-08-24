from .models import todoItem
from rest_framework.serializers import ModelSerializer

class todoSerializer(ModelSerializer):
    class Meta:
        model = todoItem
        fields = '__all__'
