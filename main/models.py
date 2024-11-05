# main/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('donor', 'Donor'),
        ('recipient', 'Recipient'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, blank=True, null=True)

class FoodPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='food_photos/', blank=True, null=True)
    expiration_date = models.DateField()
    contact_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=15)
    donor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
class Request(models.Model):
    food_post = models.ForeignKey(FoodPost, on_delete=models.CASCADE)
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)