from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Cafe
from django.shortcuts import render
from .models import Cafe
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
  return render(request, 'home.html')

@login_required
def allCafe(request):
  cafes = Cafe.objects.all()
  return render(request, 'allCafe.html', {'cafes': cafes})

@login_required
def cafes_index(request):
  cafes = Cafe.objects.filter(user=request.user)
  return render(request, 'cafes/index.html', {'cafes': cafes})

@login_required
def cafes_detail(request, cafes_id):
  cafes = Cafe.objects.get(id=cafes_id)
  return render(request, 'cafes/detail.html', {'cafes': cafes})



def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cafes')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
  


class CafeCreate(LoginRequiredMixin, CreateView):
  model = Cafe
  fields = '__all__'
  success_url = '/cafes/'
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CafeUpdate(LoginRequiredMixin, UpdateView):
  model = Cafe
  fields = '__all__'
  success_url = '/cafes/'

class CafeDelete(LoginRequiredMixin, DeleteView):
  model = Cafe
  success_url = '/cafes/'
