from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<int:pk>', views.view_photo, name='view-photo'),
    path('add/', views.add_photo, name='add-photo'),
]
