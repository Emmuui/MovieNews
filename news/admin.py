from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin


class MovieAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


class IframeVideoAdminForm(forms.ModelForm):
    link = forms.CharField(label='Ссылка на трейлер', widget=CKEditorUploadingWidget())

    class Meta:
        model = IframeVideo
        fields = '__all__'


@admin.register(MovieGenre)
class MovieGenreAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',), }


@admin.register(MovieCategory)
class MovieCategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',), }


@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    list_display = ('title', 'is_published', 'category', 'slug')
    prepopulated_fields = {'slug': ('title',), }
    search_fields = ('title', )
    list_filter = ('category', 'genre', 'premieredate',)
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
            'fields': (('age', 'country', 'premieredate'), )
        }),
        (None, {
            'fields': (('awards', 'budget', 'is_published'), )
        }),
        ('Описание', {
            'fields': ('description', 'iframe')
        }),
    )


@admin.register(IframeVideo)
class IframeVideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    form = IframeVideoAdminForm


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(TranslationAdmin):
    list_display = ('title', 'movie')


@admin.register(MovieDirectorActor)
class MovieDirectorActorAdmin(TranslationAdmin):
    list_display = ('name', 'slug')