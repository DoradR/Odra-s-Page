from django.shortcuts import render, get_object_or_404
from .models import Match, Details, PicturesOfMatch, Club


def main_page(request):
    return render(request, 'stronaglowna.html')


def matches_page(request):
    matches = Match.objects.all()
    return render(request, 'mecze.html', {'mecze': matches})


def details_page(request, id):
    match = get_object_or_404(Match, pk=id)
    details = Details.objects.filter(match=match)
    comment = match.comment
    pictures = PicturesOfMatch.objects.filter(match=match)
    matches = Club.objects.filter(match=match)
    result = match.result
    odraGoal = match.odraGoal
    opponent = match.opponent
    opponentGoal = match.opponentGoal

    if request.method == "POST":
        match.objects.filter(id)

    return render(request, 'detale.html', {'detale': details, 'comment': comment, 'pictures': pictures, 'result': result,
                                           'matches': matches, 'odraGoal': odraGoal, 'opponent': opponent, 'opponentGoal': opponentGoal})


def help_page(request):
    return render(request, 'kontakt.html')


def about_page(request):
    return render(request, 'about.html')
