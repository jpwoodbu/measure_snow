from django.core.cache import cache
from django.db import models
from measure_snow.util import get_current_season

class SnowSeason(models.Model):
    """SnowSeason represents the time of the year that snow tends to fall.

    Since a season of snowfall usually spans two calendar years we don't want
    to associate the snowfall only by calendar year.  SnowSeasons tend to be
    defined by adjacent years (i.e. 2010-2011).  This app was built with the
    assumption the naming convention shown above will be followed.

    """
    name = models.CharField(max_length=11)

    class Meta:
        ordering = ["name"]

    def __unicode__(self):
        return self.name

class SnowfallMeasure(models.Model):
    """SnowfallMeasure is a mesaure of snowfall at any given time."""

    season = models.ForeignKey(SnowSeason, default=get_current_season)
    timestamp = models.DateTimeField()
    inches = models.DecimalField(max_digits=4, decimal_places=1)

    def __unicode__(self):
        return self.timestamp.ctime()
