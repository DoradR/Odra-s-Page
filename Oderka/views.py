import operator

from django.shortcuts import render, get_object_or_404
from .models import Match, Details, PicturesOfMatch, Club, Player, Table, Season


def main_page(request):
    club = Club.objects.all()
    return render(request, 'stronaglowna.html', {'club': club})


def main_matches_page(request):
    seasons = Season.objects.all().order_by('season').reverse()
    return render(request, 'main_matches.html', {'seasons': seasons})


def matches_page(request, id):
    seasons = get_object_or_404(Season, pk=id)
    mecze = Match.objects.filter(season=seasons)
    sortMecze = sorted(mecze, key=operator.attrgetter('date'),reverse=True)
    table = Table.objects.filter(season=seasons)
    sortTable = sorted(table, key=operator.attrgetter('points'), reverse=True)
    season = Season.objects.all().order_by('season').reverse()
    which = seasons.season

    if request.method == "POST":
        seasons.objects.filter(id)

    return render(request, 'mecze.html', {'mecze': sortMecze, 'table': sortTable, 'season': season, 'which': which})


def wins_page(request, id):
    seasons = get_object_or_404(Season, pk=id)
    mecze = Match.objects.filter(season=seasons, result=2)
    sortMecze = sorted(mecze, key=operator.attrgetter('date'),reverse=True)
    table = Table.objects.filter(season=seasons)
    sortTable = sorted(table, key=operator.attrgetter('points'), reverse=True)
    season = Season.objects.all().order_by('season').reverse()
    which = seasons.season

    if request.method == "POST":
        seasons.objects.filter(id)

    return render(request, 'mecze.html', {'mecze': sortMecze, 'table': sortTable, 'season': season, 'which': which})


def draws_page(request, id):
    seasons = get_object_or_404(Season, pk=id)
    mecze = Match.objects.filter(season=seasons, result=3)
    sortMecze = sorted(mecze, key=operator.attrgetter('date'),reverse=True)
    table = Table.objects.filter(season=seasons)
    sortTable = sorted(table, key=operator.attrgetter('points'), reverse=True)
    season = Season.objects.all().order_by('season').reverse()
    which = seasons.season

    if request.method == "POST":
        seasons.objects.filter(id)

    return render(request, 'mecze.html', {'mecze': sortMecze, 'table': sortTable, 'season': season, 'which': which})


def loses_page(request, id):
    seasons = get_object_or_404(Season, pk=id)
    mecze = Match.objects.filter(season=seasons, result=1)
    sortMecze = sorted(mecze, key=operator.attrgetter('date'),reverse=True)
    table = Table.objects.filter(season=seasons)
    sortTable = sorted(table, key=operator.attrgetter('points'), reverse=True)
    season = Season.objects.all().order_by('season').reverse()
    which = seasons.season

    if request.method == "POST":
        seasons.objects.filter(id)

    return render(request, 'mecze.html', {'mecze': sortMecze, 'table': sortTable, 'season': season, 'which': which})


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
    clubs = Club.objects.all()
    return render(request, 'about.html', {'players': sortPlayers, 'clubs': clubs})
