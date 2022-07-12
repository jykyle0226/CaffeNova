from django.shortcuts import render
from django.http import HttpResponse
from .models import Cafe
from django.shortcuts import render
from .models import Cafe
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cafes_index(request):
  cafes = Cafe.objects.all()
  return render(request, 'cafes/index.html', {'cafes': cafes})

def cafes_detail(request, cafes_id):
  cafes = Cafe.objects.get(id=cafes_id)
  return render(request, 'cafes/detail.html', {'cafes': cafes})

class CafeCreate(CreateView):
  model = Cafe
  fields = '__all__'
  success_url = '/cafes/'

class CafeUpdate(UpdateView):
  model = Cafe
  fields = '__all__'
  success_url = '/cafes/'

class CafeDelete(DeleteView):
  model = Cafe
  success_url = '/cafes/'