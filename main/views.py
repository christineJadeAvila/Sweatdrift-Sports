<<<<<<< HEAD
from django.shortcuts import render, redirect
from .models import Item
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):
    items = Item.objects.all()
    context = {
        'items' : items,
    }

    return render(request, 'main/home.html', context)

def cart(request, item_price, item_stocks): 
        return item_price - item_stocks
        # it has to be stocks minus qty, per item added in cart by user

=======
from django.shortcuts import render, redirect
from .models import Item
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):
    items = Item.objects.all()
    context = {
        'items' : items,
    }

    return render(request, 'main/home.html', context)

def cart(request, item_price, item_stocks): 
        return item_price - item_stocks
        # it has to be stocks minus qty, per item added in cart by user

>>>>>>> daad950f9bf9918ace52347581126bf4060fc0af
