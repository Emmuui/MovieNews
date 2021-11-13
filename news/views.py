from django.views.generic import DetailView, ListView

from .models import *


class MovieListView(ListView):
    template_name = 'news/index.html'
    model = Movie
    queryset = Movie.objects.all().order_by('-date_published')
    paginate_by = 4

    # def get_queryset(self):
    #     return Movie.objects.filter(is_published=True)


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'news/movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
