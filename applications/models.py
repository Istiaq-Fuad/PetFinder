from django.db import models
from users.models import User
from pets.models import Pet
import uuid


# Create your models here.
class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="PENDING")
    pet_experience = models.TextField()
    house_condition = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
