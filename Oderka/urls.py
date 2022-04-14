from django.urls import path
from .views import main_page, matches_page

urlpatterns = [
    path('main/', main_page),
    path('matches/', matches_page)
]