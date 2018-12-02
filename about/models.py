from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    creater = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

















