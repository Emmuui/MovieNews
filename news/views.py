from django.shortcuts import redirect
from django.views.generic import View, DetailView, ListView

from .forms import *
from .models import *


class MovieListView(ListView):
    template_name = 'news/index.html'
    model = Movie
    queryset = Movie.objects.all().order_by('-date_published')
    paginate_by = 4

    def get_queryset(self):
        return Movie.objects.filter(is_published=True)


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'news/movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddComment(View):
    def post(self, request, pk):
        context = {}
        form = AddCommentForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        else:
            context['add_comment'] = form
            print(request.POST)
        return redirect(movie.get_absolute_url())
