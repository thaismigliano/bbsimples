from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class State(models.Model):
  name = models.CharField(max_length=100, unique=True)
  acronym = models.CharField(max_length=2, default="NA")
  climate_date_url = models.URLField(unique=True)

  def __str__(self):
    return self.name


class City(models.Model):
  state = models.ForeignKey('State')
  name = models.CharField(max_length=100)
  climate_date_url = models.URLField()

  def __str__(self):
    return self.name


class Temperature(models.Model):
  city = models.ForeignKey('City')
  month = models.IntegerField()
  t_min_c = models.FloatField()
  t_max_c = models.FloatField()
  t_avg_c = models.FloatField()
  rain = models.FloatField()


class Location(models.Model):
  state = models.ForeignKey(State)
  city = ChainedForeignKey(
      City,
      chained_field="state",
      chained_model_field="state",
      show_all=False
  )
