from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=50)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()
    coordinates_lng = models.DecimalField(max_digits=20, decimal_places=14)
    coordinates_lat = models.DecimalField(max_digits=20, decimal_places=14)

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()
    order_number = models.IntegerField(default=1)

    class Meta(object):
        ordering = ['order_number']


    def __str__(self):
        return self.image.name
