from django.contrib import admin
from .models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'category', 'slug')
    prepopulated_fields = {'slug': ('title',), }
    search_fields = ('title', )
    save_as = True


class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',), }


class MovieCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(MovieCategory, MovieCategoryAdmin)
admin.site.register(MovieDirectorActor)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieComment)
admin.site.register(MovieGenre, MovieGenreAdmin)
