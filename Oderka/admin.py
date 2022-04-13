from django.contrib import admin
from .models import Match, ResultOfMatch

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['opponent', 'odraGoal', 'opponentGoal']
    list_filter = ('opponent',)
    search_fields = ('opponent', 'date')

admin.site.register(ResultOfMatch)
