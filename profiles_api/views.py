from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API view """
    serializer_class = serializers.HelloSerializer

    """Test API view """
    def get(self, request, format = None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else: return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def put(self, response, pk=None):
        """Handles put request"""
        return Response({'method': 'PUT'})

    def patch(self, response, pk=None):
        """Handles Patch request"""
        return Response({'method': 'PATCH'})

    def delete(self, response, pk=None):
        """Handles put request"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API vivewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Maps to urls using routers',
            ]
        return Response({'message':'Hello', 'a_viewset':a_viewset})

    def post(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else: return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, response, pk=None):
        """Return object by id"""
        return Response({'method': 'GET'})


    def update(self, response, pk=None):
        """Handles updating object"""
        return Response({'method': 'PUT'})

    def partial_update(self, response, pk=None):
        """Handles partial updating object"""
        return Response({'method': 'PATCH'})

    def destroy(self, response, pk=None):
        """Handles removing object"""
        return Response({'method': 'DELETE'})
