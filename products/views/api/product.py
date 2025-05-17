from adrf.views import APIView
from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import sync_to_async
from drf_spectacular.utils import extend_schema
import products.repositories.product as product_repository
from products.serializers import ProductSerializer

# Product Views
@extend_schema(tags=["Products"])
class ProductAPIView(APIView):
    @extend_schema(
        summary="List all products",
        description="Returns a list of all products with associated categories and keywords",
        responses={200: ProductSerializer(many=True)}
    )
    async def get(self, request):
        data = await sync_to_async(product_repository.get_all)()
        return Response(data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Create a new product",
        description="Creates a new product with the provided data",
        request=ProductSerializer,
        responses={201: ProductSerializer}
    )
    async def post(self, request):
        data = await sync_to_async(product_repository.create)(request.data)
        return Response(data, status=status.HTTP_201_CREATED)


@extend_schema(tags=["Products"])
class ProductDetailAPIView(APIView):

    @extend_schema(
        summary="Get a specific product",
        description="Returns details of a specific product by ID",
        responses={200: ProductSerializer}
    )
    async def get(self, request, pk):
        data = await sync_to_async(product_repository.get)(pk)
        return Response(data)

    @extend_schema(
        summary="Update a product",
        description="Partially updates a product with the provided data, using optimistic locking",
        request=ProductSerializer,
        responses={200: ProductSerializer}
    )
    async def patch(self, request, pk):
        data = await sync_to_async(product_repository.update)(pk, request.data)
        return Response(data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Delete a product",
        description="Deletes a specific product by ID",
        responses={204: None}
    )
    async def delete(self, request, pk):
        await sync_to_async(product_repository.delete)(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
