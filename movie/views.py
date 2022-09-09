from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView
from .models import Movie, Category
from .forms import ReviewForm


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'html/movies.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class MovieDetailView(View):
    def get(self, request, slug):
        movies = Movie.objects.get(url=slug)
        return render(request, 'html/moviesingle.html', {'movie': movies})


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

