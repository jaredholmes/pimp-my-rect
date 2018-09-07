from django.db import models
from django.conf import settings

class Rectangle(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()
    border_radius = models.IntegerField()
    background_color = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
