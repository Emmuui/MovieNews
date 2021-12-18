from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from datetime import date


class MovieCategory(models.Model):
    name = models.CharField(max_length=70, verbose_name='Категория')
    slug = models.SlugField(max_length=50, null=True, blank=True, unique=True, verbose_name='url')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class MovieGenre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Жанр')
    slug = models.SlugField(max_length=50, null=True, blank=True, unique=True, verbose_name='url')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class MovieDirectorActor(models.Model):
    name = models.CharField(max_length=70, verbose_name='Имя')
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True, verbose_name='url')
    image = models.ImageField(verbose_name='Фотография', upload_to='director_actor/', blank=True, null=True)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Актер и режиссер'
        verbose_name_plural = 'Актеры и режиссеры'

    def get_absolute_url(self):
        return reverse('director_actor_detail', args=[str(self.slug)])

    def __str__(self):
        return self.name


class IframeVideo(models.Model):
    name = models.ForeignKey('Movie', verbose_name='Имя фильма', max_length=50, null=True, on_delete=models.SET_NULL)
    link = models.TextField(verbose_name='Ссылка на трейлер')

    class Meta:
        verbose_name = 'Ссылка на трейлер'
        verbose_name_plural = 'Ссылки на трейлеры'

    def __str__(self):
        return self.name.title


class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название фильма')
    title_eng = models.CharField(max_length=50, verbose_name='Название фильма на англ', null=True, blank=True)
    tagline = models.CharField(max_length=300, verbose_name='Слоган', null=True, blank=True)
    director = models.ManyToManyField(MovieDirectorActor, max_length=50,
                                      verbose_name='Режиссер', related_name='movie_director')
    actor = models.ManyToManyField(MovieDirectorActor, max_length=50, verbose_name='Актеры', related_name='movie_actor')
    country = models.CharField(max_length=100, verbose_name='Страна', null=True)
    age = models.CharField(max_length=100, verbose_name='Возраст', null=True)
    awards = models.CharField(max_length=100, verbose_name='Награды фильма', null=True)
    premieredate = models.DateField(verbose_name='Дата премьеры', default=date.today, null=True)
    duration = models.IntegerField(verbose_name='Длительность(мин)', null=True)
    genre = models.ManyToManyField(MovieGenre, verbose_name='Жанр')
    category = models.ForeignKey(MovieCategory, verbose_name='Категория', null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True, verbose_name='url')
    image = models.ImageField(upload_to='movie_image/', verbose_name='Изображение')
    description = RichTextUploadingField(null=True, verbose_name='Описание')
    iframe = models.ForeignKey(IframeVideo, verbose_name='Трейлер', null=True, on_delete=models.SET_NULL)
    budget = models.PositiveIntegerField(verbose_name='Бюджет фильма', null=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-date_published']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', args=[str(self.slug)])

    def get_comment(self):
        return self.moviecomment_set.filter(parent__isnull=True)

    def get_four_item(self):
        return Movie.objects.all()[:4]


class PhotoGallery(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    image = models.ImageField(verbose_name='Фотография', upload_to='photo_gallery/')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class MovieComment(models.Model):
    email = models.EmailField(verbose_name='Email')
    username = models.CharField(verbose_name='Пользователь', max_length=70)
    comment = models.TextField(verbose_name='Комментарий', max_length=3000)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

