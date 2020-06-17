from django.shortcuts import render, redirect
from rest_framework.views import APIView

# Create your views here.


def home(request):
    return render(request, 'app/home.html')
