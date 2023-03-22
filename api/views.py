from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})
