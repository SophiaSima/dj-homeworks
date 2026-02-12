from django.db import models

class Sensor:
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Measurement:
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='measurements/', null=True, blank=True)
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name='measurements')

    def __str__(self):
        return f'{self.sensor.name}: {self.temperature}C'