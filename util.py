from datetime import date
from django.core.exceptions import ObjectDoesNotExist
from . import models

def get_current_season():
    """Try to return the current Season

    As a convenience, we want to set the default value of the season property
    of SnowfallMeasure objects to the current season.  But since seasons span
    two calendar years it can be hard to guess what season we're in.

    We'll first assume that the current year is the earlier component in the
    name of the SnowSeason (i.e. 2010-2011).  If that doesn't yield an
    existing SnowSeason object, we'll try using the current year as the later
    component in the SnowSeason name.

    """
    year = date.today().year
    season_name = "%s-%s" % (str(year), str(year + 1))
    try:
        return models.SnowSeason.objects.get(name=season_name)
    except ObjectDoesNotExist:
        season_name = "%s-%s" % (str(year - 1), str(year))
        return models.SnowSeason.objects.get(name=season_name)
