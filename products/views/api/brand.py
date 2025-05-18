from adrf.views import APIView
from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import sync_to_async
from drf_spectacular.utils import extend_schema
import products.services.brand as brand_service
from products.serializers.brand import BrandSerializer


# Category Views
@extend_schema(tags=["Brands"])
class BrandAPIView(APIView):
    @extend_schema(
        summary="List all brands",
        description="Returns a list of all product brands",
        responses={200: BrandSerializer(many=True)}
    )
    async def get(self, request):
        data = await sync_to_async(brand_service.get_all)()
        return Response(data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Create a new brand",
        description="Creates a new product brand",
        request=BrandSerializer,
        responses={201: BrandSerializer}
    )
    async def post(self, request):
        data = await sync_to_async(brand_service.create)(request.data)
        return Response(data, status=status.HTTP_201_CREATED)


@extend_schema(tags=["Brands"])
class BrandDetailAPIView(APIView):

    @extend_schema(
        summary="Get a specific brand",
        responses={200: BrandSerializer}
    )
    async def get(self, request, pk):
        data = await sync_to_async(brand_service.get)(pk)
        return Response(data)

    @extend_schema(
        summary="Update a brand",
        request=BrandSerializer,
        responses={200: BrandSerializer}
    )
    async def patch(self, request, pk):
        data = await sync_to_async(brand_service.update)(pk, request.data)
        return Response(data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Delete a brand",
        responses={204: None}
    )
    
    async def delete(self, request, pk):
        await sync_to_async(brand_service.delete)(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
