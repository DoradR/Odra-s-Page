from django.urls import path
from .views import main_page, matches_page, details_page

urlpatterns = [
    path('front/', main_page, name="main_page"),
    path('matches/', matches_page, name="matches_page"),
    path('details/<int:id>/', details_page, name="details_page")
]
