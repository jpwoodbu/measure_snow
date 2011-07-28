import csv
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ValidationError
from measure_snow import models

class Command(BaseCommand):
    args = '<SnowSeason name> <CSV file path>'
    help = '''Imports snowfall measures from a CSV file.

Each row of CSV data should be:
<date>,<inches>

For example:
mm/dd/yy,inches with one decimal place
11/12/11,4.5'''

    def handle(self, *args, **options):
        season_name = args[0]
        try:
            season = models.SnowSeason.objects.get(name=season_name)
        except models.SnowSeason.DoesNotExist:
            raise CommandError("SnowSeason with name %s does not exist" % season_name)

        csv_filename = args[1]
        try:
            csv_fh = open(csv_filename, 'rb')
        except IOError:
            raise CommandError("Could not open %s" % csv_filename)

        csv_reader = csv.reader(csv_fh)
        for row in csv_reader:
            try:
                timestamp = datetime.strptime(row[0], "%m/%d/%y")
            except ValueError:
                self.stderr.write('The row(%r) has a date that cannot be parsed. Skipping this row...\n' % row)
                continue

            measure = models.SnowfallMeasure(timestamp=timestamp, season=season, inches=row[1])
            try:
                measure.save()
                self.stdout.write('Successfully created SnowfallMeasure.\n')
            except ValidationError:
                self.stderr.write('The row(%r) likely has a value for inches that cannot be parsed. Skipping this row...\n' % row)
                continue
