from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from restaurants import views

urlpatterns = []

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', views.RestaurantListView.as_view(),
         name='restaurant-list'),
    path('restaurant_list', views.RestaurantListView.as_view(),
         name='restaurant-list'),
    path('restaurant/details/<restaurant_id>', views.RestaurantDetailsView.as_view(),
         name='restaurant-details'),
    path('api/restaurant-list/<city>/<street>', views.GetRestaurantListAPIView.as_view(),
         name='api-restaurant-list')
)
