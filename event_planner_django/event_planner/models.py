from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=150)
    date = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.IntegerField()
    img_url = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Donation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='reviews')
    amount = models.IntegerField()
    date = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment