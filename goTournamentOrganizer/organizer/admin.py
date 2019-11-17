from django.contrib import admin

# Register your models here.

from .models import Tournament, Participants, RuleSet, Games

admin.site.register(Tournament)
admin.site.register(Participants)
admin.site.register(RuleSet)
admin.site.register(Games)