from django.db import models

# Create your models here.

class Transit(models.Model):
    license_plate = models.CharField(max_length=20)
    car_brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    transit_date = models.DateTimeField()

    def __unicode__(self):
        return ','.join([self.license_plate,
                         self.car_brand,
                         self.car_model,
                         self.location,
                         str(self.transit_date)])
