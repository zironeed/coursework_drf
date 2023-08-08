from rest_framework.response import Response
from rest_framework.views import APIView

from users.users_serializers import UserSerializer, UserRegisterSerializer


class UserRegisterView(APIView):

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'message': 'User registered successfully'}, status=201)

        return Response(serializer.errors, status=400)

