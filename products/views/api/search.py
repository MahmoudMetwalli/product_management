from asgiref.sync import sync_to_async
from adrf.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from products.serializers.product import ProductSerializer
from products.services.product import search_products_by_word

class SearchAPIView(APIView):
    @extend_schema(
        summary="Search for products",
        description="Searches products by query string, splitting into words and searching in Arabic or English fields based on language detection. Results are cached in Redis.",
        parameters=[
            OpenApiParameter(
                name="query",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                required=True,
                description="Search query string. Can contain multiple words to search for."
            ),
            OpenApiParameter(
                name="page",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                required=False,
                description="Page number for pagination. Default is 1."
            ),
            OpenApiParameter(
                name="page_size",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                required=False,
                description="Number of results per page. Default is 20."
            ),
            OpenApiParameter(
                name="similarity_threshold",
                type=OpenApiTypes.FLOAT,
                location=OpenApiParameter.QUERY,
                required=False,
                description="Threshold for similarity matching. Default is 0.3."
            ),
        ],
        responses={
            200: ProductSerializer(many=True),
            400: {"type": "object", "properties": {"error": {"type": "string"}}},
            404: {"type": "object", "properties": {"error": {"type": "string"}}}
        }
    )
    async def get(self, request):
        query = request.query_params.get('query', '').strip()
        page = int(request.query_params.get('page', 1))
        page_size = int(request.query_params.get('page_size', 20))
        similarity_threshold = float(request.query_params.get('similarity_threshold', 0.3))
        if not query:
            return Response(
                {"error": "Query parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Split query into words
        words = query.split()

        if not words:
            return Response(
                {"error": "Query contains no valid words"},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Combine results, removing duplicates by product ID
        combined_results = await sync_to_async(search_products_by_word)(words, page, page_size, similarity_threshold)
    
        if not combined_results:
            return Response(
                {"error": "No products found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(combined_results, status=status.HTTP_200_OK)
