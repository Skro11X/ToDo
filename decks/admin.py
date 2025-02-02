from django.contrib import admin
from decks import models

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('label',)}

@admin.register(models.Deck)
class ModelNameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
