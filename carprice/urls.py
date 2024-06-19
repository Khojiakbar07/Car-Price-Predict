
from django.contrib import admin
from django.urls import include, path 
from home.views import *

urlpatterns = [
    path('admin123/', admin.site.urls),
    # path('main/',main, name='Interface'),
    path('about/' , about , name='About Page'),
    path('service/' , service , name='Service Page'),
    # path('carpredict/' , car_predict , name='Car Pricing Predict'),
    path('carlisting/' , carlisting , name='Car Listing Page'),
    path('contact/' , contact , name='Contact Page'),
    path('login/' , login , name='Login Page'),
    path('', car_predict, name='car_predict'),
]
