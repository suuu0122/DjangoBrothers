from django.db import models



class Player(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)
    birth_date = models.DateField(blank=True)
    introduction = models.TextField(blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name