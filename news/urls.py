from django.urls import path
from .views import *

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path("movie/<slug:slug>/", MovieDetailView.as_view(), name="movie_detail"),
]
