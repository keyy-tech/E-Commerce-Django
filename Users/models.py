import random
import string
from django.contrib.auth.models import AbstractUser
from django.db import models


def generate_unique_user_id():
    """Generate a random alphanumeric user ID."""
    characters = string.ascii_letters + string.digits  # Letters (both cases) and digits
    user_id = "".join(random.choice(characters) for i in range(10))
    return user_id


class CustomUser(AbstractUser):
    user_id = models.CharField(
        max_length=50, unique=True, default=generate_unique_user_id, editable=False
    )
    username = models.CharField(max_length=255, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = "email"  # Use email as the unique identifier
    REQUIRED_FIELDS = []  # Remove username from required fields

    def __str__(self):
        return self.email


def default_profile_picture():
    return "profile_pictures/default.png"


class UsersProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE
    )  # Link to CustomUser

    profile_picture = models.ImageField(
        upload_to="profile_pictures", blank=True, default=default_profile_picture
    )
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
