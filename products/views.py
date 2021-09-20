from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Products
from .serializers import ProductSerializer


class ProductsListApiView(APIView):

    def get(self, request):
        product = Products.objects.all()
        serializers = ProductSerializer(product, many=True)
        return Response(serializers.data)

