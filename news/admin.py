from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'category', 'slug')
    prepopulated_fields = {'slug': ('title',), }
    search_fields = ('title', )
    list_filter = ('category', 'genre', 'release_date',)
    save_as = True
    list_editable = ('is_published', )
    form = MovieAdminForm
    fieldsets = (
        (None, {
            'fields': (('title', 'title_eng', 'slug'), )
        }),
        (None, {
            'fields': (('image', 'tagline'), )
        }),
        (None, {
            'fields': (('director', 'actor'), )
        }),
        (None, {
            'fields': (('genre', 'category'), )
        }),
        (None, {
            'fields': (('age', 'country', 'premiere_date'), )
        }),
        (None, {
            'fields': (('awards', 'budget', 'is_published'), )
        }),
        ('Описание', {
            'fields': ('description', )
        }),
    )


class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',), }


class MovieCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(MovieCategory, MovieCategoryAdmin)
admin.site.register(MovieDirectorActor)
admin.site.register(Movie, MovieAdmin)
admin.site.register(IframeVideo)
admin.site.register(MovieComment)
admin.site.register(MovieGenre, MovieGenreAdmin)
