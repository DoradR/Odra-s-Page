from django.shortcuts import render
from .models import Match


def main_page(request):
    return render(request, 'stronaglowna.html')


def matches_page(request):
    matches = Match.objects.all()
    return render(request, 'mecze.html', {'mecze': matches})
