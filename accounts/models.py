from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        null=True,
        blank=True
    )
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        verbose_name="n° de téléphone"
    )
    address = models.TextField(
        null=True,
        blank=True,
        verbose_name="adresse"
    )
