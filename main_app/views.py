from django.shortcuts import render

# Create your views here.
# Add the following import
from django.http import HttpResponse
from .models import Cafe

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cafes_index(request):
  cafes = Cafe.objects.all()
  return render(request, 'cafes.html', {'cafes': cafes})

