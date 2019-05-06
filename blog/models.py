from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Paint(models.Model):
    color = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    type =  models.CharField(max_length=200)
    entered_date = models.DateTimeField(default=timezone.now)
    project_end_date = models.DateTimeField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.color
