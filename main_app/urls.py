from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cafes/', views.cafes_index, name='cafes'),
  path('cafes/<int:cafes_id>/', views.cafes_detail, name='detail'),
  path('cafes/create/', views.CafeCreate.as_view(), name='cafes_create'),
  path('cafes/<int:pk>/update/', views.CafeUpdate.as_view(), name='cafes_update'),
  path('cafes/<int:pk>/delete/', views.CafeDelete.as_view(), name='cafes_delete'),


]