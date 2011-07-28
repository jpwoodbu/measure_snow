from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import Context, loader
from measure_snow import models
from measure_snow import util


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

# Aggregate the measures by month into a list in chronological order.  Since
# the measures themselves are ordered by timestamp we just have to be careful
# to make a single list element for each month.
    month_measures = []
    current_index = None
    prev_month = None
    for measure in all_measures:
# Get the month abbreviation
        month = measure.timestamp.strftime("%b")
        if current_index == None:
            month_measures.append({'month': month, 'inches': measure.inches})
            current_index = 0
        elif prev_month == month:
            month_measures[current_index]['inches'] += measure.inches
        else:
            month_measures.append({'month': month, 'inches': measure.inches})
            current_index += 1
        prev_month = month

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

# Aggregate the measures by season into a list in chronological order.  Since
# the measures themselves are ordered by timestamp we just have to be careful
# to make a single list element for each month.
    season_measures = []
    current_index = None
    prev_season = None
    for measure in all_measures:
        if current_index == None:
            season_measures.append({'season': measure.season, 'inches': measure.inches})
            current_index = 0
        elif prev_season == measure.season:
            season_measures[current_index]['inches'] += measure.inches
        else:
            season_measures.append({'season': measure.season, 'inches': measure.inches})
            current_index += 1
        prev_season = measure.season

    t = loader.get_template('xml_season_summaries.tpl')
    c = Context({
        'measures': season_measures,
    })

    response = HttpResponse(t.render(c))
    response['Content-Type'] = 'application/xml'
    
    return response
