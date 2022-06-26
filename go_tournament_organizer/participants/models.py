from django.db import models

# Create your models here.

class Participant(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    hometown = models.CharField(max_length=255)
    strength_number = models.IntegerField()
    strength_type = models.CharField(max_length=1)
    attending = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ", " + str(self.strength_number) + self.strength_type
