from django.urls import path
from .views import main_page, matches_page, details_page, help_page, about_page, main_matches_page, wins_page, draws_page, loses_page

urlpatterns = [
    path('front/', main_page, name="main_page"),
    path('seazones/', main_matches_page, name="main_matches_page"),
    path('seazones/<int:id>/matches/', matches_page, name="matches_page"),
    path('seazones/<int:id>/matches/wins/', wins_page, name="wins_page"),
    path('seazones/<int:id>/matches/draws/', draws_page, name="draws_page"),
    path('seazones/<int:id>/matches/loses/', loses_page, name="loses_page"),
    path('details/<int:id>/', details_page, name="details_page"),
    path('help/', help_page, name="help_page"),
    path('about/', about_page, name="about_page")
]
