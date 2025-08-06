from django.db import models

from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Menu(models.Model):
    items = models.TextField(null=True) # список страв
    day = models.DateField()
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f'Menu for {self.day} at {self.restaurant.name}'


class Vote(models.Model):
    vote_time = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.employee.name} voted for {self.menu} at {self.vote_time}'
