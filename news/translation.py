from modeltranslation.translator import register, TranslationOptions
from .models import MovieCategory, MovieGenre, MovieDirectorActor, Movie, PhotoGallery


@register(MovieCategory)
class MovieCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(MovieGenre)
class MovieGenreTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(MovieDirectorActor)
class MovieDirectorActorTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('title', 'tagline',
              'country', 'awards',
              'description')


@register(PhotoGallery)
class PhotoGalleryTranslationOptions(TranslationOptions):
    fields = ('title', )
