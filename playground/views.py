from typing import Collection
from django.shortcuts import render
from store.models import Product, OrderItem, Collection


def hello_world(request):
    collection = Collection()
    collection.title = 'Hello World'
    
    return render(request, 'index.html', {'name': 'Ajmal Muhammed'})