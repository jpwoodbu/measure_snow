from django.urls import path

from . import views

urlpatterns = [
    path('season_by_measure/<str:season_name>/', views.show_season_by_measure,
        name='show_season_by_measure'),
    path('season_by_month/<str:season_name>/', views.show_season_by_month,
        name='show_season_by_month'),
    path('season_summaries/', views.show_season_summaries,
        name='show_season_summaries'),
    path('season_summary/<str:season_name>/', views.show_season_summary,
        name='show_season_summary'),
    path('snowfall_today/', views.show_sum_for_today,
        name='show_sum_for_today')
]
