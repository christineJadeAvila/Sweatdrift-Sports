<<<<<<< HEAD
from rest_framework.serializers import ModelSerializer
from main.models import Item

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
=======
from rest_framework.serializers import ModelSerializer
from main.models import Item

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
>>>>>>> daad950f9bf9918ace52347581126bf4060fc0af
        fields = '__all__'