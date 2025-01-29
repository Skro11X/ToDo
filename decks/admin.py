from django.contrib import admin
from decks import models

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Deck)
class ModelNameAdmin(admin.ModelAdmin):
    pass
