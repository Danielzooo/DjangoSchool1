from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie, Category, Actor
from .forms import ReviewForm


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'html/movies.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'html/moviesingle.html'
    slug_field = 'url'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class AddReviews(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ActorView(DetailView):
    model = Actor
    template_name = 'html/actor.html'
    slug_field = 'name'