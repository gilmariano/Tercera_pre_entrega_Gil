from django.db import models


class Model1(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()


class Model2(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.TextField()


class Model3(models.Model):
    field1 = models.EmailField()
    field2 = models.DateField()
