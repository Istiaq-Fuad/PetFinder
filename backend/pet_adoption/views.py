from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status


class LogoutView(APIView):
    """
    Django 5 does not have GET logout route anymore, so Django Rest Framework UI can't log out.
    This is a workaround until Django Rest Framework implements POST logout.
    Details: https://github.com/encode/django-rest-framework/issues/9206
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        logout(request)
        return redirect("/api/pets")


class HelloWorldView(APIView):
    def get(self, request):
        return Response("Hello world", status=status.HTTP_200_OK)
