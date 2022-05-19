import operator

from django.shortcuts import render, get_object_or_404
from .models import Match, Details, PicturesOfMatch, Club, Player


def main_page(request):
    return render(request, 'stronaglowna.html')


def matches_page(request):
    matches = Match.objects.all()
    sort = sorted(matches, key=operator.attrgetter('date'), reverse=True)
    return render(request, 'mecze.html', {'mecze': sort})


def details_page(request, id):
    match = get_object_or_404(Match, pk=id)
    details = Details.objects.filter(match=match)
    sortDetails = sorted(details, key=operator.attrgetter('minute'))
    pictures = PicturesOfMatch.objects.filter(match=match)
    matches = Club.objects.filter(match=match)
    comment = match.comment
    result = match.result
    odraGoal = match.odraGoal
    opponent = match.opponent
    opponentGoal = match.opponentGoal
    players = Player.objects.all()

    if request.method == "POST":
        match.objects.filter(id)

    return render(request, 'detale.html', {'detale': sortDetails, 'comment': comment, 'pictures': pictures, 'result': result,
                                           'matches': matches, 'odraGoal': odraGoal, 'opponent': opponent,
                                           'opponentGoal': opponentGoal, 'players': players})


def help_page(request):
    return render(request, 'kontakt.html')


def about_page(request):
    players = Player.objects.all()
    sortPlayers = sorted(players, key=operator.attrgetter('secondName'))
    return render(request, 'about.html', {'players': sortPlayers})
