from django.urls import path
from candy_shop.views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio/cakes/', cakes, name='cakes'),
    path('portfolio/cupcakes/', cupcakes, name='cupcakes'),
    path('portfolio/national_sweets/', national_sweets, name='national_sweets'),
    path('portfolio/donuts/', donuts, name='donuts'),
    path('services/', services, name='services'),
    path('contacts/', contacts, name='contacts'),
    path('user_registration/', user_registration, name='user_registration')
]