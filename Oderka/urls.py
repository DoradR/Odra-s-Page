from django.urls import path
from .views import main_page, matches_page, details_page, help_page, about_page, main_matches_page

urlpatterns = [
    path('front/', main_page, name="main_page"),
    path('seazones/', main_matches_page, name="main_matches_page"),
    path('matches/<int:id>/', matches_page, name="matches_page"),
    path('details/<int:id>/', details_page, name="details_page"),
    path('help/', help_page, name="help_page"),
    path('about/', about_page, name="about_page")
]
