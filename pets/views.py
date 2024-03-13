from rest_framework import generics
from .models import Pet
from .serializers import PetSerializer
from .permissions import PetsWritePermission
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from applications.serializers import ApplicationSerializer
from applications.models import Application
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from users.models import User
from django.http import Http404
from rest_framework import status


class PetListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def perform_create(self, PetSerializer):
        PetSerializer.save(user=self.request.user)


class PetDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [PetsWritePermission]
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDetailApplicationView(APIView):
    serializer_class = ApplicationSerializer

    def get(self, request, pk, format=None):
        try:
            pet = Pet.objects.get(id=pk)
            if pet.user == request.user:
                applications = Application.objects.filter(pet_id=pk)
                serializer = ApplicationSerializer(applications, many=True)
                return Response(serializer.data)
            return Response(
                {"message": "not allowed"}, status=status.HTTP_403_FORBIDDEN
            )

        except:
            raise NotFound

    
