from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=60)
    price = models.IntegerField(default=1)

    def __str__(self):
        return self.name
