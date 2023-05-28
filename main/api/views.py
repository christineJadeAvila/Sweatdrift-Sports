<<<<<<< HEAD
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Item
from .serializers import ItemSerializer
from main.api import serializers

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/items',
        'GET /api/items/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getItems(request):
    items = Item.objects.all()
    serializers = ItemSerializer(items, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getItem(request, pk):
    item = Item.objects.get(id=pk)
    serializers = ItemSerializer(item, many=False)
=======
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Item
from .serializers import ItemSerializer
from main.api import serializers

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/items',
        'GET /api/items/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getItems(request):
    items = Item.objects.all()
    serializers = ItemSerializer(items, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getItem(request, pk):
    item = Item.objects.get(id=pk)
    serializers = ItemSerializer(item, many=False)
>>>>>>> daad950f9bf9918ace52347581126bf4060fc0af
    return Response(serializers.data)