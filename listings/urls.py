from django.urls import path

from .views import index, listing, search

# app_name = 'listings'

urlpatterns = [

    path('', index, name='listings'),
    path('<int:listing_id>', listing, name='listing'),
    path('search/', search, name='search'),

]
