from django import template
from django_movie.movie.models import Category, Movie


register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('movie/templates/html/tags/last_movie.html')
def get_last_movies():
    movies = Movie.objects.order_by('id')[:5]
    return {'last_movies': movies}
