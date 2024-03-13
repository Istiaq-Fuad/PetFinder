from django.db import models
from users.models import User
from django.utils import timezone
import uuid


class Pet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    age = models.IntegerField()
    SEX_CHOICES = [("M", "Male"), ("F", "Female")]
    gender = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    # gender = models.CharField(max_length=6)
    published = models.DateTimeField(default=timezone.now)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return self.name


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pet = models.ForeignKey(Pet, related_name="photos", on_delete=models.CASCADE)
    photo_url = models.URLField()
    is_primary = models.BooleanField(default=False)
