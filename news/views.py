from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import View, DetailView, ListView

from .forms import *
from .models import *


class GenreYearFilter:

    def get_genre(self):
        return MovieGenre.objects.all()

    def get_category(self):
        return MovieCategory.objects.all()

    # def get_age(self):
    #     return Movie.objects.values('age')


class MovieListView(GenreYearFilter, ListView):
    template_name = 'news/movie_list.html'
    model = Movie
    paginate_by = 4

    def get_queryset(self):
        return Movie.objects.filter(is_published=True)


class MovieDetailView(GenreYearFilter, DetailView):
    model = Movie
    template_name = 'news/movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ActorDirectorView(GenreYearFilter, DetailView):
    model = MovieDirectorActor
    template_name = 'news/director_actor.html'


class AddComment(View):
    def post(self, request, pk):
        context = {}
        form = AddCommentForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        else:
            context['add_comment'] = form
            print(request.POST)
        return redirect(movie.get_absolute_url())


class MovieFilterView(GenreYearFilter, ListView):

    def get_queryset(self):
        return Movie.objects.filter(
                (
                    Q(category__in=self.request.GET.getlist('category')) &
                    Q(genre__in=self.request.GET.getlist('genre'))
                )
            ).distinct()


class SearchView(GenreYearFilter, ListView):
    paginate_by = 4

    def get_queryset(self):

        return Movie.objects.filter(
            Q(title__icontains=self.request.GET.get("q"))
        ).distinct()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        query = self.request.GET.get("q")
        context["q"] = f'q={query}&'
        return context




