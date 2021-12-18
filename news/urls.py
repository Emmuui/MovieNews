from django.urls import path
from .views import *

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('movie_filter/', MovieFilterView.as_view(), name='movie_filter'),
    path('search/', SearchView.as_view(), name='search'),
    path('movie/<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('actor_director/<slug:slug>/', ActorDirectorView.as_view(), name='director_actor_detail'),
    path('comment/<int:pk>/', AddComment.as_view(), name='add_comment'),
]
