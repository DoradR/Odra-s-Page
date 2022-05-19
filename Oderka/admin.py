from django.contrib import admin
from .models import Match, ResultOfMatch, Player, Club, Details, PicturesOfMatch, TypeOfDetails, Season


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_filter = ('opponent',)
    search_fields = ('opponent', 'date')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'secondName']
    list_filter = ('club',)
    search_fields = ('firstName', 'secondName')


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['nameOfClub']
    search_fields = ('nameOfClub',)


@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ['type', 'who', 'minute']
    list_filter = ('who', 'type')
    search_fields = ('minute',)


@admin.register(PicturesOfMatch)
class PicturesOfMatchAdmin(admin.ModelAdmin):
    list_display = ['pictures', 'match']
    list_filter = ('match',)


admin.site.register(ResultOfMatch)
admin.site.register(TypeOfDetails)
admin.site.register(Season)
