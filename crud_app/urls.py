from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('create/', views.create, name="create"),
    path('store/', views.store, name="store"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
]