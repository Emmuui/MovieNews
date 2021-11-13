from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class MovieCategory(models.Model):
    name = models.CharField(max_length=70, verbose_name='Категория')
    slug = models.SlugField(max_length=50, null=True, blank=True, unique=True, verbose_name='url')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class MovieGenre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Жанр')
    slug = models.SlugField(max_length=50, null=True, blank=True, unique=True, verbose_name='url')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f'{self.name}'


class MovieDirectorActor(models.Model):
    name = models.CharField(max_length=70, verbose_name='Имя')
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True, verbose_name='url')
    image = models.ImageField(verbose_name='Фотография', upload_to='director_actor/', blank=True, null=True)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Актер и режиссер'
        verbose_name_plural = 'Актеры и режиссеры'

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название фильма')
    title_eng = models.CharField(max_length=50, verbose_name='Название фильма на англ', null=True, blank=True)
    tagline = models.CharField(max_length=300, verbose_name='Слоган', null=True, blank=True)
    director = models.ManyToManyField(MovieDirectorActor, max_length=50,
                                      verbose_name='Режиссер', related_name='movie_director')
    actor = models.ManyToManyField(MovieDirectorActor, max_length=50, verbose_name='Актеры', related_name='movie_actor')
    country = models.CharField(max_length=100, verbose_name='Страна', null=True)
    age = models.CharField(max_length=100, verbose_name='Возраст', null=True)
    duration = models.IntegerField(verbose_name='Длительность(мин)', null=True)
    genre = models.ManyToManyField(MovieGenre, verbose_name='Жанр')
    category = models.ForeignKey(MovieCategory, verbose_name='Категория', null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True, verbose_name='url')
    image = models.ImageField(upload_to='movie_image/', verbose_name='Изображение')
    release_date = models.IntegerField(verbose_name='Год выпуска')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
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


class MovieComment(models.Model):
    email = models.EmailField(verbose_name='Email')
    user_name = models.CharField(verbose_name='Пользователь', max_length=70)
    comment = models.TextField(verbose_name='Комментарий', max_length=3000)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

