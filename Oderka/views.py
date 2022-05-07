from django.shortcuts import render, get_object_or_404
from .models import Match, Details


def main_page(request):
    return render(request, 'stronaglowna.html')


def matches_page(request):
    matches = Match.objects.all()
    return render(request, 'mecze.html', {'mecze': matches})


def details_page(request, id):
    match = get_object_or_404(Match, pk=id)
    details = Details.objects.filter(match=match)

    if request.method == "POST":
        match.objects.filter(id)

    return render(request, 'detale.html', {'detale': details})
