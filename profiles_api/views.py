from curses import noecho
from email import message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .import serializers

class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        an_apiview = [
            'Usamos method http',
            'Es similar a una vista tradicional',
            'Da mayor control sobre logica de programacion',
        ]
        context = {
            'message': 'hello',
            'an_apiview' : an_apiview
        }
        return Response(context)

    def post(self, request):
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello' +' '+ name

            context= {
                'message': message
            }

            return Response(context)
        else:
            context = {
                'error' : serializers.error,
                'status' : status.HTTP_400_BAD_REQUEST
            }
            return Response(context)


    def put(self, request, pk=None):
        return Response({'method' : 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method' : 'patch'})

    def delete(self, request, pk=None):
        return Response({'method' : 'delete'})



