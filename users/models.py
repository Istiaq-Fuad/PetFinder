from django.db import models
import uuid
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _


class UserAccountManager(BaseUserManager):
    def create_superuser(self, email, name, password, **other_fields):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        return self.create_user(email, name, password, **other_fields)

    def create_user(self, email, name, password, **other_fields):

        if not email:
            raise ValueError(_("You must provide an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    # def create_user(self, email, name, password=None):
    #     if not email:
    #         raise ValueError("Users must have an email address")

    #     email = self.normalize_email(email)
    #     email = email.lower()

    #     user = self.model(email=email, name=name)

    #     user.set_password(password)
    #     user.save(using=self._db)

    #     return user

    # def create_shelter(self, email, name, password=None):
    #     user = self.create_user(email, name, password)

    #     user.is_shelter = True
    #     user.save(using=self._db)

    #     return user

    # def create_superuser(self, email, name, password=None):
    #     user = self.create_user(email, name, password)

    #     user.is_superuser = True
    #     user.is_staff = True

    #     user.save(using=self._db)

    #     return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    # password_hash = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # is_shelter = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserAccountManager()

    def __str__(self):
        return self.email
