from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, FoodPost, Request

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'user_type')

class FoodPostForm(forms.ModelForm):
    class Meta:
        model = FoodPost
        fields = ['title', 'description', 'photo', 'expiration_date', 'contact_name', 'contact_phone']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = []
