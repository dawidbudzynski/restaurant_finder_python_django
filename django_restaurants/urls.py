"""django_restaurants URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from restaurants import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.RestaurantList.as_view(),
         name='restaurant'),
    path('restaurant_list', views.RestaurantList.as_view(),
         name='restaurant'),
    path('restaurant/city_found=<city_not_found>', views.RestaurantList.as_view(),
         name='restaurant_not_found'),
    path('restaurant/details/<restaurant_id>', views.RestaurantDetails.as_view(),
         name='restaurant_details')
]
