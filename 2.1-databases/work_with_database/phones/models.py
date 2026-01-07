# python manage.py migrate
from django.db import models
from django.core.validators import MinValueValidator

class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    image = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.id};" \
               f" {self.name};" \
               f" {self.price};" \
               f" {self.image};" \
               f" {self.release_date};" \
               f" {self.lte_exists};" \
               f" {self.slug}"