from django.db import models
from django.conf import settings

# Create your models here.


class UserProfile(models.Model):
    roles = (
        ('buyer', 'buyer'),
        ('seller', 'seller'),
    )

    amounts = (
        (5, 5),
        (10, 10),
        (20, 20),
        (50, 50),
        (100, 100),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    deposit = models.IntegerField(default=0, choices=amounts)
    role = models.CharField(max_length=50, choices=roles)
