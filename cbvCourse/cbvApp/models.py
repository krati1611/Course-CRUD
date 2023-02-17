from django.db import models
from django.urls import reverse

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    instructor = models.CharField(max_length=20)
    rating = models.IntegerField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
