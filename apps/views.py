import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product


@api_view(['POST'])
def create_product(request):
    data = request.data
    Product.objects.create(
        name=data['name'],
        price=data['price'],
        description=data['description']
    )
    response = requests.post('http://localhost:3000/products', json=data)
    return Response({'status': 'n1 dan n2 ga go🏃'})
