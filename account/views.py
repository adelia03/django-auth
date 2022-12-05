from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .models import User
from .serializers import RegisterUserSerializer


class RegisterUserView(APIView):
    @swagger_auto_schema(request_body=RegisterUserSerializer())
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Вы успешно зарегистрировались", status=201)
    

class DeleteUserView(APIView):
    def delete(self, request, email):
        user = get_object_or_404(User, email=email)
        if user.is_staff:
            return Response(status=403) #запрещаем
        user.delete()
        return Response(status=204)
