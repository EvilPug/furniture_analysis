from django.db import models


class FurnitureModel(models.Model):

    id = models.IntegerField(primary_key=True)
    ven_code = models.CharField(max_length=6)
    category_name = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    furniture_color = models.CharField(max_length=100)
    furniture_type = models.CharField(max_length=100)
    furniture_sort = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    orig_price = models.IntegerField()
    disc_price = models.IntegerField()

    def __str__(self):
        return self.name
