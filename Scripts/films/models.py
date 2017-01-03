from django.db import models

class Film(models.Model):
    name = models.CharField(max_length=30)
    type = models.BooleanField()

    class Meta:
        db_table = "film"