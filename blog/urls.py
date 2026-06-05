"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from blogging import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.post_creation, name='post_creation'),
    path('edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
]