from django.urls import path
from . import views

urlpatterns = [
    path('', views.MoviesView.as_view()),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='moviesingle'),
    path('review/<int:pk>/', views.AddReviews.as_view(), name='add_review'),
]


