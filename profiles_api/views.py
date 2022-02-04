from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
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
