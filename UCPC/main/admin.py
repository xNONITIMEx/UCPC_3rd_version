from django.contrib import admin

from .models import Cards, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created']

    class Meta:
        model =  Tag

class CardsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'get_tags']

    search_fields = ['title', 'desc', 'author']
    list_filter = ['tags', 'author']

    class Meta:
        model = Cards

admin.site.register(Cards, CardsAdmin)
admin.site.register(Tag, TagAdmin)