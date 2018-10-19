from django.db import models
from django.db import transaction
#from io import open
import csv
import sys

# Create your models here.
class Lock(models.Model):
  opened = models.BooleanField(default=False)
  expired = models.BooleanField(default=False)
  code = models.TextField(default='', blank=True)
  activated_at = models.DateTimeField(blank=True, null=True)
  computer = models.TextField(default='', blank=True)
  username = models.TextField(default='', blank=True)

# __ FILL DATA __

def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]


@transaction.atomic
def _fillCodes():
  with open('locker/Kode.csv') as csvfile:
    stream = unicode_csv_reader(csvfile)
    for row in stream:
      print 'importing code = ' + row[0] + '              \r',
      sys.stdout.flush()
      lock = Lock(code=row[0])
      lock.save()
  print()  # prev print was not line terminated
  print("done Kode.csv")


def fillData():
  _fillCodes()
  return "done"
