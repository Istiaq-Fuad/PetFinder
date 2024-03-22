from rest_framework.views import APIView
from .models import Application
from .serializers import ApplicationSerializer, ApplicationPatchSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework import generics

# from rest_framework import authentication, permissions
from rest_framework import status


class ApplicationListCreate(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ApplicationSerializer

    def get(self, request, format=None):
        applications = Application.objects.filter(user=request.user)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ApplicationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {"message": "Application created successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class ApplicationGetDelete(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ApplicationSerializer

    def get_object(self, request, pk):
        try:
            application = Application.objects.get(id=pk)
            if application.user == request.user or application.pet.user == request.user:
                return application
            raise PermissionDenied
        except Application.DoesNotExist:
            raise NotFound

    def get(self, request, pk, format=None):
        application = self.get_object(request, pk)
        serializer = ApplicationSerializer(application)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        application = self.get_object(request, pk)
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk, format=None):
        application = self.get_object(request, pk)
        if application.pet.user == request.user:
            serializer = ApplicationPatchSerializer(
                application, data=request.data, partial=True
            )

            if serializer.is_valid():
                # print("modified")
                serializer.save()
                return Response(serializer.data)

        return Response(
            {"message": "there was some problem updating the data"},
            status=status.HTTP_400_BAD_REQUEST,
        )
