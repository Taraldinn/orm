from django.db import models

# Create your models here.
FAV_COLOUR= [
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('yellow', 'Yellow'),
    ('black', 'Black'),
]

class Person(models.Model):
    
    class Colours(models.TextChoices):
        RED = 'red', 'Red'
        BLUE = 'blue', 'Blue'
        
    name = models.CharField(max_length=100)
    colour = models.CharField(max_length=50, choices=Colours.choices)
    