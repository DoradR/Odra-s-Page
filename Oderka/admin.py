from django.contrib import admin
from .models import Match, ResultOfMatch, Player, Club


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['opponent', 'odraGoal', 'opponentGoal']
    list_filter = ('opponent',)
    search_fields = ('opponent', 'date')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'secondName']
    list_filter = ('club',)
    search_fields = ('firstName', 'secondName')


@admin.register(Club)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['nameOfClub']
    search_fields = ('nameOfClub',)


admin.site.register(ResultOfMatch)
