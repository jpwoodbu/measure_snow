from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import Context, loader
from measure_snow import models


def show_season_by_measure(request, season_name):
    """Returns XML with each SnowfallMeasure for a given season

    The XML we returned is meant to be consumed by FusionCharts.

    """
    try:
        season = models.SnowSeason.objects.get(name=season_name)
    except ObjectDoesNotExist:
        return HttpResponse("That season does not exist.")

    measures = models.SnowfallMeasure.objects.filter(season=season).order_by('timestamp')
    t = loader.get_template('xml_season_by_measure.tpl')
    c = Context({
        'season_name': season.name,
        'measures': measures,
    })

    response = HttpResponse(t.render(c))
    response['Content-Type'] = 'application/xml'
    
    return response


def show_season_by_month(request, season_name):
    """Returns XML with a sum of SnowfallMeasures by month for a given season

    The XML returned is meant to be consumed by FusionCharts.

    """
    try:
        season = models.SnowSeason.objects.get(name=season_name)
    except ObjectDoesNotExist:
        return HttpResponse("That season does not exist.")

    all_measures = models.SnowfallMeasure.objects.filter(season=season).order_by('timestamp')

    month_measures = {}
    for measure in all_measures:
        month = measure.timestamp.strftime("%b")
        if month in month_measures:
            month_measures[month] += measure.inches
        else:
            month_measures[month] = measure.inches

    t = loader.get_template('xml_season_by_month.tpl')
    c = Context({
        'season_name': season.name,
        'measures': month_measures,
    })

    response = HttpResponse(t.render(c))
    response['Content-Type'] = 'application/xml'
    
    return response


def show_season_summaries(request):
    """Returns XML with a sum of SnowfallMeasures by seaon

    The XML returned is meant to be consumed by FusionCharts.

    """
    all_measures = models.SnowfallMeasure.objects.all().order_by('timestamp')

    season_measures = {}
    for measure in all_measures:
        season = measure.season.name
        if season in season_measures:
            season_measures[season] += measure.inches
        else:
            season_measures[season] = measure.inches

    t = loader.get_template('xml_season_summaries.tpl')
    c = Context({
        'measures': season_measures,
    })

    response = HttpResponse(t.render(c))
    response['Content-Type'] = 'application/xml'
    
    return response
