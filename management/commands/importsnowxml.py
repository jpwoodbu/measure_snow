from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from measure_snow import models
from xml.etree import ElementTree

class Command(BaseCommand):
    args = '<SnowSeason name> <initial year> <Fusion Charts XML file path>'
    help = 'Imports snowfall measures from a FusionChart XML document'

    def handle(self, *args, **options):
        season_name = args[0]
        try:
            season = models.SnowSeason.objects.get(name=season_name)
        except models.SnowSeason.DoesNotExist:
            raise CommandError("SnowSeason with name %s does not exist" % season_name)

        xml_filename = args[2]
        try:
            xml_fh = open(xml_filename, 'r')
        except IOError:
            raise CommandError("Could not open %s" % xml_filename)

        try:
            xml = ElementTree.fromstring(xml_fh.read())
        except ElementTree.ParseError:
            raise CommandError("Could not parse XML in %s" % xml_filename)
        finally:
            xml_fh.close()

        prev_month = None
        year = int(args[1])
# Get all the set tags under parent tag (usually 'graph')
        for x in xml.getiterator(tag='set'):
# Since the set tags don't contain a year component in their 'name' (used as a
# date), lets assume, for now, that the year for this snowfall measure is the
# year provided in the arguments.  We'll later consider changing it.
            timestamp = datetime.strptime(x.attrib['name'] + '/%s' % year, '%m/%d/%Y')
            inches = x.attrib['value']

# If this is the first iteration then let's assume that we alreay have the
# correct year.  If not, let's increment the year if the month we're looking
# at now is numerically less than the previous month seen.
            if prev_month != None and timestamp.month < prev_month:
                year += 1
                timestamp = datetime.strptime(x.attrib['name'] + '/%s' % year, '%m/%d/%Y')

            prev_month = timestamp.month
            measure = models.SnowfallMeasure(timestamp=timestamp, inches=inches, season=season)
            measure.save()
            self.stdout.write('Successfully created SnowfallMeasure.\n')
