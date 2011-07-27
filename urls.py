from django.conf.urls.defaults import patterns

urlpatterns = patterns('measure_snow.views',
    (r'^season_by_measure/(?P<season_name>\d+-\d+)/$', 'show_season_by_measure'),
    (r'^season_by_month/(?P<season_name>\d+-\d+)/$', 'show_season_by_month'),
    (r'^season_summaries/$', 'show_season_summaries'),
)
