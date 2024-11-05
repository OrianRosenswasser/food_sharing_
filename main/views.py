from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, FoodPostForm, RequestForm
from .models import FoodPost
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('food_feed')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def food_feed(request):
    food_posts = FoodPost.objects.all()
    return render(request, 'main/food_feed.html', {'food_posts': food_posts})

@login_required
def post_food(request):
    if request.method == 'POST':
        form = FoodPostForm(request.POST, request.FILES)
        if form.is_valid():
            food_post = form.save(commit=False)
            food_post.donor = request.user
            food_post.save()
            return redirect('food_feed')
    else:
        form = FoodPostForm()
    return render(request, 'main/post_food.html', {'form': form})

@login_required
def request_food(request, food_post_id):
    food_post = get_object_or_404(FoodPost, id=food_post_id)
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            request_instance = form.save(commit=False)
            request_instance.recipient = request.user
            request_instance.food_post = food_post
            request_instance.save()
            return redirect('food_feed')
    else:
        form = RequestForm()
    return render(request, 'main/request_food.html', {'form': form, 'food_post': food_post})

def home(request):
    return render(request, 'main/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('food_feed')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})