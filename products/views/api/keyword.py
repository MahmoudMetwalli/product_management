from adrf.views import APIView
from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import sync_to_async
from drf_spectacular.utils import extend_schema
import products.repositories.keyworrd as keyword_repository
from products.serializers import KeywordSerializer


# Keyword Views
@extend_schema(tags=["Keywords"])
class KeywordAPIView(APIView):
    @extend_schema(
        summary="List all keywords",
        responses={200: KeywordSerializer(many=True)}
    )
    async def get(self, request):
        data = await sync_to_async(keyword_repository.get_all)()
        return Response(data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Create a new keyword",
        request=KeywordSerializer,
        responses={201: KeywordSerializer}
    )
    async def post(self, request):
        data = await sync_to_async(keyword_repository.create)(request.data)
        return Response(data, status=status.HTTP_201_CREATED)

@extend_schema(tags=["Keywords"])
class KeywordDetailAPIView(APIView):

    @extend_schema(
        summary="Get a specific keyword",
        responses={200: KeywordSerializer}
    )
    async def get(self, request, pk):
        data = await sync_to_async(keyword_repository.get)(pk)
        return Response(data)

    @extend_schema(
        summary="Update a keyword",
        request=KeywordSerializer,
        responses={200: KeywordSerializer}
    )
    async def patch(self, request, pk):
        data = await sync_to_async(keyword_repository.update)(pk, request.data)
        return Response(data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Delete a keyword",
        responses={204: None}
    )
    async def delete(self, request, pk):
        await sync_to_async(keyword_repository.delete)(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
